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
            *{margin:0;padding:0;box-sizing:border-box}
            .drestry-reward{width:100%;font-family:system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;padding-bottom:20px}
            .upload-zone{background:#f5f5f7;border:2px dashed #d4d4d8;border-radius:24px;cursor:pointer;transition:border-color .25s;position:relative;width:100%;aspect-ratio:16/9;overflow:hidden}
            .upload-zone:hover{border-color:#a1a1aa}
            .upload-content{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;transition:opacity .3s;pointer-events:none}
            .upload-icon{font-size:48px;margin-bottom:12px}
            .upload-text{color:#3f3f46;font-weight:500;font-size:1rem;margin-bottom:8px}
            .upload-desc{color:#71717a;font-size:.85rem}
            .upload-desc .domain{color:#71717a;font-weight:500}
            .preview-container{position:absolute;inset:0;display:none;justify-content:center;align-items:center;background:#f5f5f7}
            .preview-img{max-width:100%;max-height:100%;width:auto;height:auto;display:block}
            .action-btn{position:absolute;top:16px;right:16px;width:56px;height:56px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:15;backdrop-filter:blur(4px);border:1px solid rgba(255,255,255,.4);transition:all .2s;font-size:28px;font-weight:600}
            .action-btn span{line-height:1;margin-top:-2px}
            .copy-btn{background:#10b981;color:#fff}
            .copy-btn:hover{background:#059669;transform:scale(1.05)}
            .clear-btn{background:#ef4444;color:#fff}
            .clear-btn:hover{background:#dc2626;transform:scale(1.05)}
            .upload-zone.has-preview .upload-content{opacity:0;visibility:hidden}
            .upload-zone.has-preview .preview-container{display:flex}
            .reward-card{background:#f5f5f7;border:1px solid #e4e4e9;border-radius:24px;padding:20px;margin-top:20px;text-align:center;animation:celebrate .5s}
            @keyframes celebrate{0%{opacity:0;transform:scale(.95)}50%{opacity:1;transform:scale(1.02)}100%{opacity:1;transform:scale(1)}}
            .reward-title{display:flex;align-items:center;justify-content:center;gap:8px;color:#3f3f46;font-size:1.1rem;font-weight:600;margin-bottom:16px}
            .reward-title span{font-size:1.35rem}
            .qr-img{width:140px;height:140px;margin:0 auto}
            .qr-img img{width:100%;height:100%;object-fit:contain}
            .reward-desc{color:#71717a;font-size:.8rem;margin-top:12px}
            .toast{position:fixed;bottom:30px;left:50%;transform:translateX(-50%) translateY(100px);background:rgba(0,0,0,.8);color:#fff;padding:10px 20px;border-radius:40px;font-size:14px;z-index:1000;opacity:0;transition:all .3s;white-space:nowrap;pointer-events:none}
            .toast.show{transform:translateX(-50%) translateY(0);opacity:1}
            .toast-spinner{display:inline-block;width:14px;height:14px;border:2px solid rgba(255,255,255,.3);border-top-color:#fff;border-radius:50%;animation:spin .8s linear infinite;margin-right:8px;vertical-align:middle}
            @keyframes spin{to{transform:rotate(360deg)}}
            .confetti{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:999;overflow:hidden}
            .confetti-piece{position:absolute;width:10px;height:20px;background:linear-gradient(135deg,#ffd700,#ffaa00);opacity:.8;animation:fall 3s linear forwards}
            @keyframes fall{0%{transform:translateY(-100px) rotate(0);opacity:1}100%{transform:translateY(100vh) rotate(360deg);opacity:0}}
            @media (max-width:560px){.upload-icon{font-size:40px}.upload-text{font-size:.9rem}.upload-desc{font-size:.75rem}.action-btn{width:48px;height:48px;font-size:24px;top:12px;right:12px}.qr-img{width:110px;height:110px}.reward-card{padding:16px}}
        </style>
    </head>
    <body>
        <div class="drestry-reward">
            <div class="upload-zone" id="uploadZone">
                <div class="action-btn" id="actionBtn"><span>✓</span></div>
                <div class="upload-content">
                    <div class="upload-icon">📸</div>
                    <div class="upload-text">点击上传截图</div>
                    <div class="upload-desc">上传包含 <span class="domain">drestryrobot.readthedocs.io</span> 的分享截图有奖</div>
                </div>
                <div class="preview-container" id="previewContainer"><img class="preview-img" id="previewImg" alt="预览"></div>
                <input type="file" id="fileInput" accept="image/*" style="display:none">
            </div>
            <div class="reward-card" id="rewardCard" style="display:none">
                <div class="reward-title"><span>🎉</span> 验证成功，领奖 <span>🧧</span></div>
                <div class="qr-img"><img id="rewardQr" src="https://drestryrobot.oss-cn-shanghai.aliyuncs.com/202606%20%E5%BE%AE%E4%BF%A1%E4%BA%8C%E7%BB%B4%E7%A0%81.png" alt="二维码"></div>
                <div class="reward-desc">📱 微信扫一扫领取红包</div>
            </div>
        </div>
        <div class="toast" id="toast"></div>

        <script>
            (function(){
                const zone = document.getElementById('uploadZone');
                const fileInput = document.getElementById('fileInput');
                const previewImg = document.getElementById('previewImg');
                const rewardCard = document.getElementById('rewardCard');
                const actionBtn = document.getElementById('actionBtn');
                const toast = document.getElementById('toast');
                
                let timeout = null;
                
                function showToast(msg, isLoading) {
                    if (isLoading) {
                        toast.innerHTML = '<span class="toast-spinner"></span> ' + msg;
                    } else {
                        toast.innerHTML = msg;
                    }
                    toast.classList.add('show');
                    setTimeout(() => toast.classList.remove('show'), 2000);
                }
                
                async function copyLink() {
                    try {
                        await navigator.clipboard.writeText('https://drestryrobot.readthedocs.io');
                        showToast('✅ 网址复制成功！快去分享吧！');
                    } catch {
                        const ta = document.createElement('textarea');
                        ta.value = 'https://drestryrobot.readthedocs.io';
                        document.body.appendChild(ta);
                        ta.select();
                        document.execCommand('copy');
                        document.body.removeChild(ta);
                        showToast('✅ 网址复制成功！快去分享吧！');
                    }
                }
                
                function clearImage() {
                    zone.classList.remove('has-preview');
                    previewImg.src = '';
                    fileInput.value = '';
                    rewardCard.style.display = 'none';
                    actionBtn.className = 'action-btn copy-btn';
                    actionBtn.innerHTML = '<span>✓</span>';
                    showToast('🗑️ 已清除图片');
                }
                
                function updateBtn() {
                    if (zone.classList.contains('has-preview')) {
                        actionBtn.className = 'action-btn clear-btn';
                        actionBtn.innerHTML = '<span>✗</span>';
                    } else {
                        actionBtn.className = 'action-btn copy-btn';
                        actionBtn.innerHTML = '<span>✓</span>';
                    }
                }
                
                actionBtn.onclick = (e) => {
                    e.stopPropagation();
                    zone.classList.contains('has-preview') ? clearImage() : copyLink();
                };
                
                zone.onclick = (e) => {
                    if (e.target === actionBtn || e.target.parentNode === actionBtn) return;
                    fileInput.click();
                };
                
                zone.ondragover = (e) => e.preventDefault();
                zone.ondrop = (e) => {
                    e.preventDefault();
                    const f = e.dataTransfer.files[0];
                    if (f && f.type.startsWith('image/')) handleFile(f);
                    else showToast('❌ 请上传图片');
                };
                
                fileInput.onchange = (e) => {
                    if (e.target.files?.length) handleFile(e.target.files[0]);
                };
                
                // 计算两个字符串的相似度（Levenshtein距离）
                function similarity(s1, s2) {
                    const len1 = s1.length;
                    const len2 = s2.length;
                    if (len1 === 0) return len2 === 0 ? 1 : 0;
                    if (len2 === 0) return 0;
                    
                    // 创建距离矩阵
                    const dp = Array(len1 + 1);
                    for (let i = 0; i <= len1; i++) {
                        dp[i] = Array(len2 + 1);
                        dp[i][0] = i;
                    }
                    for (let j = 0; j <= len2; j++) {
                        dp[0][j] = j;
                    }
                    
                    for (let i = 1; i <= len1; i++) {
                        for (let j = 1; j <= len2; j++) {
                            const cost = s1[i - 1] === s2[j - 1] ? 0 : 1;
                            dp[i][j] = Math.min(
                                dp[i - 1][j] + 1,
                                dp[i][j - 1] + 1,
                                dp[i - 1][j - 1] + cost
                            );
                        }
                    }
                    
                    const maxLen = Math.max(len1, len2);
                    const similarity = 1 - dp[len1][len2] / maxLen;
                    return similarity;
                }
                
                // 验证逻辑：在OCR文本中滑动窗口匹配域名
                function validate(text) {
                    if (!text) return false;
                    
                    const target = "drestryrobot.readthedocs.io";
                    const lowerText = text.toLowerCase().replace(/[\s\n\r\t]/g, '');
                    
                    console.log('OCR文本(去空格):', lowerText);
                    
                    // 滑动窗口匹配
                    let bestMatch = 0;
                    const targetLen = target.length;
                    
                    for (let i = 0; i <= Math.max(0, lowerText.length - targetLen); i++) {
                        const sub = lowerText.substring(i, i + targetLen);
                        const sim = similarity(sub, target);
                        if (sim > bestMatch) {
                            bestMatch = sim;
                        }
                    }
                    
                    // 也检查较短的窗口（处理OCR识别缺失字符的情况）
                    for (let len = Math.floor(targetLen * 0.7); len <= targetLen; len++) {
                        for (let i = 0; i <= lowerText.length - len; i++) {
                            const sub = lowerText.substring(i, i + len);
                            const sim = similarity(sub, target.substring(0, len));
                            if (sim > bestMatch) {
                                bestMatch = sim;
                            }
                        }
                    }
                    
                    console.log(`最佳相似度: ${(bestMatch * 100).toFixed(1)}%`);
                    
                    // 相似度 >= 60% 即通过
                    return bestMatch >= 0.6;
                }
                
                function showConfetti() {
                    const c = document.createElement('div');
                    c.className = 'confetti';
                    document.body.appendChild(c);
                    for (let i = 0; i < 80; i++) {
                        const p = document.createElement('div');
                        p.className = 'confetti-piece';
                        p.style.left = Math.random() * 100 + '%';
                        p.style.width = (Math.random() * 8 + 4) + 'px';
                        p.style.height = (Math.random() * 12 + 6) + 'px';
                        p.style.background = ['#ffd700', '#ffaa00', '#ff6b6b', '#4ecdc4', '#45b7d1'][Math.floor(Math.random() * 5)];
                        p.style.animationDelay = Math.random() * 0.5 + 's';
                        c.appendChild(p);
                    }
                    setTimeout(() => c.remove(), 3000);
                }
                
                async function handleFile(file) {
                    rewardCard.style.display = 'none';
                    
                    const reader = new FileReader();
                    reader.onload = (e) => {
                        previewImg.src = e.target.result;
                        zone.classList.add('has-preview');
                        updateBtn();
                    };
                    reader.readAsDataURL(file);
                    
                    showToast('识别中...', true);
                    
                    try {
                        const img = await new Promise((res, rej) => {
                            const i = new Image();
                            i.onload = () => { URL.revokeObjectURL(i.src); res(i); };
                            i.onerror = rej;
                            i.src = URL.createObjectURL(file);
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
                        const blob = await new Promise(r => canvas.toBlob(r, 'image/png'));
                        
                        if (typeof Tesseract === 'undefined') {
                            await new Promise((res, rej) => {
                                const s = document.createElement('script');
                                s.src = 'https://cdn.jsdelivr.net/npm/tesseract.js@5/dist/tesseract.min.js';
                                s.onload = res;
                                s.onerror = rej;
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
                        
                        toast.classList.remove('show');
                        
                        console.log('OCR识别结果:', text);
                        
                        if (validate(text)) {
                            showToast('✅ 验证成功！');
                            timeout = setTimeout(() => {
                                rewardCard.style.display = 'block';
                                showConfetti();
                            }, 800);
                        } else {
                            showToast('❌ 未检测到指定域名');
                        }
                    } catch (err) {
                        console.error(err);
                        toast.classList.remove('show');
                        showToast('❌ 识别失败，请重试');
                    }
                }
                
                updateBtn();
            })();
        </script>
    </body>
    </html>