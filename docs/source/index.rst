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
        <title>分享有奖 · DrestryRobot</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                background: transparent;
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                padding: 20px;
                display: flex;
                justify-content: center;
            }

            .drestry-reward {
                max-width: 500px;
                width: 100%;
            }

            /* 主题变量 */
            .drestry-reward {
                --text: #212529;
                --text-muted: #6c757d;
                --accent: #3b82f6;
                --accent-bg: #eef2ff;
                --success: #10b981;
                --success-bg: #d1fae5;
                --error: #ef4444;
                --error-bg: #fee2e2;
                --border: #e9ecef;
                --card-bg: #ffffff;
                --overlay-bg: rgba(0,0,0,0.6);
                --qr-border: #e5e7eb;
            }

            @media (prefers-color-scheme: dark) {
                .drestry-reward {
                    --text: #cdd6f4;
                    --text-muted: #a6adc8;
                    --accent: #89b4fa;
                    --accent-bg: #313244;
                    --success: #a6e3a1;
                    --success-bg: #313244;
                    --error: #f38ba8;
                    --error-bg: #313244;
                    --border: #3a3a4a;
                    --card-bg: #1e1e2e;
                    --overlay-bg: rgba(0,0,0,0.7);
                    --qr-border: #3a3a4a;
                }
            }

            .reward-inner {
                padding: 20px;
            }

            .reward-desc {
                color: var(--text-muted);
                font-size: 14px;
                line-height: 1.5;
                margin-bottom: 20px;
                text-align: center;
            }

            .reward-desc strong {
                color: var(--accent);
                font-family: monospace;
                font-size: 12px;
                background: var(--accent-bg);
                padding: 2px 8px;
                border-radius: 20px;
            }

            .upload-zone {
                background: var(--card-bg);
                border: 2px dashed var(--border);
                border-radius: 20px;
                text-align: center;
                cursor: pointer;
                transition: all 0.2s;
                position: relative;
                min-height: 200px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                overflow: hidden;
            }

            .upload-zone:hover {
                border-color: var(--accent);
            }

            .upload-content {
                padding: 40px 20px;
                position: relative;
                z-index: 2;
            }

            .upload-icon {
                font-size: 48px;
                margin-bottom: 10px;
            }

            .upload-text {
                color: var(--text);
                font-weight: 500;
                font-size: 16px;
            }

            .upload-hint {
                color: var(--text-muted);
                font-size: 12px;
                margin-top: 6px;
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

            .preview-overlay {
                position: absolute;
                bottom: 0;
                left: 0;
                right: 0;
                background: var(--overlay-bg);
                color: white;
                text-align: center;
                padding: 10px;
                font-size: 13px;
                font-weight: 500;
                backdrop-filter: blur(4px);
                z-index: 3;
                display: none;
                border-radius: 0 0 18px 18px;
            }

            .preview-overlay span {
                display: inline-flex;
                align-items: center;
                gap: 6px;
            }

            .upload-zone.has-preview .upload-content {
                opacity: 0;
                visibility: hidden;
            }

            .upload-zone.has-preview .preview-img {
                display: block;
            }

            .upload-zone.has-preview .preview-overlay {
                display: block;
            }

            .status {
                padding: 12px;
                border-radius: 16px;
                font-size: 13px;
                text-align: center;
                margin: 16px 0;
                display: none;
            }

            .status.loading {
                background: var(--accent-bg);
                color: var(--accent);
                display: block;
            }

            .status.success {
                background: var(--success-bg);
                color: var(--success);
                display: block;
            }

            .status.error {
                background: var(--error-bg);
                color: var(--error);
                display: block;
            }

            /* 优化后的领奖区域 */
            .reward-card {
                background: linear-gradient(135deg, #10b981 0%, #059669 100%);
                border-radius: 20px;
                padding: 20px;
                margin-top: 16px;
                text-align: center;
                animation: fadeInUp 0.4s ease;
                box-shadow: 0 8px 20px rgba(16, 185, 129, 0.3);
            }

            @media (prefers-color-scheme: dark) {
                .reward-card {
                    background: linear-gradient(135deg, #0f9d6e 0%, #047857 100%);
                    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
                }
            }

            .reward-card-title {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 8px;
                color: white;
                font-size: 18px;
                font-weight: 600;
                margin-bottom: 16px;
            }

            .reward-card-title span {
                font-size: 22px;
            }

            .qr-wrapper {
                background: white;
                border-radius: 20px;
                padding: 16px;
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
                color: rgba(255, 255, 255, 0.9);
                font-size: 13px;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 6px;
            }

            .reward-footer {
                margin-top: 20px;
                font-size: 11px;
                color: var(--text-muted);
                text-align: center;
                padding-top: 16px;
                border-top: 1px solid var(--border);
            }

            @keyframes fadeInUp {
                from {
                    opacity: 0;
                    transform: translateY(20px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

            @media (max-width: 560px) {
                .reward-inner {
                    padding: 16px;
                }
                .upload-content {
                    padding: 30px 16px;
                }
                .upload-icon {
                    font-size: 40px;
                }
                .upload-text {
                    font-size: 14px;
                }
                .preview-overlay {
                    padding: 8px;
                    font-size: 12px;
                }
                .preview-img {
                    padding: 8px;
                }
                .qr-img-reward {
                    width: 120px;
                    height: 120px;
                }
                .reward-card-title {
                    font-size: 16px;
                }
            }
        </style>
    </head>
    <body>
        <div class="drestry-reward">
            <div class="reward-inner">
                <div class="reward-desc">
                    上传包含 <strong>drestryrobot.readthedocs.io</strong> 的截图
                </div>

                <div class="upload-zone" id="uploadZone">
                    <div class="upload-content">
                        <div class="upload-icon">📸</div>
                        <div class="upload-text">点击上传截图</div>
                        <div class="upload-hint">支持 JPG / PNG</div>
                    </div>
                    <img class="preview-img" id="previewImg" alt="预览">
                    <div class="preview-overlay" id="previewOverlay">
                        <span>🖱️ 点击更换图片</span>
                    </div>
                    <input type="file" id="fileInput" accept="image/*" style="display: none;">
                </div>

                <div class="status" id="statusMsg"></div>

                <div class="reward-card" id="rewardCard" style="display: none;">
                    <div class="reward-card-title">
                        <span>🎉</span> 验证成功，领奖 <span>🧧</span>
                    </div>
                    <div class="qr-wrapper">
                        <div class="qr-img-reward">
                            <img id="rewardQr" src="https://drestryrobot.oss-cn-shanghai.aliyuncs.com/202606%20%E5%BE%AE%E4%BF%A1%E4%BA%8C%E7%BB%B4%E7%A0%81.png" alt="微信红包二维码">
                        </div>
                    </div>
                    <div class="reward-card-desc">
                        <span>💚</span> 微信扫一扫领取红包 <span>💚</span>
                    </div>
                </div>

                <div class="reward-footer">
                    ⚡ 本地OCR识别 · 图片不上传服务器
                </div>
            </div>
        </div>

        <script>
            (function() {
                const REQUIRED_DOMAIN = "drestryrobot.readthedocs.io";
                
                const uploadZone = document.getElementById('uploadZone');
                const fileInput = document.getElementById('fileInput');
                const previewImg = document.getElementById('previewImg');
                const statusDiv = document.getElementById('statusMsg');
                const rewardCard = document.getElementById('rewardCard');
                
                uploadZone.addEventListener('click', () => fileInput.click());
                
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
                
                function showStatus(msg, type) {
                    statusDiv.className = 'status';
                    statusDiv.textContent = msg;
                    statusDiv.style.display = 'block';
                    statusDiv.classList.add(type);
                }
                
                function hideStatus() {
                    statusDiv.style.display = 'none';
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
                        
                        const processedBlob = await preprocess(img);
                        const text = await ocr(processedBlob);
                        
                        if (validate(text)) {
                            showStatus('验证成功', 'success');
                            rewardCard.style.display = 'block';
                        } else {
                            showStatus('未检测到指定域名', 'error');
                        }
                    } catch {
                        showStatus('识别失败，请重试', 'error');
                    }
                }
                
                function preprocess(img) {
                    return new Promise((resolve) => {
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
                        canvas.toBlob(resolve, 'image/png');
                    });
                }
                
                let worker = null;
                async function ocr(blob) {
                    if (typeof Tesseract === 'undefined') {
                        await new Promise((resolve, reject) => {
                            const s = document.createElement('script');
                            s.src = 'https://cdn.jsdelivr.net/npm/tesseract.js@5/dist/tesseract.min.js';
                            s.onload = resolve;
                            s.onerror = reject;
                            document.head.appendChild(s);
                        });
                    }
                    if (!worker) {
                        worker = await Tesseract.createWorker('eng');
                        await worker.setParameters({
                            tessedit_pageseg_mode: '6',
                            tessedit_char_whitelist: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.:/_-'
                        });
                    }
                    const { data: { text } } = await worker.recognize(blob);
                    return text;
                }
            })();
        </script>
    </body>
    </html>