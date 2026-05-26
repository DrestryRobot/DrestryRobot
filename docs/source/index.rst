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

    <div id="dr-chat-root" style="position: fixed; bottom: 20px; right: 20px; z-index: 9999;"></div>

    <style>
        .dr-chat-container {
            position: fixed !important;
            bottom: 20px !important;
            right: 20px !important;
            width: 380px !important;
            max-width: 90vw !important;
            background: white !important;
            border-radius: 16px !important;
            box-shadow: 0 4px 24px rgba(0,0,0,0.15) !important;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
            z-index: 9999 !important;
            display: flex !important;
            flex-direction: column !important;
            font-size: 14px !important;
            line-height: 1.5 !important;
        }
        @media (max-width: 768px) {
            .dr-chat-container.dr-collapsed { width: auto !important; min-width: 140px !important; bottom: 20px !important; left: 50% !important; right: auto !important; transform: translateX(-50%) !important; }
            .dr-chat-container:not(.dr-collapsed) { width: 100vw !important; height: 80vh !important; bottom: 0 !important; left: 0 !important; right: 0 !important; border-radius: 16px 16px 0 0 !important; }
            .dr-chat-container:not(.dr-collapsed) .dr-chat-body { height: calc(80vh - 56px) !important; }
            .dr-chat-container.dr-collapsed .dr-chat-body { display: none !important; }
        }
        .dr-chat-header { background: #1a1a2e; color: white; padding: 12px 16px; border-radius: 16px 16px 0 0; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center; }
        .dr-header-left { display: flex; align-items: center; gap: 8px; }
        .dr-header-right { display: flex; align-items: center; gap: 12px; }
        .dr-quota-badge { background: #4caf50; color: white; font-size: 11px; border-radius: 20px; padding: 4px 10px; }
        .dr-quota-badge.low { background: #ff9800; }
        .dr-quota-badge.none { background: #f44336; }
        .dr-arrow { transition: transform 0.2s; font-size: 12px; }
        .dr-collapsed .dr-arrow { transform: rotate(180deg); }
        .dr-chat-body { display: flex; flex-direction: column; height: 500px; background: #f5f5f5; }
        .dr-chat-messages { flex: 1; overflow-y: auto; padding: 16px; background: #fafafa; }
        .dr-message { margin-bottom: 12px; padding: 8px 12px; border-radius: 12px; max-width: 85%; word-wrap: break-word; }
        .dr-user { background: #1a1a2e; color: white; margin-left: auto; border-bottom-right-radius: 4px; }
        .dr-bot { background: #e8e8ec; color: #1a1a2e; margin-right: auto; border-bottom-left-radius: 4px; }
        .dr-chat-input-area { display: flex; padding: 12px; gap: 8px; border-top: 1px solid #e0e0e0; background: white; position: relative; }
        .dr-chat-input { flex: 1; padding: 10px 14px; border: 1px solid #ddd; border-radius: 24px; outline: none; font-size: 14px; }
        .dr-chat-send { background: #1a1a2e; color: white; border: none; border-radius: 24px; padding: 0 18px; cursor: pointer; font-size: 13px; }
        .dr-chat-send:disabled { background: #ccc; cursor: not-allowed; }
        .dr-unlock-btn { background: #ff9800 !important; }
        .dr-donate-modal { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); z-index: 10001; display: flex; justify-content: center; align-items: center; visibility: hidden; opacity: 0; transition: all 0.3s; }
        .dr-donate-modal.active { visibility: visible; opacity: 1; }
        .dr-donate-content { background: white; border-radius: 24px; max-width: 90vw; width: 340px; padding: 24px; text-align: center; position: relative; }
        .dr-donate-qr { width: 220px; height: 220px; margin: 16px auto; background: #f5f5f5; border-radius: 12px; overflow: hidden; }
        .dr-donate-qr img { width: 100%; height: auto; }
        .dr-device-id-input { width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 12px; margin: 12px 0; font-family: monospace; font-size: 12px; background: #f5f5f5; text-align: center; }
        .dr-tip { background: #fff3e0; padding: 10px; border-radius: 12px; font-size: 12px; color: #e67e22; margin: 12px 0; }
        .dr-check-payment { background: #ff9800; color: white; border: none; border-radius: 28px; padding: 12px; width: 100%; font-size: 15px; font-weight: bold; cursor: pointer; margin-top: 12px; }
        .dr-close-modal { position: absolute; top: 12px; right: 16px; font-size: 22px; cursor: pointer; color: #999; }
        .dr-disclaimer { font-size: 10px; color: #999; margin-top: 14px; padding-top: 10px; border-top: 1px solid #eee; }
        .dr-typing-cursor { display: inline-block; width: 2px; height: 1.2em; background-color: #1a1a2e; margin-left: 2px; vertical-align: middle; animation: blink 1s step-end infinite; }
        @keyframes blink { 0%,100% { opacity: 1; } 50% { opacity: 0; } }
        .dr-quota-warning { background: #fff3e0; padding: 8px; font-size: 12px; text-align: center; color: #e67e22; }
        .dr-lock-overlay { position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: rgba(255,255,240,0.95); border-radius: 12px; display: flex; align-items: center; justify-content: center; z-index: 10; }
        .dr-lock-message { background: #1a1a2e; color: white; padding: 10px 20px; border-radius: 40px; font-size: 13px; font-weight: bold; cursor: pointer; }
        pre { background: #0d1117; color: #e6edf3; padding: 12px; border-radius: 8px; overflow-x: auto; margin: 8px 0; }
        code { font-family: 'SF Mono', Monaco, monospace; font-size: 13px; }
        :not(pre) > code { background: #e8e8ec; padding: 2px 6px; border-radius: 4px; color: #d73a49; }
        mjx-container { overflow-x: auto !important; margin: 8px 0 !important; }
    </style>

    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>

.. raw:: html

    <div id="dr-chat-widget" class="dr-chat-container dr-collapsed">
        <div class="dr-chat-header">
            <div class="dr-header-left"><span>🤖 DrestryRobot 助手</span><span id="quotaBadge" class="dr-quota-badge">免费 3/3 次</span></div>
            <div class="dr-header-right"><span class="dr-arrow">▼</span></div>
        </div>
        <div class="dr-chat-body">
            <div id="quotaWarning" class="dr-quota-warning" style="display:none;">⚠️ 免费额度已用完，请付费解锁</div>
            <div class="dr-chat-messages" id="chatMessages"><div class="dr-message dr-bot">🤖 欢迎！<br>🎁 新用户 3次免费<br>💰 用完后 ¥1 永久解锁<br>开始提问吧！</div></div>
            <div class="dr-chat-input-area" id="inputArea">
                <input type="text" class="dr-chat-input" id="chatInput" placeholder="输入问题...">
                <button class="dr-chat-send" id="sendBtn">发送</button>
            </div>
        </div>
    </div>

    <div id="payModal" class="dr-donate-modal">
        <div class="dr-donate-content">
            <span class="dr-close-modal" id="closeModalBtn">&times;</span>
            <h3>💰 ¥1 永久解锁</h3>
            <div class="dr-donate-qr"><img src="https://drestryrobot.oss-cn-shanghai.aliyuncs.com/202605%20%E8%B5%9E%E8%B5%8F%E7%A0%81.png" alt="赞赏码"></div>
            <div class="dr-tip">💡 扫码支付 <strong>¥1</strong><br>⚠️ 备注填写下方设备ID</div>
            <input type="text" id="deviceIdInput" class="dr-device-id-input" readonly onclick="this.select()">
            <button class="dr-check-payment" id="submitPayBtn">✅ 我已支付，输入密码解锁</button>
            <div class="dr-disclaimer">⚠️ 个人开发，服务可能调整，请谅解</div>
        </div>
    </div>

    <script>
    (function() {
        // 解锁密码（直接显示在提示中）
        var UNLOCK_PASSWORD = 'DrestryRobot';
        var FREE_QUOTA = 3;
        var STORAGE_USED = 'dr_used_quota';
        var STORAGE_DEVICE = 'dr_device_id';
        var STORAGE_UNLOCKED = 'dr_unlocked_v4';
        var DEEPSEEK_KEY = 'sk-c09347c4e827479a842a21acf5771103';
        
        function getDeviceId() {
            var id = localStorage.getItem(STORAGE_DEVICE);
            if (!id) {
                id = 'DR_' + Date.now().toString(36) + '_' + Math.random().toString(36).substring(2, 10);
                localStorage.setItem(STORAGE_DEVICE, id);
            }
            return id;
        }
        
        function isUnlocked() {
            var list = JSON.parse(localStorage.getItem(STORAGE_UNLOCKED) || '[]');
            return list.indexOf(getDeviceId()) !== -1;
        }
        
        function markUnlocked(deviceId) {
            var list = JSON.parse(localStorage.getItem(STORAGE_UNLOCKED) || '[]');
            if (list.indexOf(deviceId) === -1) {
                list.push(deviceId);
                localStorage.setItem(STORAGE_UNLOCKED, JSON.stringify(list));
            }
        }
        
        function getUsed() {
            if (isUnlocked()) return FREE_QUOTA;
            return parseInt(localStorage.getItem(STORAGE_USED) || '0');
        }
        
        function getRemaining() {
            if (isUnlocked()) return Infinity;
            return Math.max(0, FREE_QUOTA - getUsed());
        }
        
        function incrementUsed() {
            if (isUnlocked()) return;
            var used = getUsed() + 1;
            localStorage.setItem(STORAGE_USED, used.toString());
            updateUI();
        }
        
        function canAsk() {
            return getRemaining() > 0;
        }
        
        function updateUI() {
            var badge = document.getElementById('quotaBadge');
            var warning = document.getElementById('quotaWarning');
            var input = document.getElementById('chatInput');
            var sendBtn = document.getElementById('sendBtn');
            var inputArea = document.getElementById('inputArea');
            
            if (isUnlocked()) {
                badge.innerHTML = '🌟 永久解锁';
                badge.style.background = '#9c27b0';
                if (warning) warning.style.display = 'none';
                if (input) input.disabled = false;
                if (sendBtn) { sendBtn.disabled = false; sendBtn.innerHTML = '发送'; sendBtn.classList.remove('dr-unlock-btn'); }
                var overlay = inputArea ? inputArea.querySelector('.dr-lock-overlay') : null;
                if (overlay) overlay.remove();
                return;
            }
            
            var remaining = getRemaining();
            badge.innerHTML = '🎁 免费 ' + remaining + '/' + FREE_QUOTA + ' 次';
            
            if (remaining <= 0) {
                badge.className = 'dr-quota-badge none';
                if (warning) warning.style.display = 'block';
                if (input) input.disabled = true;
                if (sendBtn) { sendBtn.disabled = false; sendBtn.innerHTML = '💰 付费解锁'; sendBtn.classList.add('dr-unlock-btn'); }
                if (inputArea && !inputArea.querySelector('.dr-lock-overlay')) {
                    var lock = document.createElement('div');
                    lock.className = 'dr-lock-overlay';
                    lock.innerHTML = '<div class="dr-lock-message">💰 点击付费 ¥1 永久解锁</div>';
                    lock.onclick = function() { showPayModal(); };
                    inputArea.appendChild(lock);
                }
            } else {
                badge.className = remaining === 1 ? 'dr-quota-badge low' : 'dr-quota-badge';
                if (warning) warning.style.display = 'none';
                if (input) input.disabled = false;
                if (sendBtn) { sendBtn.disabled = false; sendBtn.innerHTML = '发送'; sendBtn.classList.remove('dr-unlock-btn'); }
                var overlay2 = inputArea ? inputArea.querySelector('.dr-lock-overlay') : null;
                if (overlay2) overlay2.remove();
            }
        }
        
        function showPayModal() {
            document.getElementById('deviceIdInput').value = getDeviceId();
            document.getElementById('payModal').classList.add('active');
        }
        
        function closePayModal() {
            document.getElementById('payModal').classList.remove('active');
        }
        
        function submitPayment() {
            var pwd = prompt('🔐 请输入解锁密码\n\n密码: DrestryRobot');
            if (pwd === UNLOCK_PASSWORD) {
                var deviceId = getDeviceId();
                markUnlocked(deviceId);
                updateUI();
                closePayModal();
                alert('✅ 解锁成功！现在可以无限次提问了。');
                var msgs = document.getElementById('chatMessages');
                var msg = document.createElement('div');
                msg.className = 'dr-message dr-bot';
                msg.innerHTML = '🎉 恭喜！已永久解锁！';
                msgs.appendChild(msg);
                msgs.scrollTop = msgs.scrollHeight;
            } else {
                alert('❌ 密码错误！请确认已付款后输入正确密码。');
            }
        }
        
        // ========== 聊天功能 ==========
        var isLoading = false;
        
        function mdToHtml(text) {
            if (!text) return '';
            var latexBlocks = [], latexInlines = [];
            text = text.replace(/\$\$([\s\S]*?)\$\$/g, function(m, f) { var i = latexBlocks.length; latexBlocks.push(f); return '@@LB_' + i + '@@'; });
            text = text.replace(/\$([^\$\n]+?)\$/g, function(m, f) { var i = latexInlines.length; latexInlines.push(f); return '@@LI_' + i + '@@'; });
            var html = marked.parse(text, { mangle: false, headerIds: false });
            html = html.replace(/@@LB_(\d+)@@/g, function(m, i) { return '$$' + latexBlocks[parseInt(i)] + '$$'; });
            html = html.replace(/@@LI_(\d+)@@/g, function(m, i) { return '$' + latexInlines[parseInt(i)] + '$'; });
            return html;
        }
        
        function addMsg(role, content) {
            var msgs = document.getElementById('chatMessages');
            var div = document.createElement('div');
            div.className = 'dr-message dr-' + role;
            if (role === 'user') { div.textContent = content; }
            else { div.innerHTML = mdToHtml(content); }
            msgs.appendChild(div);
            msgs.scrollTop = msgs.scrollHeight;
            if (role === 'bot' && window.MathJax) MathJax.typesetPromise([div]).catch(function(e) {});
        }
        
        function showLoading() {
            var msgs = document.getElementById('chatMessages');
            var loadingDiv = document.createElement('div');
            loadingDiv.className = 'dr-message dr-bot';
            loadingDiv.id = 'loadingMsg';
            loadingDiv.innerHTML = '<span style="display:inline-block;width:16px;height:16px;border:2px solid #ccc;border-top-color:#1a1a2e;border-radius:50%;animation:spin 0.8s linear infinite;"></span> 思考中...';
            msgs.appendChild(loadingDiv);
            msgs.scrollTop = msgs.scrollHeight;
        }
        
        function hideLoading() {
            var loading = document.getElementById('loadingMsg');
            if (loading) loading.remove();
        }
        
        var style = document.createElement('style');
        style.textContent = '@keyframes spin { to { transform: rotate(360deg); } }';
        document.head.appendChild(style);
        
        async function sendMsg() {
            if (!canAsk()) { showPayModal(); return; }
            var input = document.getElementById('chatInput');
            var msg = input.value.trim();
            if (!msg || isLoading) return;
            addMsg('user', msg);
            input.value = '';
            if (!isUnlocked()) incrementUsed();
            isLoading = true;
            showLoading();
            
            try {
                var response = await fetch('https://api.deepseek.com/v1/chat/completions', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + DEEPSEEK_KEY },
                    body: JSON.stringify({
                        model: 'deepseek-chat',
                        messages: [
                            { role: 'system', content: '你是机器人学专家。回答严谨深刻。用Markdown格式：##标题、-列表、$公式$、```代码```。' },
                            { role: 'user', content: msg }
                        ],
                        temperature: 0.3,
                        stream: false
                    })
                });
                
                if (!response.ok) {
                    throw new Error('API请求失败: ' + response.status);
                }
                
                var data = await response.json();
                hideLoading();
                
                if (data && data.choices && data.choices[0] && data.choices[0].message) {
                    var reply = data.choices[0].message.content;
                    addMsg('bot', reply);
                } else if (data && data.error) {
                    addMsg('bot', 'API错误：' + data.error.message);
                } else {
                    addMsg('bot', '返回数据格式异常，请重试。');
                }
            } catch(error) {
                hideLoading();
                addMsg('bot', '调用失败：' + error.message + '\n\n请检查网络后重试。');
            }
            isLoading = false;
        }
        
        function bindEvents() {
            var header = document.querySelector('.dr-chat-header');
            var send = document.getElementById('sendBtn');
            var input = document.getElementById('chatInput');
            var closeModal = document.getElementById('closeModalBtn');
            var submitPay = document.getElementById('submitPayBtn');
            
            if (header) {
                header.addEventListener('click', function() {
                    document.getElementById('dr-chat-widget').classList.toggle('dr-collapsed');
                });
            }
            if (send) send.addEventListener('click', function() { if (!canAsk() && !isUnlocked()) showPayModal(); else sendMsg(); });
            if (input) input.addEventListener('keypress', function(e) { if (e.key === 'Enter') { e.preventDefault(); if (!canAsk() && !isUnlocked()) showPayModal(); else sendMsg(); } });
            if (closeModal) closeModal.addEventListener('click', closePayModal);
            if (submitPay) submitPay.addEventListener('click', submitPayment);
        }
        
        function init() {
            bindEvents();
            updateUI();
            console.log('DrestryRobot 已启动 | 解锁密码: ' + UNLOCK_PASSWORD);
        }
        
        window.showPayModal = showPayModal;
        window.closePayModal = closePayModal;
        window.submitPayment = submitPayment;
        
        init();
    })();
    </script>