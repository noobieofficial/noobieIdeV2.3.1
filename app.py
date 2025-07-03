#!/usr/bin/env python3

import eventlet
eventlet.monkey_patch()

from flask import Flask, render_template, request, jsonify, session
from flask_socketio import SocketIO, emit
import os
import sys
import threading
import queue
import uuid
import tempfile
import shutil
import signal
import time
import json
from datetime import datetime
import subprocess
import io
import contextlib


# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Try to import Noobie interpreter
try:
    from noobie02 import NoobieInterpreter
    from func import *
except ImportError as e:
    print(f"Error importing Noobie modules: {e}")
    print("Make sure noobie02.py and func.py are in the same directory")
    # For development without the files, create a simple stub
    class NoobieInterpreter:
        def __init__(self):
            self.variables = {}
            
        def _process_line(self, line, line_num):
            # Simple stub implementation
            line = line.strip()
            if line.startswith('SAY'):
                msg = line[3:].strip().strip('"\'')
                print(msg)
            elif line.startswith('CREATE'):
                parts = line.split()
                if len(parts) >= 3:
                    var_name = parts[2]
                    var_value = parts[3] if len(parts) > 3 else "0"
                    self.variables[var_name] = var_value
            elif line.startswith('LISTEN'):
                parts = line.split()
                if len(parts) >= 3:
                    var_name = parts[2]
                    prompt = ' '.join(parts[3:]).strip('"\'')
                    value = input(prompt)
                    self.variables[var_name] = value
            else:
                print(f"Command not implemented in stub: {line}")
                
        def interpret(self, code):
            lines = code.split('\n')
            for i, line in enumerate(lines):
                if line.strip():
                    self._process_line(line, i + 1)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'noobie-secret-key-2024')
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

# Global storage for active sessions
active_sessions = {}
session_interpreters = {}
session_threads = {}
session_inputs = {}


class WebOutputCapture:
    """Capture output for web display"""
    def __init__(self, session_id, output_type='stdout'):
        self.session_id = session_id
        self.output_type = output_type
        self.buffer = ""
        
    def write(self, text):
        if text.strip():
            socketio.emit('output', {
                'type': self.output_type,
                'text': text,
                'timestamp': datetime.now().isoformat()
            }, room=self.session_id)
        
    def flush(self):
        pass


class WebInputHandler:
    """Handle input requests for web interface"""
    def __init__(self, session_id):
        self.session_id = session_id
        self.input_queue = queue.Queue()
        self.waiting_for_input = False
        
    def get_input(self, prompt=''):
        """Get input from web interface"""
        # Send input request to frontend
        socketio.emit('input_request', {
            'prompt': prompt,
            'timestamp': datetime.now().isoformat()
        }, room=self.session_id)
        
        self.waiting_for_input = True
        
        # Wait for input response
        try:
            result = self.input_queue.get(timeout=300)  # 5 minute timeout
            return result
        except queue.Empty:
            return ""
        finally:
            self.waiting_for_input = False
            
    def provide_input(self, input_text):
        """Provide input from web interface"""
        if self.waiting_for_input:
            self.input_queue.put(input_text)
            return True
        return False


