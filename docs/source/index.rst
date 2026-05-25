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
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 400px;
        max-width: 90vw;
        background: white;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        z-index: 9999;
        display: flex;
        flex-direction: column;
        font-size: 14px;
        line-height: 1.6;
    }
    .dr-chat-header {
        background: #1a1a2e;
        color: white;
        padding: 12px 16px;
        border-radius: 12px 12px 0 0;
        font-weight: bold;
        cursor: pointer;
        display: flex;
        justify-content: space-between;
        user-select: none;
    }
    .dr-chat-body {
        display: flex;
        flex-direction: column;
        height: 480px;
    }
    .dr-chat-messages {
        flex: 1;
        overflow-y: auto;
        padding: 16px;
        background: #fafafa;
        font-size: 14px;
        line-height: 1.6;
    }
    .dr-message {
        margin-bottom: 16px;
        padding: 10px 14px;
        border-radius: 12px;
        max-width: 85%;
        word-wrap: break-word;
        font-size: 14px;
        line-height: 1.6;
    }
    .dr-message p {
        margin: 0 0 8px 0;
    }
    .dr-message p:last-child {
        margin-bottom: 0;
    }
    .dr-message ul, .dr-message ol {
        margin: 8px 0;
        padding-left: 20px;
    }
    .dr-message li {
        margin: 4px 0;
    }
    .dr-user {
        background: #1a1a2e;
        color: white;
        margin-left: auto;
        text-align: right;
        border-bottom-right-radius: 4px;
    }
    .dr-bot {
        background: #e8e8ec;
        color: #1a1a2e;
        margin-right: auto;
        border-bottom-left-radius: 4px;
    }
    .dr-loading {
        color: #888;
        font-style: italic;
        padding: 10px 14px;
        margin-bottom: 16px;
        font-size: 13px;
    }
    .dr-chat-input-area {
        display: flex;
        padding: 12px 16px;
        gap: 10px;
        border-top: 1px solid #e0e0e0;
        background: white;
        border-radius: 0 0 12px 12px;
    }
    .dr-chat-input {
        flex: 1;
        padding: 12px 16px;
        border: 1px solid #d0d0d0;
        border-radius: 28px;
        outline: none;
        font-size: 15px;
        font-family: inherit;
        line-height: 1.4;
        transition: border-color 0.2s, box-shadow 0.2s;
        background: #fefefe;
    }
    .dr-chat-input:focus {
        border-color: #1a1a2e;
        box-shadow: 0 0 0 3px rgba(26, 26, 46, 0.1);
    }
    .dr-chat-input::placeholder {
        color: #aaa;
        font-size: 14px;
    }
    .dr-chat-send {
        background: #1a1a2e;
        color: white;
        border: none;
        border-radius: 28px;
        padding: 0 22px;
        cursor: pointer;
        font-size: 14px;
        font-weight: 500;
        font-family: inherit;
        transition: background 0.2s, transform 0.1s;
    }
    .dr-chat-send:hover {
        background: #2a2a3e;
    }
    .dr-chat-send:active {
        transform: scale(0.97);
    }
    .dr-collapsed .dr-chat-body {
        display: none;
    }
    /* MathJax 渲染的公式样式 */
    mjx-container {
        overflow-x: auto;
        overflow-y: hidden;
        margin: 8px 0;
    }
    .dr-arrow {
        transition: transform 0.2s ease;
        display: inline-block;
    }
    .dr-collapsed .dr-arrow {
        transform: rotate(180deg);
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
        const arrow = container.querySelector('.dr-arrow');
        const messagesDiv = document.getElementById('dr-chat-messages');
        const input = document.getElementById('dr-chat-input');
        const sendBtn = document.getElementById('dr-chat-send');
        
        let isLoading = false;
        
        header.addEventListener('click', () => {
            container.classList.toggle('dr-collapsed');
        });
        
        // 将 Markdown 转换为 HTML，同时保留 LaTeX 公式
        function markdownToHtml(text) {
            if (!text) return '';
            
            // 临时保护 LaTeX 公式，避免被 marked 误解析
            const latexBlocks = [];
            const latexInlines = [];
            
            // 保护 $$...$$ 块级公式
            text = text.replace(/\$\$([\s\S]*?)\$\$/g, (match, formula) => {
                const idx = latexBlocks.length;
                latexBlocks.push(formula);
                return `@@LATEX_BLOCK_${idx}@@`;
            });
            
            // 保护 $...$ 行内公式
            text = text.replace(/\$([^\$\n]+?)\$/g, (match, formula) => {
                const idx = latexInlines.length;
                latexInlines.push(formula);
                return `@@LATEX_INLINE_${idx}@@`;
            });
            
            // 使用 marked 解析 Markdown
            let html = marked.parse(text, { mangle: false, headerIds: false });
            
            // 恢复块级公式
            html = html.replace(/@@LATEX_BLOCK_(\d+)@@/g, (match, idx) => {
                return `$$${latexBlocks[parseInt(idx)]}$$`;
            });
            
            // 恢复行内公式
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
            
            // 触发 MathJax 渲染新公式
            if (role === 'bot' && window.MathJax) {
                MathJax.typesetPromise([div]).catch(err => console.warn('MathJax error:', err));
            }
        }
        
        async function sendMessage() {
            const message = input.value.trim();
            if (!message || isLoading) return;
            
            addMessage('user', message);
            input.value = '';
            input.style.height = 'auto';
            
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
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
            }
        });
        
        // 自动调整输入框高度（可选）
        input.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = Math.min(this.scrollHeight, 100) + 'px';
        });
    })();
    </script>