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

            /* 深浅色主题变量 */
            :root {
                --text: #1e293b;
                --text-muted: #64748b;
                --accent: #3b82f6;
                --accent-light: #dbeafe;
                --success: #10b981;
                --success-light: #d1fae5;
                --error: #ef4444;
                --error-light: #fee2e2;
                --border: #e2e8f0;
                --card-bg: #ffffff;
                --overlay-bg: rgba(0, 0, 0, 0.65);
                --clear-bg: #ef4444;
                --shadow: rgba(0, 0, 0, 0.05);
            }

            @media (prefers-color-scheme: dark) {
                :root {
                    --text: #f1f5f9;
                    --text-muted: #94a3b8;
                    --accent: #60a5fa;
                    --accent-light: #1e293b;
                    --success: #34d399;
                    --success-light: #1e293b;
                    --error: #f87171;
                    --error-light: #1e293b;
                    --border: #334155;
                    --card-bg: #0f172a;
                    --overlay-bg: rgba(0, 0, 0, 0.75);
                    --clear-bg: #ef4444;
                    --shadow: rgba(0, 0, 0, 0.3);
                }
            }

            .drestry-reward {
                width: 100%;
                margin: 0;
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                padding-bottom: 20px;
            }

            .reward-inner {
                padding: 0;
            }

            /* 上传框 - 宽度100%自适应，固定比例16:9 */
            .upload-zone {
                background: var(--card-bg);
                border: 2px dashed var(--border);
                border-radius: 24px;
                text-align: center;
                cursor: pointer;
                transition: all 0.3s ease;
                position: relative;
                width: 100%;
                aspect-ratio: 16 / 9;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                overflow: hidden;
                box-shadow: 0 2px 8px var(--shadow);
            }

            .upload-zone:hover {
                border-color: var(--accent);
                background: var(--accent-light);
            }

            .upload-content {
                padding: 20px;
                position: relative;
                z-index: 2;
                transition: opacity 0.3s ease, visibility 0.3s ease;
            }

            .upload-icon {
                font-size: 48px;
                margin-bottom: 12px;
            }

            .upload-text {
                color: var(--text);
                font-weight: 500;
                font-size: 1rem;
                margin-bottom: 8px;
            }

            .upload-desc {
                color: var(--text-muted);
                font-size: 0.85rem;
                line-height: 1.4;
            }

            .upload-desc .domain {
                color: var(--accent);
                font-weight: 500;
            }

            .preview-img {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                object-fit: contain;
                background: var(--card-bg);
                display: none;
                z-index: 1;
                padding: 12px;
            }

            /* 清除按钮 - 完美居中 */
            .clear-btn {
                position: absolute;
                top: 12px;
                right: 12px;
                width: 28px;
                height: 28px;
                background: var(--clear-bg);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                cursor: pointer;
                z-index: 15;
                opacity: 0;
                visibility: hidden;
                backdrop-filter: blur(4px);
                border: 1px solid rgba(255, 255, 255, 0.3);
                transition: all 0.2s ease;
            }

            .clear-btn span {
                color: white;
                font-size: 18px;
                font-weight: bold;
                line-height: 1;
                display: flex;
                align-items: center;
                justify-content: center;
                width: 100%;
                height: 100%;
            }

            .clear-btn:hover {
                transform: scale(1.1);
                background: #dc2626;
            }

            .upload-zone.has-preview .clear-btn {
                opacity: 1;
                visibility: visible;
            }

            /* 底部浮层 */
            .bottom-overlay {
                position: absolute;
                bottom: 0;
                left: 0;
                right: 0;
                padding: 0 16px;
                font-size: 0.875rem;
                font-weight: 500;
                text-align: center;
                z-index: 10;
                backdrop-filter: blur(16px);
                -webkit-backdrop-filter: blur(16px);
                border-radius: 0 0 22px 22px;
                transition: opacity 0.25s ease, transform 0.25s ease;
                height: 42px;
                display: flex;
                align-items: center;
                justify-content: center;
                border-top: 1px solid rgba(255, 255, 255, 0.15);
            }

            .change-overlay {
                background: var(--overlay-bg);
                color: white;
                opacity: 1;
                transform: translateY(0);
            }

            .change-overlay span {
                display: inline-flex;
                align-items: center;
                gap: 6px;
            }

            /* 状态浮层 */
            .status-overlay {
                background: var(--overlay-bg);
                color: white;
                opacity: 0;
                transform: translateY(10px);
                pointer-events: none;
            }

            .status-overlay.show {
                opacity: 1;
                transform: translateY(0);
            }

            .status-overlay.loading {
                background: rgba(59, 130, 246, 0.85);
            }

            .status-overlay.success {
                background: rgba(16, 185, 129, 0.85);
            }

            .status-overlay.error {
                background: rgba(239, 68, 68, 0.85);
            }

            .change-overlay.hide {
                opacity: 0;
                transform: translateY(10px);
                pointer-events: none;
            }

            .loading-spinner {
                display: inline-block;
                width: 14px;
                height: 14px;
                border: 2px solid rgba(255, 255, 255, 0.3);
                border-top-color: white;
                border-radius: 50%;
                animation: spin 0.8s linear infinite;
                margin-right: 8px;
                vertical-align: middle;
            }

            @keyframes spin {
                to { transform: rotate(360deg); }
            }

            .success-check {
                display: inline-block;
                animation: checkPop 0.4s ease-out;
                font-size: 1rem;
                font-weight: bold;
                margin-right: 6px;
            }

            @keyframes checkPop {
                0% { transform: scale(0); opacity: 0; }
                50% { transform: scale(1.2); }
                100% { transform: scale(1); opacity: 1; }
            }

            .upload-zone.has-preview .upload-content {
                opacity: 0;
                visibility: hidden;
            }

            .upload-zone.has-preview .preview-img {
                display: block;
            }

            /* 领奖卡片 */
            .reward-card {
                background: var(--card-bg);
                border: 1px solid var(--border);
                border-radius: 24px;
                padding: 24px;
                margin-top: 20px;
                text-align: center;
                animation: celebrate 0.5s ease-out;
                box-shadow: 0 4px 12px var(--shadow);
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
                color: var(--text);
                font-size: 1.1rem;
                font-weight: 600;
                margin-bottom: 16px;
            }

            .reward-card-title span {
                font-size: 1.35rem;
            }

            /* 二维码背景始终白色 */
            .qr-wrapper {
                background: #ffffff;
                border-radius: 20px;
                padding: 12px;
                display: inline-block;
                margin-bottom: 12px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
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
                color: var(--text-muted);
                font-size: 0.8rem;
            }

            /* 移动端适配 */
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
                .bottom-overlay {
                    height: 38px;
                    font-size: 0.8rem;
                }
                .clear-btn {
                    top: 8px;
                    right: 8px;
                }
                .qr-img-reward {
                    width: 110px;
                    height: 110px;
                }
                .reward-card {
                    padding: 18px;
                }
            }
        </style>
    </head>
    <body>
        <div class="drestry-reward">
            <div class="reward-inner">
                <div class="upload-zone" id="uploadZone">
                    <div class="clear-btn" id="clearBtn">
                        <span>✕</span>
                    </div>

                    <div class="upload-content">
                        <div class="upload-icon">📸</div>
                        <div class="upload-text">点击上传截图</div>
                        <div class="upload-desc">
                            上传包含 <span class="domain">drestryrobot.readthedocs.io</span> 的分享截图有奖
                        </div>
                    </div>

                    <img class="preview-img" id="previewImg" alt="预览">

                    <div class="bottom-overlay change-overlay" id="changeOverlay">
                        <span>🖱️ 点击更换图片</span>
                    </div>

                    <div class="bottom-overlay status-overlay" id="statusOverlay"></div>

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

        <script>
            (function() {
                const REQUIRED_DOMAIN = "drestryrobot.readthedocs.io";
                
                const uploadZone = document.getElementById('uploadZone');
                const fileInput = document.getElementById('fileInput');
                const previewImg = document.getElementById('previewImg');
                const changeOverlay = document.getElementById('changeOverlay');
                const statusOverlay = document.getElementById('statusOverlay');
                const rewardCard = document.getElementById('rewardCard');
                const clearBtn = document.getElementById('clearBtn');
                
                changeOverlay.classList.remove('hide');
                statusOverlay.classList.remove('show');
                
                clearBtn.addEventListener('click', (e) => {
                    e.stopPropagation();
                    uploadZone.classList.remove('has-preview');
                    previewImg.src = '';
                    fileInput.value = '';
                    rewardCard.style.display = 'none';
                    hideStatus();
                });
                
                uploadZone.addEventListener('click', (e) => {
                    if (e.target === clearBtn || e.target.parentNode === clearBtn) return;
                    fileInput.click();
                });
                
                uploadZone.addEventListener('dragover', (e) => {
                    e.preventDefault();
                    uploadZone.style.borderColor = 'var(--accent)';
                });
                uploadZone.addEventListener('dragleave', () => {
                    uploadZone.style.borderColor = 'var(--border)';
                });
                uploadZone.addEventListener('drop', (e) => {
                    e.preventDefault();
                    uploadZone.style.borderColor = 'var(--border)';
                    const file = e.dataTransfer.files[0];
                    if (file && file.type.startsWith('image/')) handleFile(file);
                    else showStatus('请上传图片', 'error');
                });
                
                fileInput.addEventListener('change', (e) => {
                    if (e.target.files?.length) handleFile(e.target.files[0]);
                });
                
                function validate(text) {
                    if (!text) return false;
                    const lower = text.toLowerCase();
                    return lower.includes(REQUIRED_DOMAIN) ||
                           lower.replace(/[\s\n\r]/g, '').includes(REQUIRED_DOMAIN) ||
                           (/drestryrobot/i.test(lower) && /readthedocs/i.test(lower));
                }
                
                let timeout = null;
                
                function showStatus(msg, type) {
                    if (timeout) clearTimeout(timeout);
                    changeOverlay.classList.add('hide');
                    statusOverlay.innerHTML = '';
                    statusOverlay.className = 'bottom-overlay status-overlay';
                    statusOverlay.classList.add(type);
                    if (type === 'loading') statusOverlay.innerHTML = '<span class="loading-spinner"></span> ' + msg;
                    else if (type === 'success') statusOverlay.innerHTML = '<span class="success-check">✓</span> ' + msg;
                    else statusOverlay.innerHTML = '✗ ' + msg;
                    statusOverlay.classList.add('show');
                }
                
                function hideStatus() {
                    if (timeout) clearTimeout(timeout);
                    statusOverlay.classList.remove('show');
                    changeOverlay.classList.remove('hide');
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
                    hideStatus();
                    
                    const reader = new FileReader();
                    reader.onload = (e) => {
                        previewImg.src = e.target.result;
                        uploadZone.classList.add('has-preview');
                    };
                    reader.readAsDataURL(file);
                    
                    showStatus('识别中...', 'loading');
                    
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
                            showStatus('验证成功！', 'success');
                            timeout = setTimeout(() => {
                                hideStatus();
                                rewardCard.style.display = 'block';
                                showConfetti();
                            }, 800);
                        } else {
                            showStatus('未检测到指定域名', 'error');
                            timeout = setTimeout(() => hideStatus(), 1000);
                        }
                    } catch {
                        showStatus('识别失败，请重试', 'error');
                        timeout = setTimeout(() => hideStatus(), 1000);
                    }
                }
            })();
        </script>
    </body>
    </html>