class NoobieWebInterpreter:
    """Web-adapted Noobie interpreter"""
    def __init__(self, session_id):
        self.session_id = session_id
        self.interpreter = NoobieInterpreter()
        self.output_capture = WebOutputCapture(session_id)
        self.error_capture = WebOutputCapture(session_id, 'stderr')
        self.input_handler = WebInputHandler(session_id)
        self.running = False
        self.paused = False
        
    def setup_io_redirection(self):
        """Setup input/output redirection"""
        # Store original handlers
        self.original_stdout = sys.stdout
        self.original_stderr = sys.stderr
        self.original_input = __builtins__['input'] if isinstance(__builtins__, dict) else __builtins__.input
        
        # Redirect to web handlers
        sys.stdout = self.output_capture
        sys.stderr = self.error_capture
        
        # Custom input function
        def web_input(prompt=''):
            return self.input_handler.get_input(prompt)
            
        if isinstance(__builtins__, dict):
            __builtins__['input'] = web_input
        else:
            __builtins__.input = web_input
            
    def restore_io(self):
        """Restore original input/output"""
        sys.stdout = self.original_stdout
        sys.stderr = self.original_stderr
        
        if isinstance(__builtins__, dict):
            __builtins__['input'] = self.original_input
        else:
            __builtins__.input = self.original_input
            
    def execute_line(self, line):
        """Execute a single line of code"""
        if not line.strip() or line.strip().startswith('#'):
            return True
            
        try:
            # Setup IO redirection
            self.setup_io_redirection()
            
            # Execute the line using the process_line method
            self.interpreter._process_line(line.strip(), 1)
            
            # Send success signal
            socketio.emit('line_executed', {
                'line': line,
                'success': True,
                'timestamp': datetime.now().isoformat()
            }, room=self.session_id)
            
            return True
            
        except Exception as e:
            # Send error
            socketio.emit('line_executed', {
                'line': line,
                'success': False,
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }, room=self.session_id)
            
            socketio.emit('output', {
                'type': 'error',
                'text': f"Error: {str(e)}\n",
                'timestamp': datetime.now().isoformat()
            }, room=self.session_id)
            
            return False
            
        finally:
            # Restore IO
            self.restore_io()
            
    def execute_code(self, code):
        """Execute full code with real-time execution"""
        self.running = True
        
        try:
            # Setup IO redirection
            self.setup_io_redirection()
            
            # Send execution started signal
            socketio.emit('execution_started', {
                'timestamp': datetime.now().isoformat()
            }, room=self.session_id)
            
            # Execute the entire code using the original interpreter
            self.interpreter.interpret(code)
            
        except Exception as e:
            socketio.emit('output', {
                'type': 'error',
                'text': f"Execution error: {str(e)}\n",
                'timestamp': datetime.now().isoformat()
            }, room=self.session_id)
            
        finally:
            self.running = False
            self.restore_io()
            socketio.emit('execution_finished', {
                'timestamp': datetime.now().isoformat()
            }, room=self.session_id)


@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')


@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})


@socketio.on('connect')
def handle_connect():
    """Handle client connection"""
    session_id = str(uuid.uuid4())
    session['session_id'] = session_id
    
    # Create new interpreter for this session
    interpreter = NoobieWebInterpreter(session_id)
    active_sessions[session_id] = interpreter
    session_interpreters[session_id] = interpreter
    
    # Join room
    from flask_socketio import join_room
    join_room(session_id)
    
    emit('connected', {
        'session_id': session_id,
        'timestamp': datetime.now().isoformat()
    })
    
    print(f"Client connected: {session_id}")


@socketio.on('disconnect')
def handle_disconnect():
    """Handle client disconnection"""
    session_id = session.get('session_id')
    if session_id:
        # Stop any running code
        if session_id in active_sessions:
            active_sessions[session_id].running = False
            
        # Clean up
        active_sessions.pop(session_id, None)
        session_interpreters.pop(session_id, None)
        session_threads.pop(session_id, None)
        session_inputs.pop(session_id, None)
        
        print(f"Client disconnected: {session_id}")


@socketio.on('execute_code')
def handle_execute_code(data):
    """Handle code execution request"""
    session_id = session.get('session_id')
    if not session_id or session_id not in active_sessions:
        emit('error', {'message': 'Invalid session'})
        return
        
    code = data.get('code', '').strip()
    if not code:
        emit('error', {'message': 'No code provided'})
        return
        
    interpreter = active_sessions[session_id]
    
    # Stop any running code
    if interpreter.running:
        interpreter.running = False
        time.sleep(0.1)
        
    # Create new interpreter for fresh execution
    interpreter = NoobieWebInterpreter(session_id)
    active_sessions[session_id] = interpreter
    
    # Execute in separate thread
    def execute_thread():
        try:
            interpreter.execute_code(code)
        except Exception as e:
            socketio.emit('output', {
                'type': 'error',
                'text': f"Thread error: {str(e)}\n",
                'timestamp': datetime.now().isoformat()
            }, room=session_id)
            
    thread = threading.Thread(target=execute_thread, daemon=True)
    session_threads[session_id] = thread
    thread.start()


