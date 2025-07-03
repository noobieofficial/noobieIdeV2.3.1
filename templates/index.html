<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Noobie Web IDE</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        :root {
            --primary-color: #2563eb;
            --secondary-color: #1e40af;
            --success-color: #16a34a;
            --error-color: #dc2626;
            --warning-color: #ca8a04;
            --bg-color: #0f172a;
            --surface-color: #1e293b;
            --text-color: #e2e8f0;
            --text-muted: #94a3b8;
            --border-color: #334155;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: var(--bg-color);
            color: var(--text-color);
            height: 100vh;
            overflow: hidden;
        }

        .container {
            display: flex;
            flex-direction: column;
            height: 100vh;
        }

        .header {
            background: var(--surface-color);
            padding: 0.75rem;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            flex-wrap: wrap;
            gap: 0.75rem;
        }

        .logo {
            font-size: 1.25rem;
            font-weight: bold;
            color: var(--primary-color);
            white-space: nowrap;
        }

        .toolbar {
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
        }

        .btn {
            padding: 0.5rem 1rem;
            border: none;
            border-radius: 0.375rem;
            font-size: 0.875rem;
            cursor: pointer;
            transition: all 0.15s ease;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            white-space: nowrap;
        }

        .btn:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        .btn-primary {
            background: var(--primary-color);
            color: white;
        }

        .btn-primary:hover {
            background: var(--secondary-color);
        }

        .btn-danger {
            background: var(--error-color);
            color: white;
        }

        .btn-danger:hover {
            background: #b91c1c;
        }

        .btn-secondary {
            background: var(--border-color);
            color: var(--text-color);
        }

        .btn-secondary:hover {
            background: #475569;
        }

        .status-bar {
            background: var(--surface-color);
            padding: 0.5rem 1rem;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.875rem;
            color: var(--text-muted);
            min-height: 2.5rem;
        }

        .status-indicator {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .status-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--success-color);
            flex-shrink: 0;
        }

        .status-dot.disconnected {
            background: var(--error-color);
        }

        .status-dot.executing {
            background: var(--warning-color);
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }

        .main-content {
            flex: 1;
            display: flex;
            overflow: hidden;
            min-height: 0;
        }

        .editor-panel {
            flex: 1;
            display: flex;
            flex-direction: column;
            min-width: 0;
            border-right: 1px solid var(--border-color);
        }

        .editor-header {
            background: var(--surface-color);
            padding: 0.75rem 1rem;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-shrink: 0;
        }

        .editor-title {
            font-weight: 600;
            color: var(--text-color);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .editor-actions {
            display: flex;
            gap: 0.5rem;
        }

        .editor-container {
            flex: 1;
            position: relative;
            overflow: hidden;
            display: flex;
            min-height: 0;
        }

        .line-numbers {
            width: 50px;
            background: var(--surface-color);
            color: var(--text-muted);
            padding: 1rem 0.5rem;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            line-height: 1.5rem;
            border-right: 1px solid var(--border-color);
            user-select: none;
            overflow-y: hidden;
            overflow-x: hidden;
            text-align: right;
            flex-shrink: 0;
            display: flex;
            flex-direction: column;
        }

        .line-numbers > div {
            height: 1.5rem;
            line-height: 1.5rem;
            padding-right: 0.5rem;
        }

        .editor {
            flex: 1;
            padding: 1rem;
            background: var(--bg-color);
            color: var(--text-color);
            border: none;
            outline: none;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            line-height: 1.5rem;
            resize: none;
            tab-size: 4;
            white-space: pre;
            overflow: auto;
            min-width: 0;
        }

        .editor:focus {
            background: var(--bg-color);
        }

        .output-panel {
            width: 40%;
            display: flex;
            flex-direction: column;
            background: var(--surface-color);
            min-width: 0;
        }

        .output-header {
            padding: 0.75rem 1rem;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-shrink: 0;
        }

        .output-title {
            font-weight: 600;
            color: var(--text-color);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .output-container {
            flex: 1;
            display: flex;
            flex-direction: column;
            min-height: 0;
        }

        .output {
            flex: 1;
            padding: 1rem;
            background: #111827;
            color: #f9fafb;
            font-family: 'Courier New', monospace;
            font-size: 13px;
            line-height: 1.4;
            overflow-y: auto;
            white-space: pre-wrap;
            word-wrap: break-word;
            min-height: 0;
        }

        .output-line {
            margin-bottom: 0.25rem;
        }

        .output-line.error {
            color: #fca5a5;
        }

        .output-line.success {
            color: #86efac;
        }

        .output-line.warning {
            color: #fbbf24;
        }

        .output-line.info {
            color: #7dd3fc;
        }

        .output-line.input-echo {
            color: #c084fc;
            font-weight: bold;
        }

        .input-panel {
            padding: 1rem;
            background: var(--surface-color);
            border-top: 1px solid var(--border-color);
            display: none;
            flex-shrink: 0;
        }

        .input-panel.active {
            display: flex;
            gap: 0.5rem;
            align-items: center;
        }

        .input-prompt {
            color: var(--text-muted);
            font-size: 0.875rem;
            min-width: fit-content;
            flex-shrink: 0;
        }

        .input-field {
            flex: 1;
            padding: 0.5rem;
            background: var(--bg-color);
            color: var(--text-color);
            border: 1px solid var(--border-color);
            border-radius: 0.375rem;
            font-family: 'Courier New', monospace;
            min-width: 0;
        }

        .input-field:focus {
            outline: none;
            border-color: var(--primary-color);
        }

        .progress-bar {
            height: 3px;
            background: var(--border-color);
            overflow: hidden;
        }

        .progress-fill {
            height: 100%;
            background: var(--primary-color);
            transition: width 0.3s ease;
            width: 0%;
        }

        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.5);
            z-index: 1000;
        }

        .modal.active {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 1rem;
        }

        .modal-content {
            background: var(--surface-color);
            padding: 2rem;
            border-radius: 0.5rem;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
            max-width: 500px;
            width: 100%;
            max-height: 90vh;
            overflow-y: auto;
        }

        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }

        .modal-title {
            font-size: 1.25rem;
            font-weight: 600;
        }

        .modal-close {
            background: none;
            border: none;
            font-size: 1.5rem;
            cursor: pointer;
            color: var(--text-muted);
        }

        .modal-close:hover {
            color: var(--text-color);
        }

        /* Mobile button group */
        .mobile-toolbar {
            display: none;
            background: var(--surface-color);
            padding: 0.5rem;
            border-top: 1px solid var(--border-color);
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            z-index: 100;
        }

        .mobile-toolbar-inner {
            display: flex;
            gap: 0.5rem;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
        }

        .mobile-toolbar .btn {
            flex-shrink: 0;
        }

        /* Responsive design */
        @media (max-width: 1024px) {
            .output-panel {
                width: 50%;
            }
        }

        @media (max-width: 768px) {
            .header {
                padding: 0.5rem;
            }

            .logo {
                font-size: 1.1rem;
            }

            .btn {
                padding: 0.375rem 0.75rem;
                font-size: 0.75rem;
            }

            .btn i {
                font-size: 0.875rem;
            }

            .main-content {
                flex-direction: column;
            }
            
            .editor-panel {
                border-right: none;
                border-bottom: 1px solid var(--border-color);
                flex: 1 1 60%;
            }
            
            .output-panel {
                width: 100%;
                flex: 1 1 40%;
            }

            .line-numbers {
                width: 40px;
                font-size: 12px;
                padding: 0.75rem 0.25rem;
            }

            .line-numbers > div {
                height: 1.5rem;
                line-height: 1.5rem;
                padding-right: 0.25rem;
            }

            .editor {
                font-size: 12px;
                padding: 0.75rem;
            }

            .toolbar {
                display: none;
            }

            .mobile-toolbar {
                display: block;
                padding-bottom: env(safe-area-inset-bottom, 0.5rem);
            }

            .container {
                padding-bottom: 60px;
            }
        }

        @media (max-width: 480px) {
            .header {
                justify-content: center;
            }

            .logo {
                font-size: 1rem;
            }

            .editor-actions {
                display: none;
            }

            .line-numbers {
                width: 35px;
                font-size: 11px;
            }

            .line-numbers > div {
                height: 1.5rem;
                line-height: 1.5rem;
                padding-right: 0.25rem;
            }

            .editor {
                font-size: 11px;
            }

            .output {
                font-size: 11px;
            }

            .modal-content {
                padding: 1rem;
            }

            .status-bar {
                font-size: 0.75rem;
                padding: 0.375rem 0.75rem;
            }
        }

        /* Landscape mode adjustments */
        @media (max-height: 500px) and (orientation: landscape) {
            .header {
                padding: 0.25rem 0.5rem;
            }

            .status-bar {
                display: none;
            }

            .editor-header, .output-header {
                padding: 0.5rem;
            }

            .main-content {
                flex-direction: row;
            }

            .editor-panel {
                border-right: 1px solid var(--border-color);
                border-bottom: none;
            }

            .output-panel {
                width: 50%;
            }
        }

        /* Syntax highlighting */
        .syntax-keyword { color: #569cd6; }
        .syntax-type { color: #4ec9b0; }
        .syntax-string { color: #ce9178; }
        .syntax-number { color: #b5cea8; }
        .syntax-comment { color: #6a9955; font-style: italic; }
        .syntax-variable { color: #9cdcfe; }
        .syntax-operator { color: #d4d4d4; }
        .syntax-boolean { color: #569cd6; }

        /* Touch-friendly adjustments */
        @media (hover: none) and (pointer: coarse) {
            .btn {
                min-height: 44px;
                min-width: 44px;
            }

            .input-field {
                min-height: 44px;
            }

            .modal-close {
                min-width: 44px;
                min-height: 44px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header class="header">
            <div class="logo">
                <i class="fas fa-code"></i>
                <span>Noobie Web IDE</span>
            </div>
            <div class="toolbar">
                <button class="btn btn-secondary" id="openFileBtn">
                    <i class="fas fa-folder-open"></i>
                    <span class="btn-text">Open</span>
                </button>
                <button class="btn btn-secondary" id="saveFileBtn">
                    <i class="fas fa-save"></i>
                    <span class="btn-text">Save</span>
                </button>
                <input type="file" id="fileInput" style="display:none;" accept=".noobie,.txt" />

                <button class="btn btn-primary" id="runBtn">
                    <i class="fas fa-play"></i>
                    <span class="btn-text">Run</span>
                </button>
                <button class="btn btn-danger" id="stopBtn" disabled>
                    <i class="fas fa-stop"></i>
                    <span class="btn-text">Stop</span>
                </button>
                <button class="btn btn-secondary" id="pauseBtn" disabled>
                    <i class="fas fa-pause"></i>
                    <span class="btn-text">Pause</span>
                </button>
                <button class="btn btn-secondary" id="resetBtn">
                    <i class="fas fa-refresh"></i>
                    <span class="btn-text">Reset</span>
                </button>
                <button class="btn btn-secondary" id="clearBtn">
                    <i class="fas fa-trash"></i>
                    <span class="btn-text">Clear</span>
                </button>
            </div>
        </header>

        <div class="status-bar">
            <div class="status-indicator">
                <div class="status-dot" id="statusDot"></div>
                <span id="statusText">Ready</span>
            </div>
            <div id="executionInfo"></div>
        </div>

        <div class="progress-bar">
            <div class="progress-fill" id="progressFill"></div>
        </div>

        <div class="main-content">
            <div class="editor-panel">
                <div class="editor-header">
                    <div class="editor-title">
                        <i class="fas fa-edit"></i>
                        <span>Code Editor</span>
                    </div>
                    <div class="editor-actions">
                        <button class="btn btn-secondary" id="executeLineBtn">
                            <i class="fas fa-terminal"></i>
                            <span class="btn-text">Execute Line</span>
                        </button>
                    </div>
                </div>
                <div class="editor-container">
                    <div class="line-numbers" id="lineNumbers">1</div>
                    <textarea class="editor" id="codeEditor" placeholder="Enter your Noobie code here..." spellcheck="false"></textarea>
                </div>
            </div>

            <div class="output-panel">
                <div class="output-header">
                    <div class="output-title">
                        <i class="fas fa-terminal"></i>
                        <span>Output</span>
                    </div>
                    <button class="btn btn-secondary" id="clearOutputBtn">
                        <i class="fas fa-eraser"></i>
                        <span class="btn-text">Clear</span>
                    </button>
                </div>
                <div class="output-container">
                    <div class="output" id="output"></div>
                    <div class="input-panel" id="inputPanel">
                        <div class="input-prompt" id="inputPrompt">Input:</div>
                        <input type="text" class="input-field" id="inputField" placeholder="Type your input here...">
                        <button class="btn btn-primary" id="submitInputBtn">
                            <i class="fas fa-paper-plane"></i>
                            <span class="btn-text">Submit</span>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Mobile Toolbar -->
    <div class="mobile-toolbar">
        <div class="mobile-toolbar-inner">
            <button class="btn btn-primary" id="mobileRunBtn">
                <i class="fas fa-play"></i>
            </button>
            <button class="btn btn-danger" id="mobileStopBtn" disabled>
                <i class="fas fa-stop"></i>
            </button>
            <button class="btn btn-secondary" id="mobileOpenBtn">
                <i class="fas fa-folder-open"></i>
            </button>
            <button class="btn btn-secondary" id="mobileSaveBtn">
                <i class="fas fa-save"></i>
            </button>
            <button class="btn btn-secondary" id="mobileResetBtn">
                <i class="fas fa-refresh"></i>
            </button>
            <button class="btn btn-secondary" id="mobileClearBtn">
                <i class="fas fa-trash"></i>
            </button>
            <button class="btn btn-secondary" id="mobileExecuteLineBtn">
                <i class="fas fa-terminal"></i>
            </button>
        </div>
    </div>

    <!-- Documentation Modal -->
    <div class="modal" id="docModal">
        <div class="modal-content">
            <div class="modal-header">
                <h3 class="modal-title">Noobie Language Documentation</h3>
                <button class="modal-close" id="closeDocModal">&times;</button>
            </div>
            <div class="modal-body">
                <h4>Basic Commands:</h4>
                <ul>
                    <li><strong>SAY</strong> - Output text: <code>SAY "Hello World"</code></li>
                    <li><strong>CREATE</strong> - Create variable: <code>CREATE INT age 25</code></li>
                    <li><strong>LISTEN</strong> - Get input: <code>LISTEN STR name "Enter name: "</code></li>
                    <li><strong>CHANGE</strong> - Change variable: <code>CHANGE age 30</code></li>
                    <li><strong>IF/ELSE/ENDO</strong> - Conditional: <code>IF @age > 18 DO ... ENDO</code></li>
                </ul>
                <h4>Data Types:</h4>
                <ul>
                    <li><strong>INT</strong> - Integer numbers</li>
                    <li><strong>FLOAT</strong> - Decimal numbers</li>
                    <li><strong>STR</strong> - Text strings</li>
                    <li><strong>BOOL</strong> - Boolean values</li>
                    <li><strong>CHAR</strong> - Single characters</li>
                </ul>
            </div>
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
    <script>
        class NoobieWebIDE {
            constructor() {
                this.socket = io();
                this.isConnected = false;
                this.isExecuting = false;
                this.currentLine = 0;
                this.totalLines = 0;
                
                this.initializeElements();
                this.setupEventListeners();
                this.setupSocketListeners();
                this.setupResponsiveFeatures();
            }

            initializeElements() {
                // UI Elements
                this.runBtn = document.getElementById('runBtn');
                this.stopBtn = document.getElementById('stopBtn');
                this.pauseBtn = document.getElementById('pauseBtn');
                this.resetBtn = document.getElementById('resetBtn');
                this.clearBtn = document.getElementById('clearBtn');
                this.executeLineBtn = document.getElementById('executeLineBtn');
                this.clearOutputBtn = document.getElementById('clearOutputBtn');
                
                // Mobile buttons
                this.mobileRunBtn = document.getElementById('mobileRunBtn');
                this.mobileStopBtn = document.getElementById('mobileStopBtn');
                this.mobileOpenBtn = document.getElementById('mobileOpenBtn');
                this.mobileSaveBtn = document.getElementById('mobileSaveBtn');
                this.mobileResetBtn = document.getElementById('mobileResetBtn');
                this.mobileClearBtn = document.getElementById('mobileClearBtn');
                this.mobileExecuteLineBtn = document.getElementById('mobileExecuteLineBtn');
                
                this.codeEditor = document.getElementById('codeEditor');
                this.lineNumbers = document.getElementById('lineNumbers');
                this.output = document.getElementById('output');
                
                this.inputPanel = document.getElementById('inputPanel');
                this.inputField = document.getElementById('inputField');
                this.inputPrompt = document.getElementById('inputPrompt');
                this.submitInputBtn = document.getElementById('submitInputBtn');
                
                this.statusDot = document.getElementById('statusDot');
                this.statusText = document.getElementById('statusText');
                this.executionInfo = document.getElementById('executionInfo');
                this.progressFill = document.getElementById('progressFill');

                this.openFileBtn = document.getElementById('openFileBtn');
                this.saveFileBtn = document.getElementById('saveFileBtn');
                this.fileInput = document.getElementById('fileInput');
            }

            setupEventListeners() {
                // Toolbar buttons
                this.runBtn.addEventListener('click', () => this.runCode());
                this.stopBtn.addEventListener('click', () => this.stopExecution());
                this.pauseBtn.addEventListener('click', () => this.pauseExecution());
                this.resetBtn.addEventListener('click', () => this.resetInterpreter());
                this.clearBtn.addEventListener('click', () => this.clearOutput());
                this.executeLineBtn.addEventListener('click', () => this.executeCurrentLine());
                this.clearOutputBtn.addEventListener('click', () => this.clearOutput());      
                this.openFileBtn.addEventListener('click', () => this.fileInput.click());
                this.fileInput.addEventListener('change', (e) => this.openFile(e));
                this.saveFileBtn.addEventListener('click', () => this.saveFile());

                // Mobile toolbar buttons
                this.mobileRunBtn.addEventListener('click', () => this.runCode());
                this.mobileStopBtn.addEventListener('click', () => this.stopExecution());
                this.mobileOpenBtn.addEventListener('click', () => this.fileInput.click());
                this.mobileSaveBtn.addEventListener('click', () => this.saveFile());
                this.mobileResetBtn.addEventListener('click', () => this.resetInterpreter());
                this.mobileClearBtn.addEventListener('click', () => this.clearOutput());
                this.mobileExecuteLineBtn.addEventListener('click', () => this.executeCurrentLine());

                // Input handling
                this.submitInputBtn.addEventListener('click', () => this.submitInput());
                this.inputField.addEventListener('keypress', (e) => {
                    if (e.key === 'Enter') {
                        this.submitInput();
                    }
                });
                
                // Editor events
                this.codeEditor.addEventListener('input', () => this.updateLineNumbers());
                this.codeEditor.addEventListener('scroll', () => this.syncLineNumbers());
                this.codeEditor.addEventListener('keydown', (e) => {
                    if (e.key === 'Tab') {
                        e.preventDefault();
                        this.insertTab();
                    }
                    if (e.ctrlKey && e.key === 'Enter') {
                        this.executeCurrentLine();
                    }
                    if (e.key === 'F5') {
                        e.preventDefault();
                        this.runCode();
                    }
                });
                
                // Window events
                window.addEventListener('beforeunload', () => {
                    if (this.isExecuting) {
                        return 'Code is currently executing. Are you sure you want to leave?';
                    }
                });
            }

            setupResponsiveFeatures() {
                // Resize observer for better line number sync
                if (window.ResizeObserver) {
                    const resizeObserver = new ResizeObserver(() => {
                        this.updateLineNumbers();
                    });
                    resizeObserver.observe(this.codeEditor);
                }

                // Orientation change handler
                window.addEventListener('orientationchange', () => {
                    setTimeout(() => {
                        this.updateLineNumbers();
                        this.syncLineNumbers();
                    }, 100);
                });

                // Initial setup
                this.updateLineNumbers();
            }

            setupSocketListeners() {
                this.socket.on('connect', () => {
                    this.isConnected = true;
                    this.updateConnectionStatus();
                });

                this.socket.on('disconnect', () => {
                    this.isConnected = false;
                    this.updateConnectionStatus();
                });

                this.socket.on('connected', (data) => {
                    console.log('Connected to server:', data.session_id);
                    this.addOutput('Connected to Noobie Web IDE', 'info');
                });

                this.socket.on('output', (data) => {
                    this.addOutput(data.text, data.type);
                });

                this.socket.on('input_request', (data) => {
                    this.showInputPanel(data.prompt);
                });

                this.socket.on('input_provided', (data) => {
                    this.hideInputPanel();
                });

                this.socket.on('execution_started', (data) => {
                    this.isExecuting = true;
                    this.totalLines = data.total_lines;
                    this.currentLine = 0;
                    this.updateExecutionUI();
                    this.addOutput('Execution started...', 'info');
                });

                this.socket.on('execution_finished', (data) => {
                    this.isExecuting = false;
                    this.updateExecutionUI();
                    this.addOutput('Execution finished.', 'success');
                    this.progressFill.style.width = '100%';
                    setTimeout(() => {
                        this.progressFill.style.width = '0%';
                    }, 1000);
                });

                this.socket.on('execution_stopped', (data) => {
                    this.isExecuting = false;
                    this.updateExecutionUI();
                    this.addOutput('Execution stopped by user.', 'warning');
                });

                this.socket.on('current_line', (data) => {
                    this.currentLine = data.line_number;
                    this.highlightCurrentLine(data.line_number);
                    this.updateProgress();
                });

                this.socket.on('line_executed', (data) => {
                    if (data.success) {
                        this.addOutput(`✓ Line ${this.currentLine}: ${data.line}`, 'success');
                    } else {
                        this.addOutput(`✗ Line ${this.currentLine}: ${data.error}`, 'error');
                        this.highlightErrorLine(this.currentLine);
                    }
                });

                this.socket.on('interpreter_reset', (data) => {
                    this.addOutput('Interpreter reset.', 'info');
                    this.clearHighlights();
                });

                this.socket.on('error', (data) => {
                    this.addOutput(`Error: ${data.message}`, 'error');
                });
            }

            updateConnectionStatus() {
                if (this.isConnected) {
                    this.statusDot.classList.remove('disconnected');
                    this.statusText.textContent = 'Connected';
                } else {
                    this.statusDot.classList.add('disconnected');
                    this.statusText.textContent = 'Disconnected';
                }
            }

            updateExecutionUI() {
                if (this.isExecuting) {
                    this.runBtn.disabled = true;
                    this.stopBtn.disabled = false;
                    this.pauseBtn.disabled = false;
                    this.mobileRunBtn.disabled = true;
                    this.mobileStopBtn.disabled = false;
                    this.statusDot.classList.add('executing');
                    this.statusText.textContent = 'Executing...';
                } else {
                    this.runBtn.disabled = false;
                    this.stopBtn.disabled = true;
                    this.pauseBtn.disabled = true;
                    this.mobileRunBtn.disabled = false;
                    this.mobileStopBtn.disabled = true;
                    this.statusDot.classList.remove('executing');
                    this.statusText.textContent = this.isConnected ? 'Ready' : 'Disconnected';
                }
            }

            updateProgress() {
                if (this.totalLines > 0) {
                    const progress = (this.currentLine / this.totalLines) * 100;
                    this.progressFill.style.width = `${progress}%`;
                    this.executionInfo.textContent = `Line ${this.currentLine} of ${this.totalLines}`;
                }
            }

            runCode() {
                if (!this.isConnected) {
                    this.addOutput('Not connected to server!', 'error');
                    return;
                }

                const code = this.codeEditor.value.trim();
                if (!code) {
                    this.addOutput('No code to execute!', 'warning');
                    return;
                }

                this.clearHighlights();
                this.socket.emit('execute_code', { code });
            }

            stopExecution() {
                this.socket.emit('stop_execution');
            }

            pauseExecution() {
                if (this.pauseBtn.innerHTML.includes('Pause')) {
                    this.socket.emit('pause_execution');
                    this.pauseBtn.innerHTML = '<i class="fas fa-play"></i><span class="btn-text">Resume</span>';
                } else {
                    this.socket.emit('resume_execution');
                    this.pauseBtn.innerHTML = '<i class="fas fa-pause"></i><span class="btn-text">Pause</span>';
                }
            }

            resetInterpreter() {
                this.socket.emit('reset_interpreter');
                this.clearHighlights();
            }

            executeCurrentLine() {
                if (!this.isConnected) {
                    this.addOutput('Not connected to server!', 'error');
                    return;
                }

                const lines = this.codeEditor.value.split('\n');
                const cursorPos = this.codeEditor.selectionStart;
                const textBeforeCursor = this.codeEditor.value.substring(0, cursorPos);
                const currentLineNumber = textBeforeCursor.split('\n').length - 1;
                const currentLine = lines[currentLineNumber];

                if (!currentLine || !currentLine.trim()) {
                    this.addOutput('No code on current line!', 'warning');
                    return;
                }

                this.socket.emit('execute_line', { line: currentLine });
            }

            clearOutput() {
                this.output.innerHTML = '';
            }

            addOutput(text, type = 'normal') {
                const line = document.createElement('div');
                line.className = `output-line ${type}`;
                
                // Add timestamp
                const timestamp = new Date().toLocaleTimeString();
                line.innerHTML = `<span style="color: #64748b; font-size: 0.8em;">[${timestamp}]</span> ${this.escapeHtml(text)}`;
                
                this.output.appendChild(line);
                this.output.scrollTop = this.output.scrollHeight;
            }

            escapeHtml(text) {
                const div = document.createElement('div');
                div.textContent = text;
                return div.innerHTML;
            }

            showInputPanel(prompt) {
                this.inputPrompt.textContent = prompt || 'Input:';
                this.inputPanel.classList.add('active');
                this.inputField.focus();
                this.inputField.value = '';
            }

            hideInputPanel() {
                this.inputPanel.classList.remove('active');
            }

            submitInput() {
                const input = this.inputField.value;
                this.socket.emit('provide_input', { input });
            }

            updateLineNumbers() {
                const lines = this.codeEditor.value.split('\n');
                const lineCount = lines.length;
                
                // Clear existing content
                this.lineNumbers.innerHTML = '';
                
                // Create line numbers as separate divs for perfect alignment
                for (let i = 1; i <= lineCount; i++) {
                    const lineDiv = document.createElement('div');
                    lineDiv.textContent = i;
                    lineDiv.style.height = '1.5rem'; // Match line-height
                    lineDiv.style.lineHeight = '1.5rem';
                    this.lineNumbers.appendChild(lineDiv);
                }
                
                // Ensure line numbers container matches editor height
                const editorHeight = this.codeEditor.scrollHeight;
                this.lineNumbers.style.minHeight = editorHeight + 'px';
            }

            syncLineNumbers() {
                this.lineNumbers.scrollTop = this.codeEditor.scrollTop;
            }

            insertTab() {
                const start = this.codeEditor.selectionStart;
                const end = this.codeEditor.selectionEnd;
                const value = this.codeEditor.value;
                
                this.codeEditor.value = value.substring(0, start) + '    ' + value.substring(end);
                this.codeEditor.selectionStart = this.codeEditor.selectionEnd = start + 4;
                this.updateLineNumbers();
            }

            highlightCurrentLine(lineNumber) {
                this.clearHighlights();
                const lines = this.codeEditor.value.split('\n');
                
                // Visual feedback in editor would require more complex implementation
                // For now, we'll just show it in the output
                this.executionInfo.textContent = `Executing line ${lineNumber}: ${lines[lineNumber - 1]?.trim() || ''}`;
            }

            highlightErrorLine(lineNumber) {
                // Similar to highlightCurrentLine, visual feedback would need more implementation
                this.addOutput(`Error on line ${lineNumber}`, 'error');
            }

            clearHighlights() {
                this.executionInfo.textContent = '';
                this.progressFill.style.width = '0%';
            }

            openFile(e) {
                const file = e.target.files[0];
                if (!file) return;
                
                const reader = new FileReader();
                reader.onload = (ev) => {
                    this.codeEditor.value = ev.target.result;
                    this.updateLineNumbers();
                    this.addOutput(`Loaded file: ${file.name}`, 'info');
                };
                reader.onerror = () => {
                    this.addOutput(`Failed to load file: ${file.name}`, 'error');
                };
                reader.readAsText(file);
                
                // Reset file input
                e.target.value = '';
            }

            saveFile() {
                const code = this.codeEditor.value;
                const blob = new Blob([code], { type: 'text/plain' });
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'code.noobie';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);
                
                this.addOutput('File saved: code.noobie', 'info');
            }
        }

        // Initialize the IDE when the page loads
        document.addEventListener('DOMContentLoaded', () => {
            const ide = new NoobieWebIDE();
            
            // Add some sample code for demonstration
            const sampleCode = `# Welcome to Noobie Web IDE!
# A beginner-friendly programming environment

# Let's start with a simple program
SAY "Hello, World!" end

# Create a variable
CREATE INT age 0

# Get user input
LISTEN INT age "Enter your age: "

# Make a decision
IF @age >= 18 DO
    SAY "You are an adult!" end
ELSE
    SAY "You are a minor!" end
ENDO

# Say goodbye
SAY "Thanks for using Noobie!" end`;

            if (!ide.codeEditor.value.trim()) {
                ide.codeEditor.value = sampleCode;
                ide.updateLineNumbers();
            }
            
            // Handle responsive button text
            const updateButtonText = () => {
                const width = window.innerWidth;
                const showText = width > 480;
                
                document.querySelectorAll('.btn-text').forEach(span => {
                    span.style.display = showText ? 'inline' : 'none';
                });
            };
            
            updateButtonText();
            window.addEventListener('resize', updateButtonText);
        });
    </script>
</body>
</html>
