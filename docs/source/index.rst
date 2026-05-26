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

<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    <title>DrestryRobot 智能助手 - 专业版</title>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/highlight.js/lib/core.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/highlight.js/lib/languages/python.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/highlight.js/lib/languages/javascript.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/highlight.js/lib/languages/cpp.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/highlight.js/lib/languages/bash.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/highlight.js/styles/github-dark.css">
    
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
        align-items: center !important;
        user-select: none !important;
    }
    
    .dr-header-left {
        display: flex;
        align-items: center;
        gap: 8px;
        flex-wrap: wrap;
    }
    
    .dr-header-right {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .dr-quota-badge {
        background: #4caf50;
        color: white;
        font-size: 12px;
        border-radius: 20px;
        padding: 5px 12px;
        font-weight: normal;
        line-height: 1;
        display: inline-flex;
        align-items: center;
        height: 26px;
        box-sizing: border-box;
    }
    
    .dr-quota-badge.low { background: #ff9800; }
    .dr-quota-badge.none { background: #f44336; }
    
    .dr-admin-icon {
        cursor: pointer;
        font-size: 12px;
        padding: 5px 12px;
        border-radius: 20px;
        background: rgba(255,255,255,0.15);
        transition: background 0.2s;
        font-weight: normal;
        line-height: 1;
        display: inline-flex;
        align-items: center;
        height: 26px;
        box-sizing: border-box;
    }
    .dr-admin-icon:hover {
        background: rgba(255,255,255,0.3);
    }
    
    .dr-arrow {
        transition: transform 0.2s ease !important;
        display: inline-flex !important;
        align-items: center;
        font-size: 12px;
        height: 26px;
    }
    .dr-collapsed .dr-arrow { transform: rotate(180deg) !important; }
    
    .dr-admin-panel {
        display: none;
        background: white;
        border-top: 1px solid #e0e0e0;
        flex-direction: column;
        max-height: 280px;
        overflow: hidden;
    }
    .dr-admin-panel.active {
        display: flex;
    }
    .dr-admin-header {
        background: #1a1a2e;
        color: white;
        padding: 8px 12px;
        font-weight: bold;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 12px;
    }
    .dr-admin-list {
        max-height: 230px;
        overflow-y: auto;
        padding: 10px;
        background: #fafafa;
    }
    .dr-order-item {
        background: white;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
        border-left: 3px solid #ff9800;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .dr-order-device {
        font-family: monospace;
        font-size: 11px;
        background: #f0f0f0;
        padding: 4px 8px;
        border-radius: 6px;
        word-break: break-all;
        margin-bottom: 6px;
    }
    .dr-order-time {
        font-size: 10px;
        color: #999;
        margin: 4px 0;
    }
    .dr-unlock-btn-admin {
        background: #4caf50;
        color: white;
        border: none;
        border-radius: 20px;
        padding: 6px 12px;
        font-size: 11px;
        cursor: pointer;
        margin-top: 8px;
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
        box-sizing: border-box;
        font-size: 12px;
    }
    
    .dr-chat-body {
        display: flex !important;
        flex-direction: column !important;
        height: 480px !important;
        position: relative;
    }
    
    .dr-chat-messages {
        flex: 1 !important;
        overflow-y: auto !important;
        padding: 16px !important;
        background: #fafafa !important;
    }
    
    .dr-message {
        margin-bottom: 16px !important;
        padding: 10px 14px !important;
        border-radius: 12px !important;
        max-width: 85% !important;
        word-wrap: break-word !important;
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
        padding: 12px 16px !important;
        border: 1px solid #ccc !important;
        border-radius: 28px !important;
        outline: none !important;
        font-size: 15px !important;
    }
    
    .dr-chat-send {
        background: #1a1a2e !important;
        color: white !important;
        border: none !important;
        border-radius: 28px !important;
        padding: 0 22px !important;
        cursor: pointer !important;
        font-size: 14px !important;
        font-weight: 500 !important;
        transition: background 0.2s !important;
    }
    
    .dr-chat-send:disabled {
        background: #ccc !important;
        cursor: not-allowed;
    }
    
    .dr-unlock-btn { background: #ff9800 !important; }
    .dr-collapsed .dr-chat-body { display: none !important; }
    
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
        width: 350px;
        padding: 24px;
        text-align: center;
        position: relative;
    }
    .dr-donate-qr {
        width: 250px;
        height: 250px;
        margin: 20px auto;
        background: #f5f5f5;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 16px;
        overflow: hidden;
    }
    .dr-donate-qr img {
        width: 100%;
        height: auto;
    }
    .dr-username-input {
        width: 100%;
        padding: 12px;
        border: 1px solid #ddd;
        border-radius: 12px;
        margin: 12px 0;
        font-size: 16px;
        box-sizing: border-box;
        font-family: monospace;
        background: #f5f5f5;
    }
    .dr-tip {
        background: #fff3e0;
        padding: 12px;
        border-radius: 12px;
        font-size: 13px;
        color: #e67e22;
        margin: 12px 0;
    }
    .dr-check-payment {
        background: #ff9800;
        color: white;
        border: none;
        border-radius: 28px;
        padding: 12px 24px;
        width: 100%;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        margin-top: 12px;
    }
    .dr-close-modal {
        position: absolute;
        top: 12px;
        right: 16px;
        font-size: 24px;
        cursor: pointer;
        color: #999;
    }
    .dr-disclaimer {
        font-size: 11px;
        color: #999;
        margin-top: 16px;
        padding-top: 12px;
        border-top: 1px solid #eee;
        text-align: center;
    }
    
    .dr-quota-warning {
        background: #fff3e0;
        padding: 8px 12px;
        font-size: 12px;
        text-align: center;
        border-bottom: 1px solid #ffe0b2;
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
    }
    mjx-container {
        overflow-x: auto !important;
        overflow-y: hidden !important;
        margin: 8px 0 !important;
    }
    </style>
</head>
<body>
<div id="dr-chat-widget" class="dr-chat-container dr-collapsed">
    <div class="dr-chat-header">
        <div class="dr-header-left">
            <span>🤖 DrestryRobot 智能助手</span>
            <span id="quotaBadge" class="dr-quota-badge">免费 3/3 次</span>
        </div>
        <div class="dr-header-right">
            <span class="dr-admin-icon" id="adminToggle">⚙️ 管理</span>
            <span class="dr-arrow">▼</span>
        </div>
    </div>
    <div class="dr-chat-body">
        <div id="quotaWarning" class="dr-quota-warning" style="display:none;">
            ⚠️ 免费额度已用完，请付费 ¥1 解锁无限次使用
        </div>
        
        <div id="adminPanel" class="dr-admin-panel">
            <div class="dr-admin-header">
                <span>🔐 待解锁订单</span>
                <button class="dr-refresh-btn" id="refreshOrdersBtn">刷新</button>
            </div>
            <div style="padding: 8px 10px 0 10px;">
                <input type="text" id="searchOrderInput" class="search-input" placeholder="🔍 搜索设备ID">
            </div>
            <div class="dr-admin-list" id="orderList">
                <div style="text-align:center; padding:20px; color:#999;">加载中...</div>
            </div>
        </div>
        
        <div class="dr-chat-messages" id="dr-chat-messages">
            <div class="dr-message dr-bot">🤖 欢迎使用 DrestryRobot 专业助手！<br><br>🎁 新用户赠送 <strong>3次免费提问</strong> 额度<br>💰 3次用完后，仅需 <strong>¥1</strong> 即可永久解锁无限次使用<br><br>开始提问吧！</div>
        </div>
        <div class="dr-chat-input-area" id="input-area">
            <input type="text" class="dr-chat-input" id="dr-chat-input" placeholder="输入机器人相关问题...">
            <button class="dr-chat-send" id="dr-chat-send">发送</button>
        </div>
    </div>
</div>

<div id="donateModal" class="dr-donate-modal">
    <div class="dr-donate-content">
        <span class="dr-close-modal" id="closeModalBtn">&times;</span>
        <h3>💰 永久解锁无限使用</h3>
        <div class="dr-donate-qr">
            <img src="https://drestryrobot.oss-cn-shanghai.aliyuncs.com/202605%20%E8%B5%9E%E8%B5%8F%E7%A0%81.png" alt="赞赏码" style="width:100%">
        </div>
        <div class="dr-tip">
            💡 扫码支付 <strong>¥1</strong> 永久解锁无限次提问<br>
            ⚠️ <strong>支付时必须在「备注」中填写以下设备ID：</strong>
            <input type="text" id="deviceIdDisplay" class="dr-username-input" readonly onclick="this.select()" style="background:#f0f0f0; font-size:12px;">
            填写错误将无法解锁！
        </div>
        <button class="dr-check-payment" id="submitPaymentBtn">✅ 我已支付，申请解锁</button>
        <div class="dr-disclaimer">
            ⚠️ 个人开发项目，服务可能随时下架，请谅解
        </div>
    </div>
</div>

<script>
(function() {
    var ADMIN_PASSWORD = '666666';
    var UNLOCK_PRICE = 1;
    var FREE_QUOTA = 3;
    
    var STORAGE_USED_QUOTA = 'drestryrobot_used_quota';
    var STORAGE_PENDING = 'drestryrobot_pending_payments';
    var STORAGE_DEVICE_ID = 'drestryrobot_device_id';
    var STORAGE_UNLOCKED_DEVICES = 'drestryrobot_unlocked_devices_v2';
    
    var DEEPSEEK_KEY = 'sk-c09347c4e827479a842a21acf5771103';
    
    function getDeviceId() {
        var deviceId = localStorage.getItem(STORAGE_DEVICE_ID);
        if (!deviceId) {
            var timestamp = Date.now().toString(36);
            var random = Math.random().toString(36).substring(2, 15);
            deviceId = 'DR_' + timestamp + '_' + random;
            localStorage.setItem(STORAGE_DEVICE_ID, deviceId);
        }
        return deviceId;
    }
    
    function isDeviceUnlocked() {
        var deviceId = getDeviceId();
        var unlockedDevices = JSON.parse(localStorage.getItem(STORAGE_UNLOCKED_DEVICES) || '[]');
        return unlockedDevices.indexOf(deviceId) !== -1;
    }
    
    function markDeviceUnlocked(deviceId) {
        var unlockedDevices = JSON.parse(localStorage.getItem(STORAGE_UNLOCKED_DEVICES) || '[]');
        if (unlockedDevices.indexOf(deviceId) === -1) {
            unlockedDevices.push(deviceId);
            localStorage.setItem(STORAGE_UNLOCKED_DEVICES, JSON.stringify(unlockedDevices));
        }
    }
    
    function isPermanentlyUnlocked() {
        return isDeviceUnlocked();
    }
    
    function getUsedQuota() {
        if (isPermanentlyUnlocked()) return FREE_QUOTA;
        return parseInt(localStorage.getItem(STORAGE_USED_QUOTA) || '0');
    }
    
    function getRemainingQuota() {
        if (isPermanentlyUnlocked()) return Infinity;
        return Math.max(0, FREE_QUOTA - getUsedQuota());
    }
    
    function incrementUsedQuota() {
        if (isPermanentlyUnlocked()) return;
        var current = getUsedQuota();
        localStorage.setItem(STORAGE_USED_QUOTA, (current + 1).toString());
        updateQuotaUI();
    }
    
    function canAskQuestion() {
        return getRemainingQuota() > 0;
    }
    
    function updateQuotaUI() {
        var quotaBadge = document.getElementById('quotaBadge');
        var quotaWarning = document.getElementById('quotaWarning');
        
        if (isPermanentlyUnlocked()) {
            quotaBadge.innerHTML = '🌟 永久解锁';
            quotaBadge.className = 'dr-quota-badge';
            quotaBadge.style.background = '#9c27b0';
            if (quotaWarning) quotaWarning.style.display = 'none';
            var input = document.getElementById('dr-chat-input');
            var sendBtn = document.getElementById('dr-chat-send');
            if (input) input.disabled = false;
            if (sendBtn) {
                sendBtn.disabled = false;
                sendBtn.innerHTML = '发送';
                sendBtn.classList.remove('dr-unlock-btn');
            }
            removeLockOverlay();
            return;
        }
        
        var remaining = getRemainingQuota();
        quotaBadge.innerHTML = '🎁 免费 ' + remaining + '/' + FREE_QUOTA + ' 次';
        
        if (remaining <= 0) {
            quotaBadge.className = 'dr-quota-badge none';
            if (quotaWarning) quotaWarning.style.display = 'block';
            var input = document.getElementById('dr-chat-input');
            var sendBtn = document.getElementById('dr-chat-send');
            if (input) input.disabled = true;
            if (sendBtn) {
                sendBtn.disabled = false;
                sendBtn.innerHTML = '💰 付费解锁';
                sendBtn.classList.add('dr-unlock-btn');
            }
            addLockOverlay();
        } else {
            quotaBadge.className = remaining <= 1 ? 'dr-quota-badge low' : 'dr-quota-badge';
            if (quotaWarning) quotaWarning.style.display = 'none';
            var input = document.getElementById('dr-chat-input');
            var sendBtn = document.getElementById('dr-chat-send');
            if (input) input.disabled = false;
            if (sendBtn) {
                sendBtn.disabled = false;
                sendBtn.innerHTML = '发送';
                sendBtn.classList.remove('dr-unlock-btn');
            }
            removeLockOverlay();
        }
    }
    
    function addLockOverlay() {
        var inputArea = document.getElementById('input-area');
        if (inputArea && !inputArea.querySelector('.dr-lock-overlay')) {
            var lockDiv = document.createElement('div');
            lockDiv.className = 'dr-lock-overlay';
            lockDiv.innerHTML = '<div class="dr-lock-message">💰 额度已用完，点击付费 ¥1 永久解锁</div>';
            lockDiv.querySelector('.dr-lock-message').addEventListener('click', function() { showDonateModal(); });
            inputArea.style.position = 'relative';
            inputArea.appendChild(lockDiv);
        }
    }
    
    function removeLockOverlay() {
        var inputArea = document.getElementById('input-area');
        var overlay = inputArea ? inputArea.querySelector('.dr-lock-overlay') : null;
        if (overlay) overlay.remove();
    }
    
    function showDonateModal() {
        var deviceId = getDeviceId();
        document.getElementById('deviceIdDisplay').value = deviceId;
        document.getElementById('donateModal').classList.add('active');
    }
    
    function closeDonateModal() {
        document.getElementById('donateModal').classList.remove('active');
    }
    
    function submitPaymentInfo() {
        var deviceId = getDeviceId();
        
        if (isPermanentlyUnlocked()) {
            alert('您已经永久解锁了，可以直接使用！');
            closeDonateModal();
            return;
        }
        
        var pending = JSON.parse(localStorage.getItem(STORAGE_PENDING) || '[]');
        var existing = null;
        for (var i = 0; i < pending.length; i++) {
            if (pending[i].deviceId === deviceId && pending[i].status === 'pending') {
                existing = pending[i];
                break;
            }
        }
        if (existing) {
            alert('您已提交过申请，请等待管理员处理');
            closeDonateModal();
            return;
        }
        
        pending.push({
            deviceId: deviceId,
            time: new Date().toISOString(),
            status: 'pending',
            amount: UNLOCK_PRICE
        });
        localStorage.setItem(STORAGE_PENDING, JSON.stringify(pending));
        
        alert('申请已提交！\n\n设备ID：' + deviceId + '\n金额：¥' + UNLOCK_PRICE + '\n\n请确保在支付备注中填写了正确的设备ID，管理员确认后会为您永久解锁。');
        closeDonateModal();
    }
    
    var adminAuthenticated = false;
    var adminPanelOpen = false;
    
    function toggleAdminPanel() {
        var panel = document.getElementById('adminPanel');
        if (adminPanelOpen) {
            panel.classList.remove('active');
            adminPanelOpen = false;
        } else {
            if (!adminAuthenticated) {
                var pwd = prompt('请输入管理员密码：');
                if (pwd !== ADMIN_PASSWORD) {
                    alert('密码错误');
                    return;
                }
                adminAuthenticated = true;
            }
            panel.classList.add('active');
            adminPanelOpen = true;
            loadPendingOrders();
        }
    }
    
    function loadPendingOrders() {
        var pending = JSON.parse(localStorage.getItem(STORAGE_PENDING) || '[]');
        var searchInput = document.getElementById('searchOrderInput');
        var searchTerm = searchInput ? searchInput.value.toLowerCase() : '';
        var orderListDiv = document.getElementById('orderList');
        
        var filtered = [];
        for (var i = 0; i < pending.length; i++) {
            var order = pending[i];
            if (order.status === 'pending' && (searchTerm === '' || order.deviceId.toLowerCase().indexOf(searchTerm) !== -1)) {
                filtered.push(order);
            }
        }
        
        if (filtered.length === 0) {
            orderListDiv.innerHTML = '<div style="text-align:center; padding:20px; color:#999;">暂无待处理订单</div>';
            return;
        }
        
        orderListDiv.innerHTML = '';
        for (var j = 0; j < filtered.length; j++) {
            var order = filtered[j];
            var orderDiv = document.createElement('div');
            orderDiv.className = 'dr-order-item';
            orderDiv.innerHTML = '<div class="dr-order-device">🖥️ ' + escapeHtml(order.deviceId) + '</div>' +
                '<div class="dr-order-time">⏰ ' + new Date(order.time).toLocaleString() + '</div>' +
                '<div class="dr-order-time">💰 ¥' + order.amount + '</div>' +
                '<button class="dr-unlock-btn-admin" data-deviceid="' + escapeHtml(order.deviceId) + '">✅ 确认已收款，永久解锁</button>';
            orderListDiv.appendChild(orderDiv);
            var btn = orderDiv.querySelector('.dr-unlock-btn-admin');
            btn.addEventListener('click', (function(did) {
                return function() { confirmUnlock(did); };
            })(order.deviceId));
        }
    }
    
    function confirmUnlock(deviceId) {
        if (!confirm('确认设备 "' + deviceId + '" 已完成 ¥1 支付并为其永久解锁吗？')) return;
        
        var pending = JSON.parse(localStorage.getItem(STORAGE_PENDING) || '[]');
        var orderIndex = -1;
        for (var i = 0; i < pending.length; i++) {
            if (pending[i].deviceId === deviceId && pending[i].status === 'pending') {
                orderIndex = i;
                break;
            }
        }
        if (orderIndex !== -1) {
            pending.splice(orderIndex, 1);
            localStorage.setItem(STORAGE_PENDING, JSON.stringify(pending));
        }
        
        markDeviceUnlocked(deviceId);
        updateQuotaUI();
        
        if (getDeviceId() === deviceId) {
            alert('✅ 您的设备已永久解锁！现在可以无限次提问了。');
            var messagesDiv = document.getElementById('dr-chat-messages');
            var successMsg = document.createElement('div');
            successMsg.className = 'dr-message dr-bot';
            successMsg.innerHTML = '🎉 恭喜！您已永久解锁无限次提问权限！';
            messagesDiv.appendChild(successMsg);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        } else {
            alert('✅ 设备 ' + deviceId + ' 已永久解锁！');
        }
        
        loadPendingOrders();
    }
    
    function escapeHtml(str) {
        return str.replace(/[&<>]/g, function(m) {
            if (m === '&') return '&amp;';
            if (m === '<') return '&lt;';
            if (m === '>') return '&gt;';
            return m;
        });
    }
    
    var isLoading = false;
    var currentStreamingDiv = null;
    var streamingContent = '';
    
    if (typeof marked !== 'undefined') {
        marked.setOptions({
            highlight: function(code, lang) {
                if (lang && hljs && hljs.getLanguage(lang)) {
                    try {
                        return hljs.highlight(code, { language: lang }).value;
                    } catch (e) {}
                }
                return code;
            }
        });
    }
    
    function markdownToHtml(text) {
        if (!text) return '';
        var latexBlocks = [];
        var latexInlines = [];
        text = text.replace(/\$\$([\s\S]*?)\$\$/g, function(match, formula) {
            var idx = latexBlocks.length;
            latexBlocks.push(formula);
            return '@@LATEX_BLOCK_' + idx + '@@';
        });
        text = text.replace(/\$([^\$\n]+?)\$/g, function(match, formula) {
            var idx = latexInlines.length;
            latexInlines.push(formula);
            return '@@LATEX_INLINE_' + idx + '@@';
        });
        var html = marked.parse(text, { mangle: false, headerIds: false });
        html = html.replace(/@@LATEX_BLOCK_(\d+)@@/g, function(match, idx) {
            return '$$' + latexBlocks[parseInt(idx)] + '$$';
        });
        html = html.replace(/@@LATEX_INLINE_(\d+)@@/g, function(match, idx) {
            return '$' + latexInlines[parseInt(idx)] + '$';
        });
        return html;
    }
    
    function addMessage(role, content) {
        var messagesDiv = document.getElementById('dr-chat-messages');
        var div = document.createElement('div');
        div.className = 'dr-message dr-' + role;
        if (role === 'user') {
            div.textContent = content;
        } else {
            div.innerHTML = markdownToHtml(content);
            if (typeof hljs !== 'undefined') {
                var codeBlocks = div.querySelectorAll('pre code');
                for (var i = 0; i < codeBlocks.length; i++) {
                    hljs.highlightElement(codeBlocks[i]);
                }
            }
        }
        messagesDiv.appendChild(div);
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
        if (role === 'bot' && window.MathJax) {
            MathJax.typesetPromise([div]).catch(function(e) { console.warn(e); });
        }
    }
    
    function addStreamingMessage() {
        currentStreamingDiv = document.createElement('div');
        currentStreamingDiv.className = 'dr-message dr-bot';
        currentStreamingDiv.innerHTML = '<span class="dr-typing-cursor"></span>';
        document.getElementById('dr-chat-messages').appendChild(currentStreamingDiv);
        streamingContent = '';
    }
    
    function updateStreamingContent(newChunk) {
        if (!currentStreamingDiv) return;
        streamingContent += newChunk;
        var rendered = markdownToHtml(streamingContent);
        currentStreamingDiv.innerHTML = rendered + '<span class="dr-typing-cursor"></span>';
        var msgsDiv = document.getElementById('dr-chat-messages');
        msgsDiv.scrollTop = msgsDiv.scrollHeight;
    }
    
    function finishStreamingMessage() {
        if (!currentStreamingDiv) return;
        var rendered = markdownToHtml(streamingContent);
        currentStreamingDiv.innerHTML = rendered;
        if (window.MathJax) {
            MathJax.typesetPromise([currentStreamingDiv]).catch(function(e) { console.warn(e); });
        }
        if (typeof hljs !== 'undefined') {
            var codeBlocks = currentStreamingDiv.querySelectorAll('pre code');
            for (var i = 0; i < codeBlocks.length; i++) {
                hljs.highlightElement(codeBlocks[i]);
            }
        }
        currentStreamingDiv = null;
        streamingContent = '';
    }
    
    async function sendMessage() {
        if (!canAskQuestion()) {
            showDonateModal();
            return;
        }
        
        var input = document.getElementById('dr-chat-input');
        var message = input.value.trim();
        if (!message || isLoading) return;
        
        addMessage('user', message);
        input.value = '';
        
        if (!isPermanentlyUnlocked()) {
            incrementUsedQuota();
        }
        
        isLoading = true;
        addStreamingMessage();
        
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
                        { role: 'system', content: '你是 DrestryRobot 知识库的机器人专家。回答应严谨、深刻、偏重机器人学理论。使用 Markdown 格式：用 ## 标题，用 - 列表，用 $...$ 或 $$...$$ 公式。代码块用 ```language 标记。' },
                        { role: 'user', content: message }
                    ],
                    temperature: 0.3,
                    stream: true
                })
            });
            
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
                            var chunk = parsed.choices[0] && parsed.choices[0].delta ? parsed.choices[0].delta.content : '';
                            if (chunk) updateStreamingContent(chunk);
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
            addMessage('bot', '调用失败：' + error.message);
        }
        isLoading = false;
    }
    
    function bindEvents() {
        var header = document.querySelector('.dr-chat-header');
        var sendBtn = document.getElementById('dr-chat-send');
        var input = document.getElementById('dr-chat-input');
        var adminToggle = document.getElementById('adminToggle');
        var refreshBtn = document.getElementById('refreshOrdersBtn');
        var closeModalBtn = document.getElementById('closeModalBtn');
        var submitPaymentBtn = document.getElementById('submitPaymentBtn');
        var searchInput = document.getElementById('searchOrderInput');
        
        if (header) {
            header.addEventListener('click', function(e) {
                if (e.target === adminToggle || (adminToggle && adminToggle.contains(e.target))) return;
                document.getElementById('dr-chat-widget').classList.toggle('dr-collapsed');
            });
        }
        
        if (adminToggle) {
            adminToggle.addEventListener('click', function(e) {
                e.stopPropagation();
                toggleAdminPanel();
            });
        }
        
        if (refreshBtn) {
            refreshBtn.addEventListener('click', function() { loadPendingOrders(); });
        }
        
        if (closeModalBtn) {
            closeModalBtn.addEventListener('click', function() { closeDonateModal(); });
        }
        
        if (submitPaymentBtn) {
            submitPaymentBtn.addEventListener('click', function() { submitPaymentInfo(); });
        }
        
        if (sendBtn) {
            sendBtn.addEventListener('click', function() {
                if (!canAskQuestion() && !isPermanentlyUnlocked()) {
                    showDonateModal();
                } else {
                    sendMessage();
                }
            });
        }
        
        if (input) {
            input.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    if (!canAskQuestion() && !isPermanentlyUnlocked()) {
                        showDonateModal();
                    } else {
                        sendMessage();
                    }
                }
            });
        }
        
        if (searchInput) {
            searchInput.addEventListener('input', function() { loadPendingOrders(); });
        }
    }
    
    function init() {
        bindEvents();
        updateQuotaUI();
        console.log('DrestryRobot 已启动 | 管理员密码: 666666');
    }
    
    window.showDonateModal = showDonateModal;
    window.closeDonateModal = closeDonateModal;
    window.submitPaymentInfo = submitPaymentInfo;
    window.confirmUnlock = confirmUnlock;
    window.loadPendingOrders = loadPendingOrders;
    
    init();
})();
</script>
</body>
</html>