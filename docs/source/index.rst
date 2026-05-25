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

    <!-- 引入 marked.js 解析 Markdown -->
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <!-- 引入 MathJax 3 并配置 -->
    <script>
    window.MathJax = {
        tex: {
            inlineMath: [['$', '$'], ['\\(', '\\)']],
            displayMath: [['$$', '$$'], ['\\[', '\\]']],
            processEscapes: true
        },
        options: {
            skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre']
        },
        startup: {
            pageReady: () => {
                return MathJax.startup.defaultPageReady();
            }
        }
    };
    </script>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" id="MathJax-script" async></script>
    
    <!-- 引入 highlight.js 代码高亮 -->
    <script src="https://cdn.jsdelivr.net/npm/highlight.js/lib/core.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/highlight.js/lib/languages/python.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/highlight.js/lib/languages/javascript.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/highlight.js/lib/languages/cpp.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/highlight.js/lib/languages/bash.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/highlight.js/styles/github-dark.css">

    <style>
    /* 基础容器样式 - 桌面端右下角 */
    .dr-chat-container {
        position: fixed !important;
        bottom: 20px !important;
        right: 20px !important;
        width: 400px !important;
        max-width: 90vw !important;
        background: white !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2) !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
        z-index: 9999 !important;
        display: flex !important;
        flex-direction: column !important;
        font-size: 14px !important;
        line-height: 1.6 !important;
    }
    
    /* 移动端适配 */
    @media (max-width: 768px) {
        .dr-chat-container.dr-collapsed {
            width: auto !important;
            max-width: none !important;
            min-width: 160px !important;
            bottom: 20px !important;
            left: 50% !important;
            right: auto !important;
            top: auto !important;
            transform: translateX(-50%) !important;
            border-radius: 12px !important;
        }
        .dr-chat-container:not(.dr-collapsed) {
            width: 100vw !important;
            max-width: 100vw !important;
            height: 80vh !important;
            bottom: 0 !important;
            left: 0 !important;
            right: 0 !important;
            top: auto !important;
            transform: none !important;
            border-radius: 12px 12px 0 0 !important;
        }
        .dr-chat-container:not(.dr-collapsed) .dr-chat-body {
            height: calc(80vh - 52px) !important;
        }
        .dr-chat-container.dr-collapsed .dr-chat-body {
            display: none !important;
        }
    }
    
    .dr-chat-header {
        background: #1a1a2e !important;
        color: white !important;
        padding: 12px 16px !important;
        border-radius: 12px 12px 0 0 !important;
        font-weight: bold !important;
        cursor: pointer !important;
        display: flex !important;
        justify-content: space-between !important;
        user-select: none !important;
        white-space: nowrap !important;
    }
    
    .dr-chat-container.dr-collapsed .dr-chat-header {
        border-radius: 12px !important;
    }
    
    .dr-chat-container:not(.dr-collapsed) .dr-chat-header {
        border-radius: 12px 12px 0 0 !important;
    }
    
    .dr-chat-body {
        display: flex !important;
        flex-direction: column !important;
        height: 480px !important;
    }
    
    .dr-chat-messages {
        flex: 1 !important;
        overflow-y: auto !important;
        padding: 16px !important;
        background: #fafafa !important;
        font-size: 14px !important;
        line-height: 1.6 !important;
    }
    
    .dr-message {
        margin-bottom: 16px !important;
        padding: 10px 14px !important;
        border-radius: 12px !important;
        max-width: 85% !important;
        word-wrap: break-word !important;
        font-size: 14px !important;
        line-height: 1.6 !important;
    }
    
    .dr-message p {
        margin: 0 0 8px 0 !important;
    }
    .dr-message p:last-child {
        margin-bottom: 0 !important;
    }
    .dr-message ul, .dr-message ol {
        margin: 8px 0 !important;
        padding-left: 20px !important;
    }
    .dr-message li {
        margin: 4px 0 !important;
    }
    
    /* 代码块样式 */
    .dr-message pre {
        background: #0d1117 !important;
        border-radius: 8px !important;
        padding: 12px !important;
        overflow-x: auto !important;
        margin: 8px 0 !important;
    }
    .dr-message code {
        font-family: 'SF Mono', Monaco, 'Cascadia Code', monospace !important;
        font-size: 13px !important;
    }
    .dr-message :not(pre) > code {
        background: #e8e8ec !important;
        padding: 2px 6px !important;
        border-radius: 4px !important;
        color: #d73a49 !important;
    }
    
    /* 公式样式 */
    .dr-message mjx-container {
        margin: 8px 0 !important;
        overflow-x: auto !important;
    }
    
    .dr-user {
        background: #1a1a2e !important;
        color: white !important;
        margin-left: auto !important;
        text-align: right !important;
        border-bottom-right-radius: 4px !important;
    }
    .dr-bot {
        background: #e8e8ec !important;
        color: #1a1a2e !important;
        margin-right: auto !important;
        border-bottom-left-radius: 4px !important;
    }
    .dr-loading {
        color: #888 !important;
        font-style: italic !important;
        padding: 10px 14px !important;
        margin-bottom: 16px !important;
        font-size: 13px !important;
    }
    .dr-chat-input-area {
        display: flex !important;
        padding: 12px 16px !important;
        gap: 10px !important;
        border-top: 1px solid #e0e0e0 !important;
        background: white !important;
        border-radius: 0 0 12px 12px !important;
    }
    
    .dr-chat-input-area .dr-chat-input,
    #dr-chat-input.dr-chat-input {
        flex: 1 !important;
        padding: 12px 16px !important;
        border: 1px solid #ccc !important;
        border-radius: 28px !important;
        outline: none !important;
        font-size: 15px !important;
        font-family: inherit !important;
        line-height: 1.4 !important;
        background: white !important;
        box-sizing: border-box !important;
        min-height: 44px !important;
    }
    
    .dr-chat-input-area .dr-chat-input:focus,
    #dr-chat-input.dr-chat-input:focus {
        border-color: #1a1a2e !important;
        box-shadow: 0 0 0 2px rgba(26, 26, 46, 0.2) !important;
    }
    
    .dr-chat-input-area .dr-chat-send,
    #dr-chat-send.dr-chat-send {
        background: #1a1a2e !important;
        color: white !important;
        border: none !important;
        border-radius: 28px !important;
        padding: 0 22px !important;
        cursor: pointer !important;
        font-size: 14px !important;
        font-weight: 500 !important;
        font-family: inherit !important;
        min-height: 44px !important;
        transition: background 0.2s !important;
    }
    
    .dr-chat-input-area .dr-chat-send:hover {
        background: #2a2a3e !important;
    }
    .dr-chat-input-area .dr-chat-send:active {
        transform: scale(0.97) !important;
    }
    .dr-collapsed .dr-chat-body {
        display: none !important;
    }
    .dr-arrow {
        transition: transform 0.2s ease !important;
        display: inline-block !important;
    }
    .dr-collapsed .dr-arrow {
        transform: rotate(180deg) !important;
    }
    
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
    </style>

    <div id="dr-chat-widget" class="dr-chat-container dr-collapsed">
        <div class="dr-chat-header">
            <span>🤖 DrestryRobot 智能助手</span>
            <span class="dr-arrow">▼</span>
        </div>
        <div class="dr-chat-body">
            <div class="dr-chat-messages" id="dr-chat-messages">
                <div class="dr-message dr-bot">你好，我是 DrestryRobot 助手。请提出机器人相关问题。</div>
            </div>
            <div class="dr-chat-input-area">
                <input type="text" class="dr-chat-input" id="dr-chat-input" placeholder="输入机器人相关问题...">
                <button class="dr-chat-send" id="dr-chat-send">发送</button>
            </div>
        </div>
    </div>

    <script>
    (function() {
        const DEEPSEEK_KEY = 'sk-c09347c4e827479a842a21acf5771103';
        
        if (window.__drestryrobotChatLoaded) return;
        window.__drestryrobotChatLoaded = true;
        
        const container = document.getElementById('dr-chat-widget');
        const header = container.querySelector('.dr-chat-header');
        const messagesDiv = document.getElementById('dr-chat-messages');
        const input = document.getElementById('dr-chat-input');
        const sendBtn = document.getElementById('dr-chat-send');
        
        let isLoading = false;
        let currentStreamingDiv = null;
        let streamingContent = '';
        
        header.addEventListener('click', () => {
            container.classList.toggle('dr-collapsed');
        });
        
        // 配置 marked
        marked.setOptions({
            highlight: function(code, lang) {
                if (lang && hljs.getLanguage(lang)) {
                    try {
                        return hljs.highlight(code, { language: lang }).value;
                    } catch (e) {}
                }
                return code;
            }
        });
        
        // 将 Markdown 转换为 HTML，不转义公式
        function markdownToHtml(text) {
            if (!text) return '';
            
            // ========== 修复 DeepSeek 的 FORMULA_X 占位符 ==========
            // 定义常用公式映射表
            const formulaMap = {
                0: '$$e(t) = r(t) - y(t)$$',
                1: '$$u(t) = K_p e(t) + K_i \\int_0^t e(\\tau) d\\tau + K_d \\frac{de(t)}{dt}$$',
                2: '$$\\tau = K_p (\\theta_d - \\theta) + K_d (\\dot{\\theta}_d - \\dot{\\theta})$$',
                3: '$$\\mathbf{F} = K_p \\mathbf{e}_p + K_i \\int \\mathbf{e}_p dt + K_d \\dot{\\mathbf{e}}_p$$',
                4: '$$\\frac{K_d s}{\\tau_f s + 1}$$',
                5: '$$r(t)$$',
                6: '$$y(t)$$',
                7: '$$u(t)$$',
                8: '$$K_p$$',
                9: '$$K_i$$',
                10: '$$K_d$$',
                11: '$$K_p e(t)$$',
                12: '$$K_i \\int e(t) dt$$',
                13: '$$K_d \\frac{de(t)}{dt}$$',
                14: '$$\\theta_d$$',
                15: '$$\\theta$$',
                16: '$$\\tau$$',
                17: '$$\\mathbf{e}_p$$',
                18: '$$\\mathbf{F}$$',
                19: '$$K_u$$',
                20: '$$T_u$$'
            };
            
            // 替换所有 FORMULA_X 占位符
            text = text.replace(/FORMULA_(\d+)/g, (match, num) => {
                const idx = parseInt(num, 10);
                return formulaMap[idx] || `$$\\text{Formula}_{${idx}}$$`;
            });
            // ========== 修复结束 ==========
            
            // 保护公式不被 marked 破坏
            const formulas = [];
            
            // 保护块级公式 $$...$$
            let processed = text.replace(/\$\$([\s\S]*?)\$\$/g, (match, formula) => {
                const idx = formulas.length;
                formulas.push({ type: 'display', content: formula });
                return `__FORMULA_${idx}__`;
            });
            
            // 保护行内公式 $...$
            processed = processed.replace(/\$([^\$\n]+?)\$/g, (match, formula) => {
                const idx = formulas.length;
                formulas.push({ type: 'inline', content: formula });
                return `__FORMULA_${idx}__`;
            });
            
            // 解析 Markdown
            let html = marked.parse(processed, { mangle: false, headerIds: false });
            
            // 恢复公式
            formulas.forEach((formula, idx) => {
                const placeholder = `__FORMULA_${idx}__`;
                if (formula.type === 'display') {
                    html = html.replace(placeholder, `$$${formula.content}$$`);
                } else {
                    html = html.replace(placeholder, `$${formula.content}$`);
                }
            });
            
            return html;
        }
        
        // 强制渲染公式
        function renderMath(element) {
            if (window.MathJax && element) {
                MathJax.typesetPromise([element]).catch(err => console.warn('MathJax error:', err));
            }
        }
        
        function addStreamingMessage() {
            currentStreamingDiv = document.createElement('div');
            currentStreamingDiv.className = 'dr-message dr-bot';
            currentStreamingDiv.innerHTML = '<span class="dr-typing-cursor"></span>';
            messagesDiv.appendChild(currentStreamingDiv);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
            streamingContent = '';
        }
        
        function updateStreamingContent(newChunk) {
            if (!currentStreamingDiv) return;
            streamingContent += newChunk;
            let rendered = markdownToHtml(streamingContent);
            currentStreamingDiv.innerHTML = rendered + '<span class="dr-typing-cursor"></span>';
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
            // 实时渲染公式
            if (window.MathJax && currentStreamingDiv) {
                MathJax.typesetPromise([currentStreamingDiv]).catch(err => console.warn('MathJax error:', err));
            }
        }
        
        function finishStreamingMessage() {
            if (!currentStreamingDiv) return;
            let rendered = markdownToHtml(streamingContent);
            currentStreamingDiv.innerHTML = rendered;
            // 渲染公式
            if (window.MathJax) {
                MathJax.typesetPromise([currentStreamingDiv]).catch(err => console.warn('MathJax error:', err));
            }
            // 代码高亮
            if (typeof hljs !== 'undefined') {
                currentStreamingDiv.querySelectorAll('pre code').forEach((block) => {
                    hljs.highlightElement(block);
                });
            }
            currentStreamingDiv = null;
            streamingContent = '';
        }
        
        function addMessage(role, content) {
            const div = document.createElement('div');
            div.className = `dr-message dr-${role}`;
            
            if (role === 'user') {
                div.textContent = content;
            } else {
                div.innerHTML = markdownToHtml(content);
                // 渲染公式
                renderMath(div);
                // 代码高亮
                if (typeof hljs !== 'undefined') {
                    div.querySelectorAll('pre code').forEach((block) => {
                        hljs.highlightElement(block);
                    });
                }
            }
            
            messagesDiv.appendChild(div);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        }
        
        async function sendMessage() {
            const message = input.value.trim();
            if (!message || isLoading) return;
            
            addMessage('user', message);
            input.value = '';
            
            isLoading = true;
            addStreamingMessage();
            
            try {
                const response = await fetch('https://api.deepseek.com/v1/chat/completions', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${DEEPSEEK_KEY}`
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
                
                const reader = response.body.getReader();
                const decoder = new TextDecoder();
                let buffer = '';
                
                while (true) {
                    const { done, value } = await reader.read();
                    if (done) break;
                    
                    buffer += decoder.decode(value, { stream: true });
                    const lines = buffer.split('\n');
                    buffer = lines.pop() || '';
                    
                    for (const line of lines) {
                        if (line.startsWith('data: ')) {
                            const data = line.slice(6);
                            if (data === '[DONE]') continue;
                            try {
                                const parsed = JSON.parse(data);
                                const chunk = parsed.choices[0]?.delta?.content || '';
                                if (chunk) {
                                    updateStreamingContent(chunk);
                                }
                            } catch (e) {}
                        }
                    }
                }
                
                finishStreamingMessage();
                
            } catch (error) {
                if (currentStreamingDiv) {
                    currentStreamingDiv.remove();
                    currentStreamingDiv = null;
                }
                addMessage('bot', `调用失败：${error.message}`);
            }
            isLoading = false;
        }
        
        sendBtn.addEventListener('click', sendMessage);
        input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                sendMessage();
            }
        });
    })();
    </script>