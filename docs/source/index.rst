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

    <div id="drestryrobot-chat-root" style="position: fixed; bottom: 20px; right: 20px; z-index: 9999;">
        <!-- 聊天窗口会动态加载到这里 -->
    </div>

    <style>
        /* 基础样式 */
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
            transition: all 0.2s ease !important;
        }
        
        @media (max-width: 768px) {
            .dr-chat-container.dr-collapsed {
                width: auto !important;
                min-width: 140px !important;
                bottom: 20px !important;
                left: 50% !important;
                right: auto !important;
                transform: translateX(-50%) !important;
            }
            .dr-chat-container:not(.dr-collapsed) {
                width: 100vw !important;
                height: 80vh !important;
                bottom: 0 !important;
                left: 0 !important;
                right: 0 !important;
                top: auto !important;
                transform: none !important;
                border-radius: 16px 16px 0 0 !important;
            }
            .dr-chat-container:not(.dr-collapsed) .dr-chat-body {
                height: calc(80vh - 56px) !important;
            }
            .dr-chat-container.dr-collapsed .dr-chat-body {
                display: none !important;
            }
        }
        
        .dr-chat-header {
            background: #1a1a2e !important;
            color: white !important;
            padding: 12px 16px !important;
            border-radius: 16px 16px 0 0 !important;
            font-weight: 600 !important;
            cursor: pointer !important;
            display: flex !important;
            justify-content: space-between !important;
            align-items: center !important;
        }
        
        .dr-header-left { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
        .dr-header-right { display: flex; align-items: center; gap: 12px; }
        
        .dr-quota-badge {
            background: #4caf50;
            color: white;
            font-size: 11px;
            border-radius: 20px;
            padding: 4px 10px;
            font-weight: normal;
        }
        .dr-quota-badge.low { background: #ff9800; }
        .dr-quota-badge.none { background: #f44336; }
        
        .dr-admin-icon {
            cursor: pointer;
            font-size: 12px;
            padding: 4px 10px;
            border-radius: 20px;
            background: rgba(255,255,255,0.15);
            transition: background 0.2s;
        }
        .dr-admin-icon:hover { background: rgba(255,255,255,0.3); }
        
        .dr-arrow { transition: transform 0.2s; font-size: 12px; }
        .dr-collapsed .dr-arrow { transform: rotate(180deg); }
        
        .dr-chat-body {
            display: flex !important;
            flex-direction: column !important;
            height: 500px !important;
            background: #f5f5f5;
        }
        
        .dr-chat-messages {
            flex: 1 !important;
            overflow-y: auto !important;
            padding: 16px !important;
            background: #fafafa !important;
        }
        
        .dr-message {
            margin-bottom: 12px !important;
            padding: 8px 12px !important;
            border-radius: 12px !important;
            max-width: 85% !important;
            word-wrap: break-word !important;
        }
        
        .dr-user {
            background: #1a1a2e !important;
            color: white !important;
            margin-left: auto !important;
            border-bottom-right-radius: 4px !important;
        }
        
        .dr-bot {
            background: #e8e8ec !important;
            color: #1a1a2e !important;
            margin-right: auto !important;
            border-bottom-left-radius: 4px !important;
        }
        
        .dr-chat-input-area {
            display: flex !important;
            padding: 12px !important;
            gap: 8px !important;
            border-top: 1px solid #e0e0e0 !important;
            background: white !important;
            position: relative;
        }
        
        .dr-chat-input {
            flex: 1 !important;
            padding: 10px 14px !important;
            border: 1px solid #ddd !important;
            border-radius: 24px !important;
            outline: none !important;
            font-size: 14px !important;
        }
        
        .dr-chat-send {
            background: #1a1a2e !important;
            color: white !important;
            border: none !important;
            border-radius: 24px !important;
            padding: 0 18px !important;
            cursor: pointer !important;
            font-size: 13px !important;
            font-weight: 500 !important;
        }
        
        .dr-chat-send:disabled { background: #ccc !important; cursor: not-allowed; }
        .dr-unlock-btn { background: #ff9800 !important; }
        
        .dr-admin-panel {
            display: none;
            background: white;
            border-top: 1px solid #e0e0e0;
            flex-direction: column;
            max-height: 260px;
            overflow: hidden;
        }
        .dr-admin-panel.active { display: flex; }
        .dr-admin-header {
            background: #1a1a2e;
            color: white;
            padding: 8px 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 12px;
        }
        .dr-admin-list {
            max-height: 200px;
            overflow-y: auto;
            padding: 10px;
            background: #fafafa;
        }
        .dr-order-item {
            background: white;
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 8px;
            border-left: 3px solid #ff9800;
            font-size: 12px;
        }
        .dr-order-device {
            font-family: monospace;
            font-size: 10px;
            background: #f0f0f0;
            padding: 4px 8px;
            border-radius: 6px;
            word-break: break-all;
        }
        .dr-unlock-btn-admin {
            background: #4caf50;
            color: white;
            border: none;
            border-radius: 20px;
            padding: 5px 10px;
            font-size: 11px;
            cursor: pointer;
            margin-top: 6px;
            width: 100%;
        }
        .dr-refresh-btn {
            background: #ff9800;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 4px 10px;
            cursor: pointer;
            font-size: 11px;
        }
        .search-input {
            width: 100%;
            padding: 6px 10px;
            border: 1px solid #ddd;
            border-radius: 8px;
            margin-bottom: 8px;
            font-size: 12px;
            box-sizing: border-box;
        }
        
        .dr-donate-modal {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.8);
            z-index: 10001;
            display: flex;
            justify-content: center;
            align-items: center;
            visibility: hidden;
            opacity: 0;
            transition: all 0.3s;
        }
        .dr-donate-modal.active {
            visibility: visible;
            opacity: 1;
        }
        .dr-donate-content {
            background: white;
            border-radius: 24px;
            max-width: 90vw;
            width: 340px;
            padding: 24px;
            text-align: center;
            position: relative;
        }
        .dr-donate-qr {
            width: 220px;
            height: 220px;
            margin: 16px auto;
            background: #f5f5f5;
            border-radius: 12px;
            overflow: hidden;
        }
        .dr-donate-qr img {
            width: 100%;
            height: auto;
        }
        .dr-device-id-input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 12px;
            margin: 12px 0;
            font-family: monospace;
            font-size: 12px;
            background: #f5f5f5;
            text-align: center;
        }
        .dr-tip {
            background: #fff3e0;
            padding: 10px;
            border-radius: 12px;
            font-size: 12px;
            color: #e67e22;
            margin: 12px 0;
        }
        .dr-check-payment {
            background: #ff9800;
            color: white;
            border: none;
            border-radius: 28px;
            padding: 12px;
            width: 100%;
            font-size: 15px;
            font-weight: bold;
            cursor: pointer;
            margin-top: 12px;
        }
        .dr-close-modal {
            position: absolute;
            top: 12px;
            right: 16px;
            font-size: 22px;
            cursor: pointer;
            color: #999;
        }
        .dr-disclaimer {
            font-size: 10px;
            color: #999;
            margin-top: 14px;
            padding-top: 10px;
            border-top: 1px solid #eee;
        }
        
        .dr-typing-cursor {
            display: inline-block;
            width: 2px;
            height: 1.2em;
            background-color: #1a1a2e;
            margin-left: 2px;
            vertical-align: middle;
            animation: blink 1s step-end infinite;
        }
        @keyframes blink { 0%,100% { opacity: 1; } 50% { opacity: 0; } }
        
        .dr-quota-warning {
            background: #fff3e0;
            padding: 8px;
            font-size: 12px;
            text-align: center;
            color: #e67e22;
        }
        .dr-lock-overlay {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(255,255,240,0.95);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10;
        }
        .dr-lock-message {
            background: #1a1a2e;
            color: white;
            padding: 10px 20px;
            border-radius: 40px;
            font-size: 13px;
            font-weight: bold;
            cursor: pointer;
        }
        mjx-container { overflow-x: auto !important; margin: 8px 0 !important; }
    </style>

    <!-- 引入依赖库 -->
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/highlight.js/lib/core.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/highlight.js/lib/languages/python.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/highlight.js/lib/languages/javascript.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/highlight.js/lib/languages/cpp.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/highlight.js/styles/github-dark.css">

.. raw:: html

    <div id="dr-chat-widget" class="dr-chat-container dr-collapsed">
        <div class="dr-chat-header">
            <div class="dr-header-left">
                <span>🤖 DrestryRobot 助手</span>
                <span id="quotaBadge" class="dr-quota-badge">免费 3/3 次</span>
            </div>
            <div class="dr-header-right">
                <span class="dr-admin-icon" id="adminToggle">⚙️ 管理</span>
                <span class="dr-arrow">▼</span>
            </div>
        </div>
        <div class="dr-chat-body">
            <div id="quotaWarning" class="dr-quota-warning" style="display:none;">⚠️ 免费额度已用完，请付费解锁</div>
            
            <div id="adminPanel" class="dr-admin-panel">
                <div class="dr-admin-header">
                    <span>🔐 待解锁订单</span>
                    <button class="dr-refresh-btn" id="refreshBtn">刷新</button>
                </div>
                <div style="padding: 8px 10px 0;">
                    <input type="text" id="searchInput" class="search-input" placeholder="🔍 搜索设备ID">
                </div>
                <div class="dr-admin-list" id="orderList">加载中...</div>
            </div>
            
            <div class="dr-chat-messages" id="chatMessages">
                <div class="dr-message dr-bot">🤖 欢迎！<br>🎁 新用户 <strong>3次免费</strong><br>💰 用完后 ¥1 永久解锁<br>开始提问吧！</div>
            </div>
            
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
            <div class="dr-donate-qr">
                <img src="https://drestryrobot.oss-cn-shanghai.aliyuncs.com/202605%20%E8%B5%9E%E8%B5%8F%E7%A0%81.png" alt="赞赏码">
            </div>
            <div class="dr-tip">
                💡 扫码支付 <strong>¥1</strong><br>
                ⚠️ 备注填写下方设备ID
            </div>
            <input type="text" id="deviceIdInput" class="dr-device-id-input" readonly onclick="this.select()">
            <button class="dr-check-payment" id="submitPayBtn">✅ 我已支付，输入密码解锁</button>
            <div class="dr-disclaimer">⚠️ 个人开发，服务可能调整，请谅解</div>
        </div>
    </div>

    <script>
    (function() {
        // ========== 配置 ==========
        var UNLOCK_PASSWORD = 'drestry2025';  // 解锁密码，可修改
        var FREE_QUOTA = 3;
        
        var STORAGE_USED = 'dr_used_quota';
        var STORAGE_DEVICE = 'dr_device_id';
        var STORAGE_UNLOCKED = 'dr_unlocked_v3';
        var STORAGE_PENDING = 'dr_pending';
        
        var DEEPSEEK_KEY = 'sk-c09347c4e827479a842a21acf5771103';
        
        // ========== 设备ID ==========
        function getDeviceId() {
            var id = localStorage.getItem(STORAGE_DEVICE);
            if (!id) {
                id = 'DR_' + Date.now().toString(36) + '_' + Math.random().toString(36).substring(2, 10);
                localStorage.setItem(STORAGE_DEVICE, id);
            }
            return id;
        }
        
        // ========== 解锁状态 ==========
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
        
        // ========== 额度管理 ==========
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
        
        // ========== UI更新 ==========
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
                if (sendBtn) {
                    sendBtn.disabled = false;
                    sendBtn.innerHTML = '发送';
                    sendBtn.classList.remove('dr-unlock-btn');
                }
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
                if (sendBtn) {
                    sendBtn.disabled = false;
                    sendBtn.innerHTML = '💰 付费解锁';
                    sendBtn.classList.add('dr-unlock-btn');
                }
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
                if (sendBtn) {
                    sendBtn.disabled = false;
                    sendBtn.innerHTML = '发送';
                    sendBtn.classList.remove('dr-unlock-btn');
                }
                var overlay2 = inputArea ? inputArea.querySelector('.dr-lock-overlay') : null;
                if (overlay2) overlay2.remove();
            }
        }
        
        // ========== 付费弹窗 ==========
        function showPayModal() {
            document.getElementById('deviceIdInput').value = getDeviceId();
            document.getElementById('payModal').classList.add('active');
        }
        
        function closePayModal() {
            document.getElementById('payModal').classList.remove('active');
        }
        
        // 用户提交：输入密码解锁
        function submitPayment() {
            var pwd = prompt('🔐 请输入解锁密码（付款后向管理员索取）\n\n提示：付款时备注设备ID，联系管理员获取密码');
            
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
                alert('❌ 密码错误！请确认已付款并备注设备ID后联系管理员获取正确密码。');
            }
        }
        
        // ========== 管理员功能 ==========
        var adminAuth = false;
        
        function toggleAdmin() {
            var panel = document.getElementById('adminPanel');
            if (panel.classList.contains('active')) {
                panel.classList.remove('active');
                return;
            }
            
            if (!adminAuth) {
                var pwd = prompt('管理员密码：');
                if (pwd !== '666666') {
                    alert('密码错误');
                    return;
                }
                adminAuth = true;
            }
            panel.classList.add('active');
            loadOrders();
        }
        
        function loadOrders() {
            var pending = JSON.parse(localStorage.getItem(STORAGE_PENDING) || '[]');
            var search = document.getElementById('searchInput').value.toLowerCase();
            var container = document.getElementById('orderList');
            var filtered = pending.filter(function(o) {
                return o.status === 'pending' && (search === '' || o.deviceId.toLowerCase().indexOf(search) !== -1);
            });
            
            if (filtered.length === 0) {
                container.innerHTML = '<div style="text-align:center;padding:20px;color:#999;">暂无订单</div>';
                return;
            }
            
            container.innerHTML = '';
            for (var i = 0; i < filtered.length; i++) {
                var order = filtered[i];
                var div = document.createElement('div');
                div.className = 'dr-order-item';
                div.innerHTML = '<div class="dr-order-device">🖥️ ' + escapeHtml(order.deviceId) + '</div>' +
                    '<div>⏰ ' + new Date(order.time).toLocaleString() + '</div>' +
                    '<div>💰 ¥' + order.amount + '</div>' +
                    '<button class="dr-unlock-btn-admin" data-id="' + escapeHtml(order.deviceId) + '">✅ 确认解锁</button>';
                container.appendChild(div);
                var btn = div.querySelector('button');
                btn.onclick = (function(did) { return function() { confirmUnlock(did); }; })(order.deviceId);
            }
        }
        
        function confirmUnlock(deviceId) {
            if (!confirm('确认设备 ' + deviceId + ' 已付款并解锁？')) return;
            
            var pending = JSON.parse(localStorage.getItem(STORAGE_PENDING) || '[]');
            var idx = -1;
            for (var i = 0; i < pending.length; i++) {
                if (pending[i].deviceId === deviceId && pending[i].status === 'pending') {
                    idx = i;
                    break;
                }
            }
            if (idx !== -1) pending.splice(idx, 1);
            localStorage.setItem(STORAGE_PENDING, JSON.stringify(pending));
            
            markUnlocked(deviceId);
            if (getDeviceId() === deviceId) updateUI();
            alert('✅ 已解锁！');
            loadOrders();
        }
        
        function escapeHtml(str) {
            return str.replace(/[&<>]/g, function(m) {
                if (m === '&') return '&amp;';
                if (m === '<') return '&lt;';
                if (m === '>') return '&gt;';
                return m;
            });
        }
        
        // ========== 聊天功能 ==========
        var isLoading = false;
        var streamingDiv = null;
        var streamContent = '';
        
        marked.setOptions({
            highlight: function(code, lang) {
                if (lang && hljs.getLanguage(lang)) {
                    try { return hljs.highlight(code, { language: lang }).value; } catch(e) {}
                }
                return code;
            }
        });
        
        function mdToHtml(text) {
            if (!text) return '';
            var latexBlocks = [], latexInlines = [];
            text = text.replace(/\$\$([\s\S]*?)\$\$/g, function(m, f) {
                var i = latexBlocks.length;
                latexBlocks.push(f);
                return '@@LB_' + i + '@@';
            });
            text = text.replace(/\$([^\$\n]+?)\$/g, function(m, f) {
                var i = latexInlines.length;
                latexInlines.push(f);
                return '@@LI_' + i + '@@';
            });
            var html = marked.parse(text, { mangle: false, headerIds: false });
            html = html.replace(/@@LB_(\d+)@@/g, function(m, i) { return '$$' + latexBlocks[parseInt(i)] + '$$'; });
            html = html.replace(/@@LI_(\d+)@@/g, function(m, i) { return '$' + latexInlines[parseInt(i)] + '$'; });
            return html;
        }
        
        function addMsg(role, content) {
            var msgs = document.getElementById('chatMessages');
            var div = document.createElement('div');
            div.className = 'dr-message dr-' + role;
            if (role === 'user') {
                div.textContent = content;
            } else {
                div.innerHTML = mdToHtml(content);
                if (typeof hljs !== 'undefined') {
                    div.querySelectorAll('pre code').forEach(function(b) { hljs.highlightElement(b); });
                }
            }
            msgs.appendChild(div);
            msgs.scrollTop = msgs.scrollHeight;
            if (role === 'bot' && window.MathJax) MathJax.typesetPromise([div]).catch(function(e) {});
        }
        
        function startStream() {
            streamingDiv = document.createElement('div');
            streamingDiv.className = 'dr-message dr-bot';
            streamingDiv.innerHTML = '<span class="dr-typing-cursor"></span>';
            document.getElementById('chatMessages').appendChild(streamingDiv);
            streamContent = '';
        }
        
        function updateStream(chunk) {
            if (!streamingDiv) return;
            streamContent += chunk;
            streamingDiv.innerHTML = mdToHtml(streamContent) + '<span class="dr-typing-cursor"></span>';
            document.getElementById('chatMessages').scrollTop = document.getElementById('chatMessages').scrollHeight;
        }
        
        function endStream() {
            if (!streamingDiv) return;
            streamingDiv.innerHTML = mdToHtml(streamContent);
            if (window.MathJax) MathJax.typesetPromise([streamingDiv]).catch(function(e) {});
            if (typeof hljs !== 'undefined') {
                streamingDiv.querySelectorAll('pre code').forEach(function(b) { hljs.highlightElement(b); });
            }
            streamingDiv = null;
            streamContent = '';
        }
        
        async function sendMsg() {
            if (!canAsk()) {
                showPayModal();
                return;
            }
            var input = document.getElementById('chatInput');
            var msg = input.value.trim();
            if (!msg || isLoading) return;
            addMsg('user', msg);
            input.value = '';
            if (!isUnlocked()) incrementUsed();
            isLoading = true;
            startStream();
            try {
                var res = await fetch('https://api.deepseek.com/v1/chat/completions', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + DEEPSEEK_KEY },
                    body: JSON.stringify({
                        model: 'deepseek-chat',
                        messages: [{ role: 'system', content: '你是机器人学专家。回答严谨深刻。用Markdown格式：##标题、-列表、$公式$、```代码```。' }, { role: 'user', content: msg }],
                        temperature: 0.3,
                        stream: true
                    })
                });
                var reader = res.body.getReader();
                var decoder = new TextDecoder();
                var buf = '';
                while (true) {
                    var result = await reader.read();
                    if (result.done) break;
                    buf += decoder.decode(result.value, { stream: true });
                    var lines = buf.split('\n');
                    buf = lines.pop() || '';
                    for (var i = 0; i < lines.length; i++) {
                        var line = lines[i];
                        if (line.startsWith('data: ')) {
                            var data = line.slice(6);
                            if (data === '[DONE]') continue;
                            try {
                                var parsed = JSON.parse(data);
                                var chunk = parsed.choices[0] && parsed.choices[0].delta && parsed.choices[0].delta.content;
                                if (chunk) updateStream(chunk);
                            } catch(e) {}
                        }
                    }
                }
                endStream();
            } catch(e) {
                if (streamingDiv) streamingDiv.remove();
                streamingDiv = null;
                addMsg('bot', '调用失败：' + e.message);
            }
            isLoading = false;
        }
        
        // ========== 事件绑定 ==========
        function bindEvents() {
            var header = document.querySelector('.dr-chat-header');
            var send = document.getElementById('sendBtn');
            var input = document.getElementById('chatInput');
            var admin = document.getElementById('adminToggle');
            var refresh = document.getElementById('refreshBtn');
            var search = document.getElementById('searchInput');
            var closeModal = document.getElementById('closeModalBtn');
            var submitPay = document.getElementById('submitPayBtn');
            
            if (header) {
                header.addEventListener('click', function(e) {
                    if (e.target === admin || (admin && admin.contains(e.target))) return;
                    document.getElementById('dr-chat-widget').classList.toggle('dr-collapsed');
                });
            }
            if (admin) admin.addEventListener('click', function(e) { e.stopPropagation(); toggleAdmin(); });
            if (refresh) refresh.addEventListener('click', loadOrders);
            if (search) search.addEventListener('input', loadOrders);
            if (send) send.addEventListener('click', function() { if (!canAsk() && !isUnlocked()) showPayModal(); else sendMsg(); });
            if (input) input.addEventListener('keypress', function(e) { if (e.key === 'Enter') { e.preventDefault(); if (!canAsk() && !isUnlocked()) showPayModal(); else sendMsg(); } });
            if (closeModal) closeModal.addEventListener('click', closePayModal);
            if (submitPay) submitPay.addEventListener('click', submitPayment);
        }
        
        // ========== 初始化 ==========
        function init() {
            bindEvents();
            updateUI();
            console.log('DrestryRobot 已启动 | 管理员密码: 666666 | 用户密码: ' + UNLOCK_PASSWORD);
        }
        
        window.showPayModal = showPayModal;
        window.closePayModal = closePayModal;
        window.submitPayment = submitPayment;
        
        init();
    })();
    </script>