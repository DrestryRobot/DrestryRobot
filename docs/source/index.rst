DrestryRobot
==============

基本介绍
-------------
DrestryRobot是一个机器人开发知识库，其涵盖了机器人开发所需要用到的各类技术知识和软件工具。

核心理念
-------------
DrestryRobot由Dream、Struggle、Youth和Robot组成，是一个热爱于机器人开发、有梦想、敢奋斗、充满青春活力的团队。

编撰原则
-------------
不用图片，不用链接，不用资源。

应该是有深度的内容，不重复造轮子。

一针见血，应该是总结。

写比看重要。

围绕机器人的。

应该也不用代码，但是应该会用公式。

一般人看不懂的。

一知半解的不写。

.. toctree::
   :maxdepth: 2
   :caption: 内容目录
   :glob:

   *

.. raw:: html

    <div id="dr-chat-container" style="position: fixed; bottom: 20px; right: 20px; z-index: 9999;"></div>

    <style>
        /* 防止 iOS 输入框焦点时缩放 */
        @media (max-width: 768px) {
            input, textarea, button {
                font-size: 16px !important;
            }
            body {
                touch-action: pan-y pinch-zoom;
            }
        }
        
        /* 主容器 - 默认桌面端样式 */
        .dr-chat-widget {
            position: fixed !important;
            bottom: 20px !important;
            right: 20px !important;
            width: 400px !important;
            max-width: 90vw !important;
            background: white !important;
            border-radius: 16px !important;
            box-shadow: 0 4px 24px rgba(0,0,0,0.15) !important;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
            z-index: 9999 !important;
            display: flex !important;
            flex-direction: column !important;
            transition: all 0.3s ease !important;
            overflow: hidden !important;
        }
        
        /* 桌面端折叠状态 - 保持相同宽度，所有角都有圆角 */
        .dr-chat-widget.dr-collapsed {
            width: 400px !important;
            max-width: 90vw !important;
            min-width: auto !important;
            border-radius: 16px !important;
        }
        .dr-chat-widget.dr-collapsed .dr-chat-header {
            border-radius: 16px !important;
        }
        .dr-chat-widget.dr-collapsed .dr-chat-body {
            display: none !important;
        }
        
        /* 桌面端展开状态 - 只有顶部圆角 */
        .dr-chat-widget:not(.dr-collapsed) {
            border-radius: 16px 16px 0 0 !important;
        }
        .dr-chat-widget:not(.dr-collapsed) .dr-chat-header {
            border-radius: 16px 16px 0 0 !important;
        }
        
        /* 移动端适配 */
        @media (max-width: 768px) {
            /* 移动端折叠状态 - 右下角小图标 */
            .dr-chat-widget.dr-collapsed {
                position: fixed !important;
                bottom: 20px !important;
                right: 20px !important;
                left: auto !important;
                transform: none !important;
                width: auto !important;
                min-width: auto !important;
                max-width: none !important;
                border-radius: 40px !important;
                background: #1a1a2e !important;
                box-shadow: 0 2px 12px rgba(0,0,0,0.2) !important;
            }
            .dr-chat-widget.dr-collapsed .dr-chat-header {
                border-radius: 40px !important;
                padding: 10px 18px !important;
                background: #1a1a2e !important;
            }
            .dr-chat-widget.dr-collapsed .dr-header-left span:first-child {
                font-size: 14px;
            }
            
            /* 移动端展开状态 - 全屏，禁止页面滚动 */
            .dr-chat-widget:not(.dr-collapsed) {
                position: fixed !important;
                top: 0 !important;
                left: 0 !important;
                right: 0 !important;
                bottom: 0 !important;
                width: 100% !important;
                max-width: 100% !important;
                height: 100% !important;
                border-radius: 0 !important;
                margin: 0 !important;
                transform: none !important;
                background: white !important;
            }
            .dr-chat-widget:not(.dr-collapsed) .dr-chat-header {
                border-radius: 0 !important;
                padding: 14px 16px !important;
            }
            .dr-chat-widget:not(.dr-collapsed) .dr-chat-body {
                height: calc(100% - 52px) !important;
                display: flex !important;
            }
            
            /* 展开时禁止页面滚动 */
            body.dr-chat-open {
                overflow: hidden !important;
                position: fixed !important;
                width: 100% !important;
                height: 100% !important;
            }
        }
        
        @media (min-width: 769px) {
            .dr-chat-widget.dr-collapsed .dr-chat-header:hover {
                background: #2a2a3e !important;
            }
        }
        
        /* 头部 */
        .dr-chat-header {
            background: #1a1a2e !important;
            color: white !important;
            padding: 12px 16px !important;
            font-weight: 600 !important;
            cursor: pointer !important;
            display: flex !important;
            justify-content: space-between !important;
            align-items: center !important;
            user-select: none !important;
            transition: background 0.2s ease !important;
        }
        
        .dr-header-left {
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }
        
        .dr-header-right {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        /* 箭头 */
        .dr-arrow {
            transition: transform 0.3s ease;
            font-size: 12px;
            display: inline-block;
        }
        .dr-collapsed .dr-arrow {
            transform: rotate(180deg);
        }
        
        /* 主体 */
        .dr-chat-body {
            display: flex !important;
            flex-direction: column !important;
            height: 500px !important;
            background: #f5f5f5;
            position: relative;
        }
        
        /* 消息区域 */
        .dr-chat-messages {
            flex: 1 !important;
            overflow-y: auto !important;
            padding: 16px !important;
            background: #fafafa !important;
            overflow-x: hidden !important;
            -webkit-overflow-scrolling: touch;
        }
        
        .dr-chat-messages:after {
            content: "";
            display: table;
            clear: both;
        }
        
        /* 底部提示文字 */
        .dr-footer-tip {
            text-align: center;
            font-size: 10px;
            color: #999;
            padding: 6px 12px;
            background: #f5f5f5;
            border-top: 1px solid #e8e8e8;
        }
        
        /* 消息气泡通用样式 */
        .dr-message {
            margin-bottom: 12px !important;
            padding: 10px 14px !important;
            border-radius: 12px !important;
            max-width: 85% !important;
            word-wrap: break-word !important;
            display: inline-block !important;
            font-size: 14px !important;
            line-height: 1.5 !important;
            text-align: justify !important;
        }
        
        /* 用户消息 */
        .dr-user {
            background: #1a1a2e !important;
            color: white !important;
            border-bottom-right-radius: 4px !important;
            float: right !important;
            clear: both !important;
        }
        
        /* 机器人消息 */
        .dr-bot {
            background: #e8e8ec !important;
            color: #1a1a2e !important;
            border-bottom-left-radius: 4px !important;
            float: left !important;
            clear: both !important;
        }
        
        /* 标题保持大字号 */
        .dr-message h1 {
            font-size: 1.6em !important;
            font-weight: 600 !important;
            margin: 8px 0 6px 0 !important;
            text-align: left !important;
        }
        .dr-message h2 {
            font-size: 1.4em !important;
            font-weight: 600 !important;
            margin: 8px 0 6px 0 !important;
            text-align: left !important;
        }
        .dr-message h3 {
            font-size: 1.25em !important;
            font-weight: 600 !important;
            margin: 8px 0 6px 0 !important;
            text-align: left !important;
        }
        .dr-message h4, .dr-message h5, .dr-message h6 {
            font-size: 1.1em !important;
            font-weight: 600 !important;
            margin: 8px 0 6px 0 !important;
            text-align: left !important;
        }
        
        /* 正文段落 */
        .dr-message p {
            margin: 0 0 6px 0;
            text-align: justify !important;
            font-size: 14px !important;
        }
        .dr-message p:last-child {
            margin-bottom: 0;
        }
        
        /* 列表 */
        .dr-message ul, .dr-message ol {
            margin: 6px 0;
            padding-left: 20px;
            text-align: left !important;
            font-size: 14px !important;
        }
        .dr-message li {
            text-align: left !important;
            font-size: 14px !important;
            margin: 2px 0;
        }
        
        /* 代码块 */
        .dr-message pre {
            background: #0d1117;
            color: #e6edf3;
            padding: 10px;
            border-radius: 8px;
            overflow-x: auto;
            margin: 8px 0;
            font-size: 13px !important;
        }
        .dr-message code {
            font-family: 'SF Mono', Monaco, 'Cascadia Code', monospace;
            font-size: 13px !important;
        }
        .dr-message :not(pre) > code {
            background: #e8e8ec;
            padding: 2px 6px;
            border-radius: 4px;
            color: #d73a49;
            font-size: 13px !important;
        }
        
        /* 引用块 */
        .dr-message blockquote {
            margin: 8px 0;
            padding-left: 12px;
            border-left: 3px solid #ccc;
            color: #666;
            font-size: 14px !important;
        }
        
        /* 表格 */
        .dr-message table {
            border-collapse: collapse;
            width: 100%;
            margin: 8px 0;
            font-size: 13px !important;
        }
        .dr-message th, .dr-message td {
            border: 1px solid #ddd;
            padding: 6px;
            text-align: left;
        }
        .dr-message th {
            background: #f0f0f0;
        }
        
        /* 输入区域 */
        .dr-chat-input-area {
            display: flex !important;
            padding: 12px 16px !important;
            gap: 10px !important;
            background: white !important;
            position: relative;
        }
        
        .dr-chat-input {
            flex: 1 !important;
            padding: 10px 16px !important;
            border: 1px solid #ddd !important;
            border-radius: 24px !important;
            outline: none !important;
            font-size: 14px !important;
            transition: border-color 0.2s;
            font-family: inherit;
        }
        
        .dr-chat-input:focus {
            border-color: #1a1a2e !important;
            box-shadow: 0 0 0 2px rgba(26,26,46,0.1);
        }
        
        .dr-chat-send {
            background: #1a1a2e !important;
            color: white !important;
            border: none !important;
            border-radius: 24px !important;
            padding: 0 20px !important;
            cursor: pointer !important;
            font-size: 14px !important;
            font-weight: 500 !important;
            transition: background 0.2s;
            white-space: nowrap;
            font-family: inherit;
        }
        
        .dr-chat-send:hover {
            background: #2a2a3e !important;
        }
        
        .dr-chat-send:disabled {
            background: #ccc !important;
            cursor: not-allowed;
        }
        
        /* 思考动画 */
        .dr-thinking {
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 4px 0;
        }
        .dr-thinking-dot {
            width: 8px;
            height: 8px;
            background-color: #1a1a2e;
            border-radius: 50%;
            animation: dr-bounce 1.4s infinite ease-in-out both;
        }
        .dr-thinking-dot:nth-child(1) { animation-delay: -0.32s; }
        .dr-thinking-dot:nth-child(2) { animation-delay: -0.16s; }
        @keyframes dr-bounce {
            0%, 80%, 100% { transform: scale(0); opacity: 0.5; }
            40% { transform: scale(1); opacity: 1; }
        }
        
        /* 打字光标 */
        .dr-typing-cursor {
            display: inline-block;
            width: 2px;
            height: 1.2em;
            background-color: #1a1a2e;
            margin-left: 2px;
            vertical-align: middle;
            animation: dr-blink 1s step-end infinite;
        }
        @keyframes dr-blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0; }
        }
        
        /* MathJax 公式 */
        mjx-container {
            overflow-x: auto !important;
            margin: 8px 0 !important;
        }
    </style>

    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>

