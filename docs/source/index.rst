🔥 DrestryRobot
=====================================
.. raw:: html

   <style>
       .spinner {
           width: 18px;
           height: 18px;
           border: 2px solid #ccc;
           border-top-color: #0366d6;
           border-radius: 50%;
           animation: spin 0.8s linear infinite;
       }
       @keyframes spin {
           to { transform: rotate(360deg); }
       }
       @media (max-width: 600px) {
           .full { display: none; }
           .short { display: inline; }
       }
       @media (min-width: 601px) {
           .full { display: inline; }
           .short { display: none; }
       }
   </style>

   <div style="text-align: center; margin: 20px 0;">
       <div id="loading" style="display: flex; align-items: center; justify-content: center; gap: 8px;"><div class="spinner"></div> 数据加载中...</div>
       <div id="counter" style="display: none;">
           <span id="vercount_container_site_pv" style="display: none;">
               <span class="full">🌐 本站总访问量：</span><span class="short">🌐 访问量：</span>
               <span id="vercount_value_site_pv">0</span> 次
           </span>
           &nbsp;|&nbsp;
           <span id="vercount_container_site_uv" style="display: none;">
               <span class="full">👥 本站总访客数：</span><span class="short">👥 访客数：</span>
               <span id="vercount_value_site_uv">0</span> 人
           </span>
       </div>
   </div>

   <script>
       document.head.appendChild(Object.assign(document.createElement('script'), { src: 'https://vercount.one/js', defer: true }));
       let timer = setInterval(() => {
           let pv = document.getElementById('vercount_container_site_pv');
           if (pv && pv.style.display === 'inline') {
               document.getElementById('loading').style.display = 'none';
               document.getElementById('counter').style.display = 'block';
               clearInterval(timer);
           }
       }, 100);
   </script>

🧩 基本介绍
-------------
DrestryRobot是一个机器人开发知识库，其涵盖了机器人开发所需要用到的各类技术知识和软件工具。

🎯 核心理念
-------------
DrestryRobot由Dream、Struggle、Youth和Robot组成，是一个热爱于机器人开发、有梦想、敢奋斗、充满青春活力的团队。

⚖️ 编撰原则
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
   :caption: 📚 内容目录
   :glob:

   *

📸 分享有奖
-------------

