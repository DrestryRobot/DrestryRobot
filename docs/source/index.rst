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

    <div id="dr-chat" style="position:fixed; bottom:20px; right:20px; width:400px; background:#fff; border-radius:12px; box-shadow:0 4px 20px rgba(0,0,0,0.15); z-index:9999; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size:14px; line-height:1.5;">
        <div style="background:#1a1a2e; color:white; padding:12px 16px; border-radius:12px 12px 0 0; cursor:pointer; font-weight:600;" onclick="toggleChat()">
            🤖 DrestryRobot 助手 <span style="float:right">▼</span>
        </div>
        <div id="dr-body" style="display:none; flex-direction:column;">
            <div id="dr-msgs" style="height:400px; overflow-y:auto; padding:16px; background:#fafafa;"></div>
            <div style="display:flex; padding:12px 16px; gap:10px; border-top:1px solid #e0e0e0; background:white;">
                <input id="dr-input" type="text" style="flex:1; padding:10px 14px; border:1px solid #ccc; border-radius:24px; outline:none; font-size:14px;" placeholder="输入问题...">
                <button id="dr-send" style="background:#1a1a2e; color:white; border:none; border-radius:24px; padding:8px 20px; cursor:pointer;">发送</button>
            </div>
        </div>
    </div>

    <script>
        function toggleChat() {
            const body = document.getElementById('dr-body');
            body.style.display = body.style.display === 'none' ? 'flex' : 'none';
        }

        const KEY = 'sk-c09347c4e827479a842a21acf5771103';
        const msgs = document.getElementById('dr-msgs');
        const input = document.getElementById('dr-input');
        const send = document.getElementById('dr-send');

        function addMsg(role, text) {
            const div = document.createElement('div');
            div.style.marginBottom = '12px';
            div.style.padding = '10px 14px';
            div.style.borderRadius = '12px';
            div.style.maxWidth = '85%';
            div.style.wordWrap = 'break-word';
            
            if (role === 'user') {
                div.style.background = '#1a1a2e';
                div.style.color = 'white';
                div.style.marginLeft = 'auto';
                div.style.borderBottomRightRadius = '4px';
                div.innerText = text;
            } else {
                div.style.background = '#e8e8ec';
                div.style.color = '#1a1a2e';
                div.style.marginRight = 'auto';
                div.style.borderBottomLeftRadius = '4px';
                // 机器人消息：用 innerHTML 并触发 MathJax 渲染
                div.innerHTML = text;
            }
            msgs.appendChild(div);
            
            // 如果是机器人消息，让 MathJax 渲染其中的公式
            if (role === 'bot' && window.MathJax) {
                MathJax.typesetPromise([div]).catch(err => console.log(err));
            }
            
            msgs.scrollTop = msgs.scrollHeight;
        }

        async function sendMsg() {
            const q = input.value.trim();
            if (!q) return;
            addMsg('user', q);
            input.value = '';

            const loadingDiv = document.createElement('div');
            loadingDiv.style.marginBottom = '12px';
            loadingDiv.style.padding = '10px 14px';
            loadingDiv.style.color = '#888';
            loadingDiv.style.fontStyle = 'italic';
            loadingDiv.innerText = '思考中...';
            msgs.appendChild(loadingDiv);
            msgs.scrollTop = msgs.scrollHeight;

            try {
                const res = await fetch('https://api.deepseek.com/v1/chat/completions', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${KEY}` },
                    body: JSON.stringify({
                        model: 'deepseek-chat',
                        messages: [{ role: 'user', content: q }]
                    })
                });
                const data = await res.json();
                const reply = data.choices[0].message.content;
                loadingDiv.remove();
                addMsg('bot', reply);
            } catch(e) {
                loadingDiv.remove();
                addMsg('bot', '调用失败：' + e.message);
            }
        }

        send.onclick = sendMsg;
        input.onkeypress = (e) => { if (e.key === 'Enter') sendMsg(); };
        
        // 初始欢迎消息
        setTimeout(() => {
            if (msgs.children.length === 0) {
                addMsg('bot', '你好，我是 DrestryRobot 助手。请提出机器人相关问题。');
            }
        }, 100);
    </script>