@socketio.on('execute_line')
def handle_execute_line(data):
    """Handle single line execution"""
    session_id = session.get('session_id')
    if not session_id or session_id not in active_sessions:
        emit('error', {'message': 'Invalid session'})
        return
        
    line = data.get('line', '').strip()
    if not line:
        return
        
    interpreter = active_sessions[session_id]
    
    # Execute in separate thread for non-blocking operation
    def execute_line_thread():
        try:
            interpreter.execute_line(line)
        except Exception as e:
            socketio.emit('output', {
                'type': 'error',
                'text': f"Line execution error: {str(e)}\n",
                'timestamp': datetime.now().isoformat()
            }, room=session_id)
            
    thread = threading.Thread(target=execute_line_thread, daemon=True)
    thread.start()


@socketio.on('stop_execution')
def handle_stop_execution():
    """Handle stop execution request"""
    session_id = session.get('session_id')
    if session_id and session_id in active_sessions:
        active_sessions[session_id].running = False
        emit('execution_stopped', {
            'timestamp': datetime.now().isoformat()
        })


@socketio.on('pause_execution')
def handle_pause_execution():
    """Handle pause execution request"""
    session_id = session.get('session_id')
    if session_id and session_id in active_sessions:
        active_sessions[session_id].paused = True
        emit('execution_paused', {
            'timestamp': datetime.now().isoformat()
        })


@socketio.on('resume_execution')
def handle_resume_execution():
    """Handle resume execution request"""
    session_id = session.get('session_id')
    if session_id and session_id in active_sessions:
        active_sessions[session_id].paused = False
        emit('execution_resumed', {
            'timestamp': datetime.now().isoformat()
        })


@socketio.on('provide_input')
def handle_provide_input(data):
    """Handle input from user"""
    session_id = session.get('session_id')
    if not session_id or session_id not in active_sessions:
        emit('error', {'message': 'Invalid session'})
        return
        
    input_text = data.get('input', '')
    interpreter = active_sessions[session_id]
    
    # Provide input to interpreter
    if interpreter.input_handler.provide_input(input_text):
        emit('input_provided', {
            'input': input_text,
            'timestamp': datetime.now().isoformat()
        })
        
        # Also send to output for display
        socketio.emit('output', {
            'type': 'input_echo',
            'text': input_text + '\n',
            'timestamp': datetime.now().isoformat()
        }, room=session_id)
    else:
        emit('error', {'message': 'Not waiting for input'})


@socketio.on('reset_interpreter')
def handle_reset_interpreter():
    """Reset the interpreter"""
    session_id = session.get('session_id')
    if session_id and session_id in active_sessions:
        # Stop current execution
        active_sessions[session_id].running = False
        
        # Create new interpreter
        interpreter = NoobieWebInterpreter(session_id)
        active_sessions[session_id] = interpreter
        
        emit('interpreter_reset', {
            'timestamp': datetime.now().isoformat()
        })


# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


# Cleanup on shutdown
def cleanup_sessions():
    """Cleanup all active sessions"""
    for session_id in list(active_sessions.keys()):
        if session_id in active_sessions:
            active_sessions[session_id].running = False
    
    active_sessions.clear()
    session_interpreters.clear()
    session_threads.clear()
    session_inputs.clear()


def signal_handler(sig, frame):
    """Handle shutdown signals"""
    print("\nShutting down...")
    cleanup_sessions()
    sys.exit(0)


# Register signal handlers
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


if __name__ == '__main__':
    # For development
    print("Starting Noobie Web IDE...")
    print("Open your browser to: http://localhost:5000")
    
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    
    # Run the application


    socketio.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
