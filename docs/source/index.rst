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

    <style>
        .drestry-reward {
            max-width: 100%;
            margin: 0;
            background: var(--bg);
            border-radius: 0;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }
        
        /* 主题变量 */
        .drestry-reward {
            --bg: #ffffff;
            --bg-secondary: #f8f9fa;
            --border: #e9ecef;
            --text: #212529;
            --text-muted: #6c757d;
            --accent: #3b82f6;
            --accent-bg: #eef2ff;
            --success: #10b981;
            --success-bg: #d1fae5;
            --error: #ef4444;
            --error-bg: #fee2e2;
        }
        
        @media (prefers-color-scheme: dark) {
            .drestry-reward {
                --bg: #1e1e2e;
                --bg-secondary: #2a2a3a;
                --border: #3a3a4a;
                --text: #cdd6f4;
                --text-muted: #a6adc8;
                --accent: #89b4fa;
                --accent-bg: #313244;
                --success: #a6e3a1;
                --success-bg: #313244;
                --error: #f38ba8;
                --error-bg: #313244;
            }
        }
        
        .reward-inner {
            padding: 20px 16px;
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
            padding: 2px 6px;
            border-radius: 12px;
            word-break: break-all;
        }
        
        .upload-zone {
            background: var(--bg-secondary);
            border: 2px dashed var(--border);
            border-radius: 20px;
            text-align: center;
            cursor: pointer;
            padding: 28px 16px;
            margin-bottom: 16px;
            transition: all 0.2s;
        }
        
        .upload-zone:active {
            transform: scale(0.98);
        }
        
        .upload-icon {
            font-size: 44px;
            margin-bottom: 8px;
        }
        
        .upload-text {
            color: var(--text);
            font-weight: 500;
            font-size: 15px;
            margin-bottom: 4px;
        }
        
        .upload-hint {
            color: var(--text-muted);
            font-size: 11px;
        }
        
        .upload-hint strong {
            color: var(--accent);
            font-family: monospace;
            font-size: 10px;
        }
        
        .preview-box {
            display: none;
            margin-bottom: 16px;
            border-radius: 16px;
            overflow: hidden;
            background: var(--bg-secondary);
        }
        
        .preview-box img {
            width: 100%;
            max-height: 160px;
            object-fit: contain;
            display: block;
        }
        
        .status {
            padding: 12px 16px;
            border-radius: 16px;
            font-size: 13px;
            text-align: center;
            margin-bottom: 16px;
            display: none;
            word-break: break-word;
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
        
        .qr-container {
            background: var(--bg-secondary);
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            display: none;
        }
        
        .qr-img {
            width: 140px;
            height: 140px;
            margin: 0 auto 12px;
            background: #fff;
            border-radius: 16px;
            padding: 10px;
        }
        
        .qr-img img {
            width: 100%;
            height: 100%;
            object-fit: contain;
        }
        
        .qr-note {
            color: var(--text-muted);
            font-size: 12px;
        }
        
        .reward-footer {
            margin-top: 20px;
            font-size: 10px;
            color: var(--text-muted);
            text-align: center;
            border-top: 1px solid var(--border);
            padding-top: 16px;
        }
        
        /* 大屏幕适配 */
        @media (min-width: 600px) {
            .drestry-reward {
                max-width: 520px;
                margin: 32px auto;
                border-radius: 32px;
                border: 1px solid var(--border);
            }
            .reward-inner {
                padding: 28px 24px;
            }
            .upload-zone {
                padding: 32px 20px;
            }
            .upload-icon {
                font-size: 48px;
            }
            .qr-img {
                width: 160px;
                height: 160px;
            }
        }
    </style>

    <div class="drestry-reward">
        <div class="reward-inner">
            <div class="reward-desc">
                上传包含 <strong>drestryrobot.readthedocs.io</strong><br>的截图，自动识别后领取红包
            </div>

            <div class="upload-zone" id="uploadZone">
                <div class="upload-icon">📸</div>
                <div class="upload-text">点击上传截图</div>
                <div class="upload-hint">支持 JPG / PNG</div>
                <input type="file" id="fileInput" accept="image/*" style="display: none;">
            </div>

            <div class="preview-box" id="previewBox">
                <img id="previewImg" alt="预览">
            </div>

            <div class="status" id="statusMsg"></div>

            <div class="qr-container" id="qrArea">
                <div class="qr-img">
                    <img id="rewardQr" src="https://drestryrobot.oss-cn-shanghai.aliyuncs.com/202606%20%E5%BE%AE%E4%BF%A1%E4%BA%8C%E7%BB%B4%E7%A0%81.png" alt="微信红包二维码">
                </div>
                <div class="qr-note">💰 微信扫一扫领奖</div>
            </div>

            <div class="reward-footer">
                ⚡ 本地识别 · 图片不上传
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
                else showStatus('请上传图片文件', 'error');
            });
            
            fileInput.addEventListener('change', (e) => {
                if (e.target.files?.length) handleFile(e.target.files[0]);
            });
            
            function validate(text) {
                if (!text) return false;
                const lower = text.toLowerCase();
                return lower.includes(REQUIRED_DOMAIN) ||
                       lower.replace(/\s/g, '').includes(REQUIRED_DOMAIN) ||
                       (/drestryrobot/i.test(lower) && /readthedocs/i.test(lower) && /\.?io\b/i.test(lower));
            }
            
            function showStatus(msg, type) {
                statusDiv.textContent = msg;
                statusDiv.className = 'status';
                statusDiv.classList.add(type);
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
                        showStatus('✅ 验证通过，扫码领奖', 'success');
                        qrArea.style.display = 'block';
                    } else {
                        showStatus('❌ 未检测到指定域名，请重试', 'error');
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