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
    <!-- 引入 MathJax 渲染公式 -->
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>

    <style>
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
    /* 输入框样式 - 加强优先级 */
    .dr-chat-input-area .dr-chat-input,
    div.dr-chat-input-area input.dr-chat-input,
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
        height: auto !important;
        min-height: 44px !important;
    }
    .dr-chat-input-area .dr-chat-input:focus,
    #dr-chat-input.dr-chat-input:focus {
        border-color: #1a1a2e !important;
        box-shadow: 0 0 0 2px rgba(26, 26, 46, 0.2) !important;
    }
    .dr-chat-input-area .dr-chat-input::placeholder {
        color: #aaa !important;
        font-size: 14px !important;
    }
    /* 发送按钮样式 */
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
    mjx-container {
        overflow-x: auto !important;
        overflow-y: hidden !important;
        margin: 8px 0 !important;
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
        
        header.addEventListener('click', () => {
            container.classList.toggle('dr-collapsed');
        });
        
        function markdownToHtml(text) {
            if (!text) return '';
            
            const latexBlocks = [];
            const latexInlines = [];
            
            text = text.replace(/\$\$([\s\S]*?)\$\$/g, (match, formula) => {
                const idx = latexBlocks.length;
                latexBlocks.push(formula);
                return `@@LATEX_BLOCK_${idx}@@`;
            });
            
            text = text.replace(/\$([^\$\n]+?)\$/g, (match, formula) => {
                const idx = latexInlines.length;
                latexInlines.push(formula);
                return `@@LATEX_INLINE_${idx}@@`;
            });
            
            let html = marked.parse(text, { mangle: false, headerIds: false });
            
            html = html.replace(/@@LATEX_BLOCK_(\d+)@@/g, (match, idx) => {
                return `$$${latexBlocks[parseInt(idx)]}$$`;
            });
            
            html = html.replace(/@@LATEX_INLINE_(\d+)@@/g, (match, idx) => {
                return `$${latexInlines[parseInt(idx)]}$`;
            });
            
            return html;
        }
        
        function addMessage(role, content) {
            const div = document.createElement('div');
            div.className = `dr-message dr-${role}`;
            
            if (role === 'user') {
                div.textContent = content;
            } else {
                div.innerHTML = markdownToHtml(content);
            }
            
            messagesDiv.appendChild(div);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
            
            if (role === 'bot' && window.MathJax) {
                MathJax.typesetPromise([div]).catch(err => console.warn('MathJax error:', err));
            }
        }
        
        async function sendMessage() {
            const message = input.value.trim();
            if (!message || isLoading) return;
            
            addMessage('user', message);
            input.value = '';
            
            const loadingDiv = document.createElement('div');
            loadingDiv.className = 'dr-loading';
            loadingDiv.textContent = '思考中...';
            messagesDiv.appendChild(loadingDiv);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
            isLoading = true;
            
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
                                content: '你是 DrestryRobot 知识库的机器人专家。回答应严谨、深刻、偏重机器人学理论（运动学/动力学/控制/感知）。使用 Markdown 格式组织回答：用 ## 表示小标题，用 - 表示列表，用 $...$ 或 $$...$$ 表示公式。段落之间用空行分隔。'
                            },
                            { role: 'user', content: message }
                        ],
                        temperature: 0.3
                    })
                });
                
                const data = await response.json();
                const reply = data.choices[0].message.content;
                loadingDiv.remove();
                addMessage('bot', reply);
            } catch (error) {
                loadingDiv.remove();
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