.. raw:: html

    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            .drestry-reward {
                width: 100%;
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                padding-bottom: 20px;
            }

            .reward-inner {
                padding: 0;
            }

            .upload-zone {
                background: #f5f5f7;
                border: 2px dashed #d4d4d8;
                border-radius: 24px;
                cursor: pointer;
                transition: all 0.25s ease;
                position: relative;
                width: 100%;
                padding-top: 56.25%;
                overflow: hidden;
                box-shadow: 0 1px 2px rgba(0, 0, 0, 0.03);
            }

            .upload-zone:hover {
                border-color: #a1a1aa;
                background: #eaeaef;
            }

            .upload-inner {
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }

            .upload-content {
                text-align: center;
                z-index: 2;
                transition: opacity 0.3s ease;
                pointer-events: none;
            }

            .upload-icon {
                font-size: 48px;
                margin-bottom: 12px;
            }

            .upload-text {
                color: #3f3f46;
                font-weight: 500;
                font-size: 1rem;
                margin-bottom: 8px;
            }

            .upload-desc {
                color: #71717a;
                font-size: 0.85rem;
                line-height: 1.4;
            }

            .upload-desc .domain {
                color: #71717a;
                font-weight: 500;
            }

            .preview-container {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                display: none;
                justify-content: center;
                align-items: center;
                z-index: 1;
                background: #f5f5f7;
            }

            .preview-img {
                max-width: 100%;
                max-height: 100%;
                width: auto;
                height: auto;
                object-fit: contain;
                display: block;
            }

            .action-btn {
                position: absolute;
                top: 12px;
                right: 12px;
                width: 28px;
                height: 28px;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                cursor: pointer;
                z-index: 15;
                backdrop-filter: blur(4px);
                border: 1px solid rgba(255, 255, 255, 0.4);
                transition: all 0.2s ease;
                font-size: 16px;
                font-weight: 600;
            }

            .action-btn span {
                line-height: 1;
                display: block;
                margin-top: -1px;
            }

            .copy-btn {
                background: #10b981;
                color: white;
            }

            .copy-btn:hover {
                background: #059669;
            }

            .clear-btn {
                background: #ef4444;
                color: white;
            }

            .clear-btn:hover {
                background: #dc2626;
            }

            .upload-zone.has-preview .action-btn {
                opacity: 1;
                visibility: visible;
            }

            .upload-zone:not(.has-preview) .action-btn {
                opacity: 1;
                visibility: visible;
            }

            .toast {
                position: fixed;
                bottom: 30px;
                left: 50%;
                transform: translateX(-50%) translateY(100px);
                background: rgba(0, 0, 0, 0.8);
                color: white;
                padding: 10px 20px;
                border-radius: 40px;
                font-size: 14px;
                font-weight: 500;
                z-index: 1000;
                opacity: 0;
                transition: all 0.3s ease;
                backdrop-filter: blur(8px);
                white-space: nowrap;
                pointer-events: none;
            }

            .toast.show {
                transform: translateX(-50%) translateY(0);
                opacity: 1;
            }

            /* ========== 状态栏 - 固定高度，内容固定宽度 ========== */
            .status-bar {
                position: absolute;
                bottom: 0;
                left: 0;
                right: 0;
                height: 44px;
                backdrop-filter: blur(16px);
                -webkit-backdrop-filter: blur(16px);
                border-radius: 0 0 22px 22px;
                border-top: 1px solid rgba(0, 0, 0, 0.06);
                z-index: 10;
                transition: background-color 0.2s ease;
                display: flex;
                align-items: center;
                justify-content: center;
            }

            .upload-zone:not(.has-preview) .status-bar {
                display: none;
            }

            .upload-zone.has-preview .status-bar {
                display: flex;
            }

            /* 关键修复：所有状态内容使用固定最小宽度，确保位置一致 */
            .status-content {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                gap: 6px;
                font-size: 0.875rem;
                font-weight: 500;
                color: white;
                white-space: nowrap;
                min-width: 160px;
                text-align: center;
                line-height: 1.4;
            }

            /* 不同状态背景色 */
            .status-bar.default {
                background: rgba(0, 0, 0, 0.6);
            }

            .status-bar.loading {
                background: #71717a;
            }

            .status-bar.success {
                background: #10b981;
            }

            .status-bar.error {
                background: #ef4444;
            }

            /* 简单淡入动画 - 不改变尺寸 */
            @keyframes gentleFade {
                0% { opacity: 0; }
                100% { opacity: 1; }
            }

            .status-content {
                animation: gentleFade 0.2s ease-out;
            }

            .spinner-small {
                display: inline-block;
                width: 14px;
                height: 14px;
                border: 2px solid rgba(255, 255, 255, 0.3);
                border-top-color: white;
                border-radius: 50%;
                animation: spin 0.8s linear infinite;
            }

            @keyframes spin {
                to { transform: rotate(360deg); }
            }

            .upload-zone.has-preview .upload-content {
                opacity: 0;
                visibility: hidden;
            }

            .upload-zone.has-preview .preview-container {
                display: flex;
            }

            .reward-card {
                background: #f5f5f7;
                border: 1px solid #e4e4e9;
                border-radius: 24px;
                padding: 24px;
                margin-top: 20px;
                text-align: center;
                animation: celebrate 0.5s ease-out;
                box-shadow: 0 1px 2px rgba(0, 0, 0, 0.03);
                transition: box-shadow 0.2s ease;
            }

            .reward-card:hover {
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            }

            @keyframes celebrate {
                0% { opacity: 0; transform: scale(0.95); }
                50% { opacity: 1; transform: scale(1.02); }
                100% { opacity: 1; transform: scale(1); }
            }

            .confetti {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                pointer-events: none;
                z-index: 999;
                overflow: hidden;
            }

            .confetti-piece {
                position: absolute;
                width: 10px;
                height: 20px;
                background: linear-gradient(135deg, #ffd700, #ffaa00);
                opacity: 0.8;
                animation: fall 3s linear forwards;
            }

            @keyframes fall {
                0% { transform: translateY(-100px) rotate(0deg); opacity: 1; }
                100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
            }

            .reward-card-title {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 8px;
                color: #3f3f46;
                font-size: 1.1rem;
                font-weight: 600;
                margin-bottom: 16px;
            }

            .reward-card-title span {
                font-size: 1.35rem;
            }

            .qr-wrapper {
                background: #ffffff;
                border-radius: 20px;
                padding: 12px;
                display: inline-block;
                margin-bottom: 12px;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
                transition: box-shadow 0.2s ease;
            }

            .qr-wrapper:hover {
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            }

            .qr-img-reward {
                width: 140px;
                height: 140px;
                display: block;
            }

            .qr-img-reward img {
                width: 100%;
                height: 100%;
                object-fit: contain;
            }

            .reward-card-desc {
                color: #71717a;
                font-size: 0.8rem;
            }

            @media (max-width: 560px) {
                .drestry-reward {
                    padding-bottom: 16px;
                }
                .upload-icon {
                    font-size: 40px;
                }
                .upload-text {
                    font-size: 0.9rem;
                }
                .upload-desc {
                    font-size: 0.75rem;
                }
                .status-bar {
                    height: 40px;
                }
                .status-content {
                    font-size: 0.75rem;
                    min-width: 130px;
                }
                .action-btn {
                    top: 8px;
                    right: 8px;
                    width: 26px;
                    height: 26px;
                    font-size: 14px;
                }
                .qr-img-reward {
                    width: 110px;
                    height: 110px;
                }
                .reward-card {
                    padding: 18px;
                }
                .toast {
                    font-size: 12px;
                    padding: 8px 16px;
                    bottom: 20px;
                }
            }
        </style>
    </head>
    <body>
        <div class="drestry-reward">
            <div class="reward-inner">
                <div class="upload-zone" id="uploadZone">
                    <div class="action-btn" id="actionBtn">
                        <span>✓</span>
                    </div>

                    <div class="upload-inner">
                        <div class="upload-content">
                            <div class="upload-icon">📸</div>
                            <div class="upload-text">点击上传截图</div>
                            <div class="upload-desc">
                                上传包含 <span class="domain">drestryrobot.readthedocs.io</span> 的分享截图有奖
                            </div>
                        </div>

                        <div class="preview-container" id="previewContainer">
                            <img class="preview-img" id="previewImg" alt="预览">
                        </div>
                    </div>

                    <div class="status-bar default" id="statusBar">
                        <div class="status-content" id="statusContent">
                            <span>🖱️ 点击更换图片</span>
                        </div>
                    </div>

                    <input type="file" id="fileInput" accept="image/*" style="display: none;">
                </div>

                <div class="reward-card" id="rewardCard" style="display: none;">
                    <div class="reward-card-title">
                        <span>🎉</span> 验证成功，领奖 <span>🧧</span>
                    </div>
                    <div class="qr-wrapper">
                        <div class="qr-img-reward">
                            <img id="rewardQr" src="https://drestryrobot.oss-cn-shanghai.aliyuncs.com/202606%20%E5%BE%AE%E4%BF%A1%E4%BA%8C%E7%BB%B4%E7%A0%81.png" alt="二维码">
                        </div>
                    </div>
                    <div class="reward-card-desc">📱 微信扫一扫领取红包</div>
                </div>
            </div>
        </div>

        <div class="toast" id="toast">✅ 网址复制成功！快去分享吧！</div>

        <script>
            (function() {
                const REQUIRED_DOMAIN = "drestryrobot.readthedocs.io";
                const COPY_URL = "https://drestryrobot.readthedocs.io";
                
                const uploadZone = document.getElementById('uploadZone');
                const fileInput = document.getElementById('fileInput');
                const previewImg = document.getElementById('previewImg');
                const statusBar = document.getElementById('statusBar');
                const statusContent = document.getElementById('statusContent');
                const rewardCard = document.getElementById('rewardCard');
                const actionBtn = document.getElementById('actionBtn');
                const toast = document.getElementById('toast');
                
                function showToast(msg) {
                    toast.textContent = msg;
                    toast.classList.add('show');
                    setTimeout(() => {
                        toast.classList.remove('show');
                    }, 2000);
                }
                
                async function copyLink() {
                    try {
                        await navigator.clipboard.writeText(COPY_URL);
                        showToast('✅ 网址复制成功！快去分享吧！');
                    } catch (err) {
                        const textarea = document.createElement('textarea');
                        textarea.value = COPY_URL;
                        document.body.appendChild(textarea);
                        textarea.select();
                        document.execCommand('copy');
                        document.body.removeChild(textarea);
                        showToast('✅ 网址复制成功！快去分享吧！');
                    }
                }
                
                function clearImage() {
                    uploadZone.classList.remove('has-preview');
                    previewImg.src = '';
                    fileInput.value = '';
                    rewardCard.style.display = 'none';
                    statusBar.className = 'status-bar default';
                    statusContent.innerHTML = '<span>🖱️ 点击更换图片</span>';
                    actionBtn.className = 'action-btn copy-btn';
                    actionBtn.innerHTML = '<span>✓</span>';
                }
                
                function updateButtonStyle() {
                    if (uploadZone.classList.contains('has-preview')) {
                        actionBtn.className = 'action-btn clear-btn';
                        actionBtn.innerHTML = '<span>✗</span>';
                    } else {
                        actionBtn.className = 'action-btn copy-btn';
                        actionBtn.innerHTML = '<span>✓</span>';
                    }
                }
                
                function updateStatus(type, message, iconHtml) {
                    statusBar.className = 'status-bar ' + type;
                    // 所有消息统一使用相同结构，位置保持一致
                    statusContent.innerHTML = iconHtml + ' ' + message;
                }
                
                actionBtn.addEventListener('click', (e) => {
                    e.stopPropagation();
                    if (uploadZone.classList.contains('has-preview')) {
                        clearImage();
                    } else {
                        copyLink();
                    }
                });
                
                uploadZone.addEventListener('click', (e) => {
                    if (e.target === actionBtn || e.target.parentNode === actionBtn) return;
                    fileInput.click();
                });
                
                uploadZone.addEventListener('dragover', (e) => {
                    e.preventDefault();
                    uploadZone.style.borderColor = '#a1a1aa';
                });
                uploadZone.addEventListener('dragleave', () => {
                    uploadZone.style.borderColor = '#d4d4d8';
                });
                uploadZone.addEventListener('drop', (e) => {
                    e.preventDefault();
                    uploadZone.style.borderColor = '#d4d4d8';
                    const file = e.dataTransfer.files[0];
                    if (file && file.type.startsWith('image/')) handleFile(file);
                    else {
                        updateStatus('error', '请上传图片', '<span>✗</span>');
                        setTimeout(() => {
                            if (uploadZone.classList.contains('has-preview')) {
                                statusBar.className = 'status-bar default';
                                statusContent.innerHTML = '<span>🖱️ 点击更换图片</span>';
                            }
                        }, 1000);
                    }
                });
                
                fileInput.addEventListener('change', (e) => {
                    if (e.target.files?.length) handleFile(e.target.files[0]);
                });
                
                function validate(text) {
                    if (!text) return false;
                    const lower = text.toLowerCase();
                    return lower.includes(REQUIRED_DOMAIN) ||
                           lower.replace(/[\s\n\r]/g, '').includes(REQUIRED_DOMAIN);
                }
                
                let timeout = null;
                
                function resetToDefault() {
                    if (timeout) clearTimeout(timeout);
                    if (uploadZone.classList.contains('has-preview')) {
                        statusBar.className = 'status-bar default';
                        statusContent.innerHTML = '<span>🖱️ 点击更换图片</span>';
                    }
                }
                
                function showConfetti() {
                    const container = document.createElement('div');
                    container.className = 'confetti';
                    document.body.appendChild(container);
                    const colors = ['#ffd700', '#ffaa00', '#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#f3a683', '#f8a5c2'];
                    for (let i = 0; i < 80; i++) {
                        const piece = document.createElement('div');
                        piece.className = 'confetti-piece';
                        piece.style.left = Math.random() * 100 + '%';
                        piece.style.width = (Math.random() * 8 + 4) + 'px';
                        piece.style.height = (Math.random() * 12 + 6) + 'px';
                        piece.style.background = colors[Math.floor(Math.random() * colors.length)];
                        piece.style.animationDelay = Math.random() * 0.5 + 's';
                        piece.style.animationDuration = (Math.random() * 2 + 2) + 's';
                        container.appendChild(piece);
                    }
                    setTimeout(() => container.remove(), 3000);
                }
                
                async function handleFile(file) {
                    rewardCard.style.display = 'none';
                    
                    const reader = new FileReader();
                    reader.onload = (e) => {
                        previewImg.src = e.target.result;
                        uploadZone.classList.add('has-preview');
                        updateButtonStyle();
                    };
                    reader.readAsDataURL(file);
                    
                    updateStatus('loading', '识别中...', '<span class="spinner-small"></span>');
                    
                    try {
                        const img = await new Promise((resolve, reject) => {
                            const img = new Image();
                            img.onload = () => { URL.revokeObjectURL(img.src); resolve(img); };
                            img.onerror = reject;
                            img.src = URL.createObjectURL(file);
                        });
                        
                        const canvas = document.createElement('canvas');
                        const ctx = canvas.getContext('2d');
                        canvas.width = img.width;
                        canvas.height = img.height;
                        ctx.drawImage(img, 0, 0);
                        const data = ctx.getImageData(0, 0, canvas.width, canvas.height);
                        for (let i = 0; i < data.data.length; i += 4) {
                            const gray = 0.299 * data.data[i] + 0.587 * data.data[i+1] + 0.114 * data.data[i+2];
                            const v = gray > 128 ? 255 : 0;
                            data.data[i] = data.data[i+1] = data.data[i+2] = v;
                        }
                        ctx.putImageData(data, 0, 0);
                        const blob = await new Promise(resolve => canvas.toBlob(resolve, 'image/png'));
                        
                        if (typeof Tesseract === 'undefined') {
                            await new Promise((resolve, reject) => {
                                const s = document.createElement('script');
                                s.src = 'https://cdn.jsdelivr.net/npm/tesseract.js@5/dist/tesseract.min.js';
                                s.onload = resolve;
                                s.onerror = reject;
                                document.head.appendChild(s);
                            });
                        }
                        
                        const worker = await Tesseract.createWorker('eng');
                        await worker.setParameters({
                            tessedit_pageseg_mode: '6',
                            tessedit_char_whitelist: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.:/_-'
                        });
                        const { data: { text } } = await worker.recognize(blob);
                        await worker.terminate();
                        
                        if (validate(text)) {
                            updateStatus('success', '验证成功！', '<span>✓</span>');
                            timeout = setTimeout(() => {
                                resetToDefault();
                                rewardCard.style.display = 'block';
                                showConfetti();
                            }, 800);
                        } else {
                            updateStatus('error', '未检测到指定域名', '<span>✗</span>');
                            timeout = setTimeout(() => resetToDefault(), 1000);
                        }
                    } catch {
                        updateStatus('error', '识别失败，请重试', '<span>✗</span>');
                        timeout = setTimeout(() => resetToDefault(), 1000);
                    }
                }
                
                updateButtonStyle();
            })();
        </script>
    </body>
    </html>