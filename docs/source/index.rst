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
            font-size: 14px !important;
            line-height: 1.5 !important;
            transition: all 0.3s ease !important;
        }
        
        /* 折叠状态 - 桌面端 */
        .dr-chat-widget.dr-collapsed {
            width: 400px !important;
            min-width: 400px !important;
            max-width: auto !important;
        }
        .dr-chat-widget.dr-collapsed .dr-chat-body {
            display: none !important;
        }
        
        /* 移动端适配 (宽度 <= 768px) */
        @media (max-width: 768px) {
            .dr-chat-widget.dr-collapsed {
                position: fixed !important;
                bottom: 20px !important;
                left: 50% !important;
                right: auto !important;
                transform: translateX(-50%) !important;
                width: auto !important;
                min-width: 140px !important;
                max-width: auto !important;
                border-radius: 40px !important;
            }
            .dr-chat-widget.dr-collapsed .dr-chat-header {
                border-radius: 40px !important;
                padding: 10px 20px !important;
            }
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
            }
            .dr-chat-widget:not(.dr-collapsed) .dr-chat-header {
                border-radius: 0 !important;
                padding: 14px 16px !important;
            }
            .dr-chat-widget:not(.dr-collapsed) .dr-chat-body {
                height: calc(100% - 52px) !important;
                display: flex !important;
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
            border-radius: 16px 16px 0 0 !important;
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
        
        /* 配额标签 */
        .dr-quota-badge {
            background: #4caf50;
            color: white;
            font-size: 12px;
            border-radius: 20px;
            padding: 4px 10px;
            font-weight: normal;
            white-space: nowrap;
        }
        .dr-quota-badge.low { background: #ff9800; }
        .dr-quota-badge.none { background: #f44336; }
        .dr-quota-badge.unlocked { background: #9c27b0; }
        
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
        }
        
        /* 消息区域 */
        .dr-chat-messages {
            flex: 1 !important;
            overflow-y: auto !important;
            padding: 16px !important;
            background: #fafafa !important;
            overflow-x: hidden !important;
        }
        
        .dr-chat-messages:after {
            content: "";
            display: table;
            clear: both;
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
            text-align: justify !important;  /* 两端对齐 */
        }
        
        /* 用户消息 - 右对齐 */
        .dr-user {
            background: #1a1a2e !important;
            color: white !important;
            border-bottom-right-radius: 4px !important;
            float: right !important;
            clear: both !important;
            text-align: justify !important;
        }
        
        /* 机器人消息 - 左对齐 */
        .dr-bot {
            background: #e8e8ec !important;
            color: #1a1a2e !important;
            border-bottom-left-radius: 4px !important;
            float: left !important;
            clear: both !important;
            text-align: justify !important;
        }
        
        /* 消息内容中的段落也两端对齐 */
        .dr-message p {
            margin: 0 0 6px 0;
            text-align: justify !important;
        }
        .dr-message p:last-child {
            margin-bottom: 0;
        }
        
        /* 列表样式保持左对齐（列表不需要两端对齐） */
        .dr-message ul, .dr-message ol {
            margin: 6px 0;
            padding-left: 20px;
            text-align: left !important;
        }
        .dr-message li {
            text-align: left !important;
        }
        
        /* 标题保持左对齐 */
        .dr-message h1, .dr-message h2, .dr-message h3, 
        .dr-message h4, .dr-message h5, .dr-message h6 {
            text-align: left !important;
            margin: 8px 0 4px 0;
        }
        
        /* 代码块保持左对齐 */
        .dr-message pre, .dr-message code {
            text-align: left !important;
        }
        
        /* 输入区域 */
        .dr-chat-input-area {
            display: flex !important;
            padding: 12px 16px !important;
            gap: 10px !important;
            border-top: 1px solid #e0e0e0 !important;
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
        
        .dr-unlock-btn {
            background: #ff9800 !important;
        }
        .dr-unlock-btn:hover {
            background: #fb8c00 !important;
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
        
        /* 配额警告 */
        .dr-quota-warning {
            background: #fff3e0;
            padding: 8px 12px;
            font-size: 12px;
            text-align: center;
            border-bottom: 1px solid #ffe0b2;
            color: #e67e22;
        }
        
        /* 锁定遮罩 */
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
            backdrop-filter: blur(2px);
        }
        
        .dr-lock-message {
            background: #1a1a2e;
            color: white;
            padding: 10px 20px;
            border-radius: 40px;
            font-size: 14px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
            transition: transform 0.2s;
        }
        .dr-lock-message:hover {
            transform: scale(1.02);
        }
        
        /* 付费弹窗 */
        .dr-pay-modal {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.7);
            z-index: 10001;
            display: flex;
            justify-content: center;
            align-items: center;
            visibility: hidden;
            opacity: 0;
            transition: all 0.3s;
        }
        .dr-pay-modal.active {
            visibility: visible;
            opacity: 1;
        }
        .dr-pay-content {
            background: white;
            border-radius: 24px;
            max-width: 90vw;
            width: 360px;
            padding: 24px;
            text-align: center;
            position: relative;
            box-shadow: 0 20px 35px rgba(0,0,0,0.3);
        }
        .dr-pay-qr {
            width: 220px;
            height: 220px;
            margin: 16px auto;
            background: #f5f5f5;
            border-radius: 12px;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .dr-pay-qr img {
            width: 100%;
            height: auto;
        }
        .dr-device-id {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 12px;
            margin: 12px 0;
            font-family: monospace;
            font-size: 12px;
            background: #f5f5f5;
            text-align: center;
            cursor: pointer;
        }
        .dr-pay-tip {
            background: #fff3e0;
            padding: 10px;
            border-radius: 12px;
            font-size: 12px;
            color: #e67e22;
            margin: 12px 0;
        }
        .dr-pay-btn {
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
            transition: background 0.2s;
        }
        .dr-pay-btn:hover {
            background: #fb8c00;
        }
        .dr-close-pay {
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
        
        /* 代码块样式 */
        pre {
            background: #0d1117;
            color: #e6edf3;
            padding: 12px;
            border-radius: 8px;
            overflow-x: auto;
            margin: 8px 0;
        }
        code {
            font-family: 'SF Mono', Monaco, 'Cascadia Code', monospace;
            font-size: 13px;
        }
        :not(pre) > code {
            background: #e8e8ec;
            padding: 2px 6px;
            border-radius: 4px;
            color: #d73a49;
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
                <span>🤖 DrestryRobot 智能助手</span>
                <span id="quotaBadge" class="dr-quota-badge">免费 3/3 次</span>
            </div>
            <div class="dr-header-right">
                <span class="dr-arrow">▼</span>
            </div>
        </div>
        <div class="dr-chat-body">
            <div id="quotaWarning" class="dr-quota-warning" style="display: none;">
                ⚠️ 免费额度已用完，请点击下方按钮付费解锁
            </div>
            <div class="dr-chat-messages" id="chatMessages">
                <div class="dr-message dr-bot">
                    🤖 欢迎使用 DrestryRobot 专业助手！<br><br>
                    🎁 新用户赠送 <strong>3次免费提问</strong> 额度<br>
                    💰 3次用完后，仅需 <strong>¥1</strong> 即可永久解锁无限次使用<br><br>
                    开始提问吧！
                </div>
            </div>
            <div class="dr-chat-input-area" id="inputArea">
                <input type="text" class="dr-chat-input" id="chatInput" placeholder="输入机器人相关问题...">
                <button class="dr-chat-send" id="sendBtn">发送</button>
            </div>
        </div>
    </div>

    <div id="payModal" class="dr-pay-modal">
        <div class="dr-pay-content">
            <span class="dr-close-pay" id="closePayBtn">&times;</span>
            <h3>💰 永久解锁无限使用</h3>
            <div class="dr-pay-qr">
                <img src="https://drestryrobot.oss-cn-shanghai.aliyuncs.com/202605%20%E8%B5%9E%E8%B5%8F%E7%A0%81.png" alt="赞赏码">
            </div>
            <div class="dr-pay-tip">
                💡 扫码支付 <strong>¥1</strong> 永久解锁<br>
                ⚠️ 支付时请在「备注」中填写下方设备ID
            </div>
            <input type="text" id="deviceIdInput" class="dr-device-id" readonly onclick="this.select()">
            <button class="dr-pay-btn" id="submitPayBtn">✅ 我已支付，输入密码解锁</button>
            <div class="dr-disclaimer">
                ⚠️ 个人开发项目，服务可能随时下架，请谅解
            </div>
        </div>
    </div>

    <script>
    (function() {
        // ========== 配置 ==========
        var UNLOCK_PASSWORD = 'DrestryRobot';
        var FREE_QUOTA = 3;
        
        var STORAGE_USED = 'dr_used_quota';
        var STORAGE_DEVICE = 'dr_device_id';
        var STORAGE_UNLOCKED = 'dr_unlocked_v4';
        
        var DEEPSEEK_KEY = 'sk-c09347c4e827479a842a21acf5771103';
        
        function getDeviceId() {
            var id = localStorage.getItem(STORAGE_DEVICE);
            if (!id) {
                var timestamp = Date.now().toString(36);
                var random = Math.random().toString(36).substring(2, 10);
                id = 'DR_' + timestamp + '_' + random;
                localStorage.setItem(STORAGE_DEVICE, id);
            }
            return id;
        }
        
        function isUnlocked() {
            var list = JSON.parse(localStorage.getItem(STORAGE_UNLOCKED) || '[]');
            return list.indexOf(getDeviceId()) !== -1;
        }
        
        function markUnlocked() {
            var deviceId = getDeviceId();
            var list = JSON.parse(localStorage.getItem(STORAGE_UNLOCKED) || '[]');
            if (list.indexOf(deviceId) === -1) {
                list.push(deviceId);
                localStorage.setItem(STORAGE_UNLOCKED, JSON.stringify(list));
            }
        }
        
        function getUsedQuota() {
            if (isUnlocked()) return FREE_QUOTA;
            return parseInt(localStorage.getItem(STORAGE_USED) || '0');
        }
        
        function getRemainingQuota() {
            if (isUnlocked()) return Infinity;
            return Math.max(0, FREE_QUOTA - getUsedQuota());
        }
        
        function incrementUsedQuota() {
            if (isUnlocked()) return;
            var used = getUsedQuota() + 1;
            localStorage.setItem(STORAGE_USED, used.toString());
            updateUI();
        }
        
        function canAsk() {
            return getRemainingQuota() > 0;
        }
        
        function updateUI() {
            var badge = document.getElementById('quotaBadge');
            var warning = document.getElementById('quotaWarning');
            var input = document.getElementById('chatInput');
            var sendBtn = document.getElementById('sendBtn');
            var inputArea = document.getElementById('inputArea');
            
            if (isUnlocked()) {
                badge.innerHTML = '🌟 永久解锁';
                badge.className = 'dr-quota-badge unlocked';
                if (warning) warning.style.display = 'none';
                if (input) input.disabled = false;
                if (sendBtn) {
                    sendBtn.disabled = false;
                    sendBtn.innerHTML = '发送';
                    sendBtn.classList.remove('dr-unlock-btn');
                }
                removeLockOverlay(inputArea);
                return;
            }
            
            var remaining = getRemainingQuota();
            badge.innerHTML = '🎁 免费 ' + remaining + '/' + FREE_QUOTA + ' 次';
            
            if (remaining <= 0) {
                badge.className = 'dr-quota-badge none';
                if (warning) warning.style.display = 'block';
                if (input) input.disabled = true;
                if (sendBtn) {
                    sendBtn.disabled = false;
                    sendBtn.innerHTML = '🔓 付费解锁';
                    sendBtn.classList.add('dr-unlock-btn');
                }
                addLockOverlay(inputArea);
            } else {
                badge.className = remaining === 1 ? 'dr-quota-badge low' : 'dr-quota-badge';
                if (warning) warning.style.display = 'none';
                if (input) input.disabled = false;
                if (sendBtn) {
                    sendBtn.disabled = false;
                    sendBtn.innerHTML = '发送';
                    sendBtn.classList.remove('dr-unlock-btn');
                }
                removeLockOverlay(inputArea);
            }
        }
        
        function addLockOverlay(container) {
            if (!container || container.querySelector('.dr-lock-overlay')) return;
            var lock = document.createElement('div');
            lock.className = 'dr-lock-overlay';
            lock.innerHTML = '<div class="dr-lock-message">🔐 额度已用完，点击付费 ¥1 永久解锁</div>';
            lock.onclick = function() { showPayModal(); };
            container.appendChild(lock);
        }
        
        function removeLockOverlay(container) {
            if (!container) return;
            var overlay = container.querySelector('.dr-lock-overlay');
            if (overlay) overlay.remove();
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
                markUnlocked();
                updateUI();
                closePayModal();
                alert('✅ 解锁成功！现在可以无限次提问了。');
                var msgs = document.getElementById('chatMessages');
                var msg = document.createElement('div');
                msg.className = 'dr-message dr-bot';
                msg.innerHTML = '🎉 恭喜！您已永久解锁无限次提问权限！';
                msgs.appendChild(msg);
                msgs.scrollTop = msgs.scrollHeight;
            } else {
                alert('❌ 密码错误！请确认已付款后输入正确密码。');
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
            if (!canAsk()) {
                showPayModal();
                return;
            }
            
            var input = document.getElementById('chatInput');
            var message = input.value.trim();
            if (!message || isLoading) return;
            
            addMessage('user', message);
            input.value = '';
            
            if (!isUnlocked()) {
                incrementUsedQuota();
            }
            
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
                    widget.classList.toggle('dr-collapsed');
                });
            }
        }
        
        function bindEvents() {
            var sendBtn = document.getElementById('sendBtn');
            var input = document.getElementById('chatInput');
            var closePay = document.getElementById('closePayBtn');
            var submitPay = document.getElementById('submitPayBtn');
            
            bindCollapseEvent();
            bindScrollEvent();
            
            if (sendBtn) {
                sendBtn.addEventListener('click', function() {
                    if (!canAsk() && !isUnlocked()) {
                        showPayModal();
                    } else {
                        sendMessage();
                    }
                });
            }
            
            if (input) {
                input.addEventListener('keypress', function(e) {
                    if (e.key === 'Enter') {
                        e.preventDefault();
                        if (!canAsk() && !isUnlocked()) {
                            showPayModal();
                        } else {
                            sendMessage();
                        }
                    }
                });
            }
            
            if (closePay) {
                closePay.addEventListener('click', closePayModal);
            }
            
            if (submitPay) {
                submitPay.addEventListener('click', submitPayment);
            }
            
            var modal = document.getElementById('payModal');
            if (modal) {
                modal.addEventListener('click', function(e) {
                    if (e.target === modal) {
                        closePayModal();
                    }
                });
            }
        }
        
        function init() {
            bindEvents();
            updateUI();
            console.log('DrestryRobot 已启动 | 解锁密码: ' + UNLOCK_PASSWORD);
        }
        
        init();
    })();
    </script>