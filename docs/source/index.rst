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

🔥 分享有奖
-------------

.. raw:: html

    <style>
        /* 深浅色主题变量 */
        .drestry-reward-container {
            --bg-primary: linear-gradient(135deg, #0f172a 0%, #020617 100%);
            --bg-secondary: #0b0f18;
            --bg-card: rgba(18, 22, 31, 0.92);
            --border-color: rgba(59, 130, 246, 0.3);
            --text-title: linear-gradient(135deg, #FFFFFF 0%, #aac9ff 100%);
            --text-desc: #a5b3d0;
            --text-muted: #7786aa;
            --badge-bg: rgba(30, 41, 59, 0.9);
            --badge-color: #7aaef7;
            --upload-bg: #0b0f18;
            --upload-border: #2a354c;
            --upload-hover-bg: #111723;
            --preview-bg: #05080f;
            --preview-border: #29324a;
            --status-loading-bg: #1e2a44dd;
            --status-loading-color: #b9dcff;
            --status-success-bg: #0f2e1ddd;
            --status-success-color: #6bff8e;
            --status-error-bg: #2c1a1fdd;
            --status-error-color: #ff9494;
            --qr-bg: #0b0f17ea;
            --qr-border: #2e3c58;
            --qr-note-bg: #191f30;
            --qr-note-color: #bfcdf2;
            --footer-color: #556184;
            --footer-border: #222b3e;
            --highlight-bg: #1e2b3f;
            --highlight-color: #60a5fa;
            
            max-width: 620px;
            width: 100%;
            margin: 40px auto;
            background: var(--bg-primary);
            border-radius: 52px;
            border: 1px solid var(--border-color);
            box-shadow: 0 20px 40px -12px rgba(0, 0, 0, 0.5);
            overflow: hidden;
            font-family: -apple-system, 'Segoe UI', Roboto, sans-serif;
            transition: all 0.3s ease;
        }
        
        /* 浅色主题适配 */
        @media (prefers-color-scheme: light) {
            .drestry-reward-container {
                --bg-primary: linear-gradient(135deg, #e8edf5 0%, #d0d9e8 100%);
                --bg-secondary: #f0f4fa;
                --bg-card: rgba(245, 248, 250, 0.95);
                --border-color: rgba(59, 130, 246, 0.4);
                --text-title: linear-gradient(135deg, #1e293b 0%, #3b82f6 100%);
                --text-desc: #334155;
                --text-muted: #64748b;
                --badge-bg: rgba(59, 130, 246, 0.15);
                --badge-color: #2563eb;
                --upload-bg: #f8fafc;
                --upload-border: #cbd5e1;
                --upload-hover-bg: #f1f5f9;
                --preview-bg: #f1f5f9;
                --preview-border: #cbd5e1;
                --status-loading-bg: #dbeafe;
                --status-loading-color: #1e40af;
                --status-success-bg: #dcfce7;
                --status-success-color: #166534;
                --status-error-bg: #fee2e2;
                --status-error-color: #991b1b;
                --qr-bg: #ffffffea;
                --qr-border: #cbd5e1;
                --qr-note-bg: #e2e8f0;
                --qr-note-color: #1e293b;
                --footer-color: #64748b;
                --footer-border: #cbd5e1;
                --highlight-bg: #dbeafe;
                --highlight-color: #2563eb;
            }
        }
        
        /* 深色主题微调 */
        @media (prefers-color-scheme: dark) {
            .drestry-reward-container {
                --bg-primary: linear-gradient(135deg, #0f172a 0%, #020617 100%);
                --bg-secondary: #0b0f18;
                --text-desc: #a5b3d0;
                --text-muted: #7786aa;
            }
        }
        
        .reward-inner {
            padding: 34px 28px 42px;
        }
        
        .reward-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: var(--badge-bg);
            color: var(--badge-color);
            font-size: 12px;
            font-weight: 700;
            padding: 6px 18px;
            border-radius: 60px;
            margin-bottom: 22px;
            backdrop-filter: blur(4px);
        }
        
        .reward-title {
            font-size: 34px;
            font-weight: 800;
            background: var(--text-title);
            background-clip: text;
            -webkit-background-clip: text;
            color: transparent;
            margin-bottom: 12px;
        }
        
        .reward-desc {
            color: var(--text-desc);
            font-size: 15px;
            margin-bottom: 28px;
            border-left: 4px solid #3b82f6;
            padding-left: 16px;
            line-height: 1.45;
        }
        
        .upload-zone {
            background: var(--upload-bg);
            border: 2px dashed var(--upload-border);
            border-radius: 38px;
            text-align: center;
            cursor: pointer;
            transition: all 0.25s ease;
            margin-bottom: 24px;
            padding: 36px 20px;
        }
        
        .upload-zone:hover {
            border-color: #3b82f6;
            background: var(--upload-hover-bg);
            transform: translateY(-2px);
        }
        
        .upload-icon {
            font-size: 56px;
            margin-bottom: 12px;
            filter: drop-shadow(0 4px 6px rgba(0,0,0,0.1));
        }
        
        .upload-text {
            color: var(--text-desc);
            font-weight: 600;
            font-size: 18px;
            margin-bottom: 8px;
        }
        
        .upload-hint {
            color: var(--text-muted);
            font-size: 12.5px;
        }
        
        .upload-hint strong {
            color: var(--highlight-color);
            background: var(--highlight-bg);
            padding: 3px 10px;
            border-radius: 40px;
            font-family: monospace;
        }
        
        .preview-box {
            margin-bottom: 26px;
            display: none;
            border-radius: 32px;
            background: var(--preview-bg);
            padding: 12px;
            border: 1px solid var(--preview-border);
        }
        
        .preview-box img {
            width: 100%;
            max-height: 200px;
            object-fit: contain;
            border-radius: 22px;
        }
        
        .status {
            padding: 14px 22px;
            border-radius: 60px;
            font-size: 14px;
            font-weight: 500;
            text-align: center;
            margin-bottom: 26px;
            display: none;
        }
        
        .status.loading {
            background: var(--status-loading-bg);
            color: var(--status-loading-color);
            display: block;
        }
        
        .status.success {
            background: var(--status-success-bg);
            color: var(--status-success-color);
            display: block;
        }
        
        .status.error {
            background: var(--status-error-bg);
            color: var(--status-error-color);
            display: block;
        }
        
        .qr-container {
            background: var(--qr-bg);
            border-radius: 42px;
            padding: 28px 20px;
            text-align: center;
            border: 1px solid var(--qr-border);
            display: none;
            margin-top: 8px;
            backdrop-filter: blur(4px);
        }
        
        .qr-container h3 {
            color: var(--status-success-color);
            font-size: 24px;
            margin-bottom: 10px;
            text-align: center;
        }
        
        .qr-img {
            width: 190px;
            height: 190px;
            margin: 12px auto 18px;
            background: #ffffff;
            border-radius: 32px;
            padding: 16px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
        }
        
        .qr-img img {
            width: 100%;
            height: 100%;
            object-fit: contain;
            border-radius: 18px;
        }
        
        .qr-note {
            color: var(--qr-note-color);
            font-size: 14px;
            background: var(--qr-note-bg);
            display: inline-block;
            padding: 8px 24px;
            border-radius: 60px;
        }
        
        .reward-footer {
            margin-top: 34px;
            font-size: 11px;
            color: var(--footer-color);
            text-align: center;
            border-top: 1px solid var(--footer-border);
            padding-top: 24px;
        }
        
        /* 移动端适配 */
        @media (max-width: 600px) {
            .reward-inner {
                padding: 24px 20px 32px;
            }
            .reward-title {
                font-size: 28px;
            }
            .upload-icon {
                font-size: 48px;
            }
            .upload-text {
                font-size: 16px;
            }
            .qr-img {
                width: 160px;
                height: 160px;
            }
        }
    </style>

    <div class="drestry-reward-container">
        <div class="reward-inner">
            <div class="reward-badge">
                📘 DrestryRobot · 文档验证
            </div>
            <div class="reward-title">分享即领奖</div>
            <div class="reward-desc">
                🔍 上传包含 <strong>“drestryrobot.readthedocs.io”</strong> 的截图 → OCR识别 → 验证通过 → 秒获红包
            </div>

            <div class="upload-zone" id="uploadZone">
                <div class="upload-icon">📸📄</div>
                <div class="upload-text">点击上传 或 拖拽截图</div>
                <div class="upload-hint">支持 JPG / PNG，需包含 <strong>drestryrobot.readthedocs.io</strong></div>
                <input type="file" id="fileInput" accept="image/*" style="display: none;">
            </div>

            <div class="preview-box" id="previewBox">
                <img id="previewImg" alt="截图预览">
            </div>

            <div class="status" id="statusMsg"></div>

            <div class="qr-container" id="qrArea">
                <h3>🎁 验证通过 · 专属奖励</h3>
                <div class="qr-img">
                    <img id="rewardQr" src="https://drestryrobot.oss-cn-shanghai.aliyuncs.com/202606%20%E5%BE%AE%E4%BF%A1%E4%BA%8C%E7%BB%B4%E7%A0%81.png" alt="微信红包二维码">
                </div>
                <div class="qr-note">💰 微信扫一扫 · 立即领取现金红包</div>
            </div>

            <div class="reward-footer">
                ⚡ 本地OCR识别 · 图片不上传服务器 · 仅校验文档域名
            </div>
        </div>
    </div>

    <script>
        (function() {
            const REQUIRED_DOMAIN = "drestryrobot.readthedocs.io";
            
            const uploadZone = document.getElementById('uploadZone');
            const fileInput = document.getElementById('fileInput');
            const previewBox = document.getElementById('previewBox');
            const previewImg = document.getElementById('previewImg');
            const statusDiv = document.getElementById('statusMsg');
            const qrArea = document.getElementById('qrArea');
            
            if (!uploadZone) return;
            
            uploadZone.addEventListener('click', () => fileInput.click());
            
            uploadZone.addEventListener('dragover', (e) => {
                e.preventDefault();
                uploadZone.style.borderColor = '#3b82f6';
                uploadZone.style.background = 'var(--upload-hover-bg)';
            });
            uploadZone.addEventListener('dragleave', () => {
                uploadZone.style.borderColor = 'var(--upload-border)';
                uploadZone.style.background = 'var(--upload-bg)';
            });
            uploadZone.addEventListener('drop', (e) => {
                e.preventDefault();
                uploadZone.style.borderColor = 'var(--upload-border)';
                uploadZone.style.background = 'var(--upload-bg)';
                const file = e.dataTransfer.files[0];
                if (file && file.type.startsWith('image/')) {
                    handleFile(file);
                } else {
                    showStatus('❌ 请上传 PNG / JPG 格式截图', 'error');
                }
            });
            
            fileInput.addEventListener('change', (e) => {
                if (e.target.files && e.target.files.length) {
                    handleFile(e.target.files[0]);
                }
            });
            
            function validateDomain(text) {
                if (!text) return false;
                const lower = text.toLowerCase();
                if (lower.includes(REQUIRED_DOMAIN)) return true;
                const cleaned = lower.replace(/[\s\n\r\t]/g, '');
                if (cleaned.includes(REQUIRED_DOMAIN.replace(/[\s\n\r\t]/g, ''))) return true;
                if (/drestryrobot\s*\.\s*readthedocs\s*\.\s*io/i.test(lower)) return true;
                if (/drestryrobot/i.test(lower) && /readthedocs/i.test(lower) && /\.?io\b/i.test(lower)) return true;
                return false;
            }
            
            function showStatus(msg, type) {
                statusDiv.textContent = msg;
                statusDiv.className = 'status';
                if (type === 'loading') statusDiv.classList.add('loading');
                else if (type === 'success') statusDiv.classList.add('success');
                else if (type === 'error') statusDiv.classList.add('error');
            }
            
            async function handleFile(file) {
                qrArea.style.display = 'none';
                statusDiv.style.display = 'none';
                
                const reader = new FileReader();
                reader.onload = (e) => {
                    previewImg.src = e.target.result;
                    previewBox.style.display = 'block';
                };
                reader.readAsDataURL(file);
                
                showStatus('🔍 正在识别截图内容...', 'loading');
                
                try {
                    const img = await loadImage(file);
                    const processedBlob = await preprocessImage(img);
                    const text = await runOCR(processedBlob);
                    
                    if (validateDomain(text)) {
                        showStatus('✅ 验证通过！恭喜获得奖励资格', 'success');
                        qrArea.style.display = 'block';
                        qrArea.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                    } else {
                        showStatus('❌ 验证失败：未检测到 "drestryrobot.readthedocs.io"', 'error');
                    }
                } catch (err) {
                    showStatus('⚠️ 识别失败，请重试', 'error');
                }
            }
            
            function loadImage(file) {
                return new Promise((resolve, reject) => {
                    const img = new Image();
                    img.onload = () => { URL.revokeObjectURL(img.src); resolve(img); };
                    img.onerror = reject;
                    img.src = URL.createObjectURL(file);
                });
            }
            
            function preprocessImage(img) {
                return new Promise((resolve) => {
                    const canvas = document.createElement('canvas');
                    const ctx = canvas.getContext('2d');
                    canvas.width = img.width;
                    canvas.height = img.height;
                    ctx.drawImage(img, 0, 0);
                    const data = ctx.getImageData(0, 0, canvas.width, canvas.height);
                    for (let i = 0; i < data.data.length; i += 4) {
                        const gray = 0.299 * data.data[i] + 0.587 * data.data[i+1] + 0.114 * data.data[i+2];
                        const val = gray > 128 ? 255 : 0;
                        data.data[i] = data.data[i+1] = data.data[i+2] = val;
                    }
                    ctx.putImageData(data, 0, 0);
                    canvas.toBlob(resolve, 'image/png');
                });
            }
            
            let worker = null;
            async function runOCR(blob) {
                if (typeof Tesseract === 'undefined') {
                    await new Promise((resolve, reject) => {
                        const script = document.createElement('script');
                        script.src = 'https://cdn.jsdelivr.net/npm/tesseract.js@5/dist/tesseract.min.js';
                        script.onload = resolve;
                        script.onerror = reject;
                        document.head.appendChild(script);
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