.. raw:: html

    <div id="dr-chat-widget" class="dr-chat-widget dr-collapsed">
        <div class="dr-chat-header">
            <div class="dr-header-left">
                <span>🤖 DrestryRobot</span>
            </div>
            <div class="dr-header-right">
                <span class="dr-arrow">▼</span>
            </div>
        </div>
        <div class="dr-chat-body">
            <div class="dr-chat-messages" id="chatMessages">
                <div class="dr-message dr-bot">
                    🤖 欢迎使用 DrestryRobot 专业助手！<br><br>
                    机器人学相关问题，随时向我提问～
                </div>
            </div>
            <div class="dr-footer-tip" id="footerTip">
                ✨ 内容由 DeepSeek 生成，仅供参考
            </div>
            <div class="dr-chat-input-area" id="inputArea">
                <input type="text" class="dr-chat-input" id="chatInput" placeholder="输入机器人相关问题...">
                <button class="dr-chat-send" id="sendBtn">发送</button>
            </div>
        </div>
    </div>

    <script>
    (function() {
        // ========== 配置 ==========
        var DEEPSEEK_KEY = 'sk-c09347c4e827479a842a21acf5771103';
        
        // 移动端展开时禁止页面滚动
        function toggleBodyScroll(disable) {
            if (window.innerWidth > 768) return;
            if (disable) {
                document.body.classList.add('dr-chat-open');
            } else {
                document.body.classList.remove('dr-chat-open');
            }
        }
        
        function mdToHtml(text) {
            if (!text) return '';
            var latexBlocks = [], latexInlines = [];
            text = text.replace(/\$\$([\s\S]*?)\$\$/g, function(match, formula) {
                var idx = latexBlocks.length;
                latexBlocks.push(formula);
                return '@@LB_' + idx + '@@';
            });
            text = text.replace(/\$([^\$\n]+?)\$/g, function(match, formula) {
                var idx = latexInlines.length;
                latexInlines.push(formula);
                return '@@LI_' + idx + '@@';
            });
            var html = marked.parse(text, { mangle: false, headerIds: false });
            html = html.replace(/@@LB_(\d+)@@/g, function(match, idx) {
                return '$$' + latexBlocks[parseInt(idx)] + '$$';
            });
            html = html.replace(/@@LI_(\d+)@@/g, function(match, idx) {
                return '$' + latexInlines[parseInt(idx)] + '$';
            });
            return html;
        }
        
        // ========== 聊天功能 ==========
        var isLoading = false;
        var currentStreamingDiv = null;
        var streamingContent = '';
        var autoScrollEnabled = true;
        
        function bindScrollEvent() {
            var msgsDiv = document.getElementById('chatMessages');
            if (!msgsDiv) return;
            msgsDiv.addEventListener('scroll', function() {
                var isAtBottom = msgsDiv.scrollHeight - msgsDiv.scrollTop - msgsDiv.clientHeight < 50;
                autoScrollEnabled = isAtBottom;
            });
        }
        
        function scrollToBottom() {
            if (!autoScrollEnabled) return;
            var msgsDiv = document.getElementById('chatMessages');
            if (msgsDiv) {
                msgsDiv.scrollTop = msgsDiv.scrollHeight;
            }
        }
        
        function addMessage(role, content, isHtml) {
            var msgs = document.getElementById('chatMessages');
            var div = document.createElement('div');
            div.className = 'dr-message dr-' + role;
            if (role === 'user') {
                div.textContent = content;
            } else {
                div.innerHTML = isHtml ? content : mdToHtml(content);
            }
            msgs.appendChild(div);
            scrollToBottom();
            if (role === 'bot' && window.MathJax) {
                MathJax.typesetPromise([div]).catch(function(e) {});
            }
            return div;
        }
        
        function showThinking() {
            var msgs = document.getElementById('chatMessages');
            var thinkingDiv = document.createElement('div');
            thinkingDiv.className = 'dr-message dr-bot';
            thinkingDiv.id = 'thinkingIndicator';
            thinkingDiv.innerHTML = '<div class="dr-thinking"><span class="dr-thinking-dot"></span><span class="dr-thinking-dot"></span><span class="dr-thinking-dot"></span><span style="margin-left:4px;">思考中...</span></div>';
            msgs.appendChild(thinkingDiv);
            scrollToBottom();
        }
        
        function hideThinking() {
            var thinking = document.getElementById('thinkingIndicator');
            if (thinking) thinking.remove();
        }
        
        function startStreaming() {
            currentStreamingDiv = document.createElement('div');
            currentStreamingDiv.className = 'dr-message dr-bot';
            currentStreamingDiv.innerHTML = '<span class="dr-typing-cursor"></span>';
            document.getElementById('chatMessages').appendChild(currentStreamingDiv);
            streamingContent = '';
            scrollToBottom();
        }
        
        function updateStreaming(chunk) {
            if (!currentStreamingDiv) return;
            streamingContent += chunk;
            var rendered = mdToHtml(streamingContent);
            currentStreamingDiv.innerHTML = rendered + '<span class="dr-typing-cursor"></span>';
            scrollToBottom();
        }
        
        function finishStreaming() {
            if (!currentStreamingDiv) return;
            var rendered = mdToHtml(streamingContent);
            currentStreamingDiv.innerHTML = rendered;
            if (window.MathJax) {
                MathJax.typesetPromise([currentStreamingDiv]).catch(function(e) {});
            }
            currentStreamingDiv = null;
            streamingContent = '';
            scrollToBottom();
        }
        
        async function sendMessage() {
            var input = document.getElementById('chatInput');
            var message = input.value.trim();
            if (!message || isLoading) return;
            
            addMessage('user', message);
            input.value = '';
            
            isLoading = true;
            autoScrollEnabled = true;
            showThinking();
            
            try {
                var response = await fetch('https://api.deepseek.com/v1/chat/completions', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': 'Bearer ' + DEEPSEEK_KEY
                    },
                    body: JSON.stringify({
                        model: 'deepseek-chat',
                        messages: [
                            { 
                                role: 'system', 
                                content: '你是 DrestryRobot 知识库的机器人专家。回答应严谨、深刻、偏重机器人学理论。使用 Markdown 格式：用 ## 标题，用 - 列表，用 $...$ 或 $$...$$ 公式。代码块用 ```language 标记。'
                            },
                            { role: 'user', content: message }
                        ],
                        temperature: 0.3,
                        stream: true
                    })
                });
                
                if (!response.ok) {
                    throw new Error('API请求失败: ' + response.status);
                }
                
                if (!response.body) {
                    throw new Error('响应不支持流式读取');
                }
                
                hideThinking();
                startStreaming();
                
                var reader = response.body.getReader();
                var decoder = new TextDecoder();
                var buffer = '';
                
                while (true) {
                    var result = await reader.read();
                    if (result.done) break;
                    buffer += decoder.decode(result.value, { stream: true });
                    var lines = buffer.split('\n');
                    buffer = lines.pop() || '';
                    for (var i = 0; i < lines.length; i++) {
                        var line = lines[i];
                        if (line.startsWith('data: ')) {
                            var data = line.slice(6);
                            if (data === '[DONE]') continue;
                            try {
                                var parsed = JSON.parse(data);
                                var chunk = parsed.choices && parsed.choices[0] && parsed.choices[0].delta && parsed.choices[0].delta.content;
                                if (chunk) updateStreaming(chunk);
                            } catch(e) {}
                        }
                    }
                }
                finishStreaming();
            } catch(error) {
                hideThinking();
                if (currentStreamingDiv) {
                    currentStreamingDiv.remove();
                    currentStreamingDiv = null;
                }
                addMessage('bot', '调用失败：' + error.message + '\n\n请检查网络后重试。');
            }
            isLoading = false;
        }
        
        function bindCollapseEvent() {
            var widget = document.getElementById('dr-chat-widget');
            var header = document.querySelector('.dr-chat-header');
            
            if (header) {
                header.addEventListener('click', function(e) {
                    e.stopPropagation();
                    var isExpanding = widget.classList.contains('dr-collapsed');
                    widget.classList.toggle('dr-collapsed');
                    if (window.innerWidth <= 768) {
                        toggleBodyScroll(!isExpanding);
                    }
                });
            }
        }
        
        function bindEvents() {
            var sendBtn = document.getElementById('sendBtn');
            var input = document.getElementById('chatInput');
            
            bindCollapseEvent();
            bindScrollEvent();
            
            if (sendBtn) {
                sendBtn.addEventListener('click', sendMessage);
            }
            
            if (input) {
                input.addEventListener('keypress', function(e) {
                    if (e.key === 'Enter') {
                        e.preventDefault();
                        sendMessage();
                    }
                });
            }
        }
        
        function init() {
            bindEvents();
            console.log('DrestryRobot 已启动');
        }
        
        init();
    })();
    </script>