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

    <style>
    .dr-chat-container {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 360px;
        max-width: 90vw;
        background: white;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        font-family: system-ui, sans-serif;
        z-index: 9999;
        display: flex;
        flex-direction: column;
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
    }
    .dr-chat-body {
        display: flex;
        flex-direction: column;
        height: 400px;
    }
    .dr-chat-messages {
        flex: 1;
        overflow-y: auto;
        padding: 12px;
        background: #f5f5f5;
        font-size: 14px;
    }
    .dr-message {
        margin-bottom: 12px;
        padding: 8px 12px;
        border-radius: 8px;
        max-width: 85%;
        word-wrap: break-word;
    }
    .dr-user {
        background: #1a1a2e;
        color: white;
        margin-left: auto;
        text-align: right;
    }
    .dr-bot {
        background: #e0e0e0;
        color: #1a1a2e;
        margin-right: auto;
    }
    .dr-loading {
        color: #666;
        font-style: italic;
        padding: 8px 12px;
    }
    .dr-chat-input-area {
        display: flex;
        padding: 12px;
        gap: 8px;
        border-top: 1px solid #ddd;
        background: white;
        border-radius: 0 0 12px 12px;
    }
    .dr-chat-input {
        flex: 1;
        padding: 8px 12px;
        border: 1px solid #ccc;
        border-radius: 20px;
        outline: none;
    }
    .dr-chat-send {
        background: #1a1a2e;
        color: white;
        border: none;
        border-radius: 20px;
        padding: 8px 16px;
        cursor: pointer;
    }
    .dr-collapsed .dr-chat-body {
        display: none;
    }
    </style>

    <div id="dr-chat-widget" class="dr-chat-container dr-collapsed">
        <div class="dr-chat-header">
            <span>🤖 DrestryRobot 智能助手</span>
            <span>▼</span>
        </div>
        <div class="dr-chat-body">
            <div class="dr-chat-messages">
                <div class="dr-message dr-bot">你好，我是 DrestryRobot 助手。请提出机器人相关问题。</div>
            </div>
            <div class="dr-chat-input-area">
                <input type="text" class="dr-chat-input" placeholder="问点什么...">
                <button class="dr-chat-send">发送</button>
            </div>
        </div>
    </div>

    <script>
    (function() {
        const DEEPSEEK_KEY = 'sk-c09347c4e827479a842a21acf5771103';
        
        // 防止重复加载
        if (window.__drestryrobotChatLoaded) return;
        window.__drestryrobotChatLoaded = true;
        
        const container = document.getElementById('dr-chat-widget');
        const header = container.querySelector('.dr-chat-header');
        const messagesDiv = container.querySelector('.dr-chat-messages');
        const input = container.querySelector('.dr-chat-input');
        const sendBtn = container.querySelector('.dr-chat-send');
        
        let isLoading = false;
        
        header.addEventListener('click', () => {
            container.classList.toggle('dr-collapsed');
        });
        
        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }
        
        async function sendMessage() {
            const message = input.value.trim();
            if (!message || isLoading) return;
            
            messagesDiv.innerHTML += `<div class="dr-message dr-user">${escapeHtml(message)}</div>`;
            input.value = '';
            
            const loadingDiv = document.createElement('div');
            loadingDiv.className = 'dr-loading';
            loadingDiv.innerText = '思考中...';
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
                            { role: 'system', content: '你是 DrestryRobot 知识库的机器人专家。回答应严谨、深刻、偏重机器人学理论（运动学/动力学/控制/感知），不用代码但可用公式，避免浅显解释。' },
                            { role: 'user', content: message }
                        ],
                        temperature: 0.3
                    })
                });
                
                const data = await response.json();
                const reply = data.choices[0].message.content;
                
                loadingDiv.remove();
                messagesDiv.innerHTML += `<div class="dr-message dr-bot">${escapeHtml(reply)}</div>`;
                messagesDiv.scrollTop = messagesDiv.scrollHeight;
            } catch (error) {
                loadingDiv.remove();
                messagesDiv.innerHTML += `<div class="dr-message dr-bot">❌ 调用失败：${error.message}</div>`;
            }
            isLoading = false;
        }
        
        sendBtn.addEventListener('click', sendMessage);
        input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') sendMessage();
        });
    })();
    </script>