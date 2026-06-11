🔥 DrestryRobot
=====================================
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
                <div class="reward-title"><span>🎉</span> 验证成功，有奖 <span>🧧</span></div>
                <div class="qr-img"><img id="rewardQr" src="https://drestryrobot.oss-cn-shanghai.aliyuncs.com/202606%20%E5%BE%AE%E4%BF%A1%E4%BA%8C%E7%BB%B4%E7%A0%81.png" alt="二维码"></div>
                <div class="reward-desc">📱 微信扫一扫领取5元红包</div>
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
                
                let hideToastTimeout = null;
                let showRewardTimeout = null;
                
                function showToast(msg, isLoading) {
                    if (hideToastTimeout) clearTimeout(hideToastTimeout);
                    
                    if (isLoading) {
                        toast.innerHTML = '<span class="toast-spinner"></span> ' + msg;
                    } else {
                        toast.innerHTML = msg;
                    }
                    toast.classList.add('show');
                }
                
                function hideToast() {
                    toast.classList.remove('show');
                }
                
                async function copyLink() {
                    try {
                        await navigator.clipboard.writeText('https://drestryrobot.readthedocs.io/');
                        showToast('✅ 网址复制成功！快去分享吧！');
                        hideToastTimeout = setTimeout(hideToast, 3000);
                    } catch {
                        const ta = document.createElement('textarea');
                        ta.value = 'https://drestryrobot.readthedocs.io';
                        document.body.appendChild(ta);
                        ta.select();
                        document.execCommand('copy');
                        document.body.removeChild(ta);
                        showToast('✅ 网址复制成功！快去分享吧！');
                        hideToastTimeout = setTimeout(hideToast, 3000);
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
                    hideToastTimeout = setTimeout(hideToast, 3000);
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
                    if (zone.classList.contains('has-preview')) {
                        clearImage();
                    } else {
                        copyLink();
                    }
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
                    else {
                        showToast('❌ 请上传图片文件');
                        hideToastTimeout = setTimeout(hideToast, 3000);
                    }
                };
                
                fileInput.onchange = (e) => {
                    if (e.target.files?.length) handleFile(e.target.files[0]);
                };
                
                // 计算相似度：匹配的字符数占目标字符串长度的比例，同时考虑识别文本长度的惩罚
                function calculateSimilarity(ocrText, target) {
                    if (!ocrText || ocrText.length === 0) return 0;
                    
                    const lowerOcr = ocrText.toLowerCase();
                    const lowerTarget = target.toLowerCase();
                    
                    // 找出OCR文本中包含的目标字符序列（顺序匹配）
                    let matchCount = 0;
                    let targetIdx = 0;
                    
                    for (let i = 0; i < lowerOcr.length && targetIdx < lowerTarget.length; i++) {
                        if (lowerOcr[i] === lowerTarget[targetIdx]) {
                            matchCount++;
                            targetIdx++;
                        }
                    }
                    
                    // 基础相似度 = 匹配字符数 / 目标字符串长度
                    let baseSimilarity = matchCount / lowerTarget.length;
                    
                    // 长度惩罚因子：OCR文本长度与目标长度差异越大，惩罚越重
                    // 目标长度约 30 个字符，OCR文本越长，匹配率应该越低
                    const targetLen = lowerTarget.length;
                    const ocrLen = lowerOcr.length;
                    
                    let lengthPenalty = 1.0;
                    if (ocrLen > targetLen * 2) {
                        // 如果OCR文本长度超过目标长度的2倍，大幅降低相似度
                        lengthPenalty = Math.max(0, 1 - (ocrLen - targetLen * 2) / (ocrLen));
                    } else if (ocrLen < targetLen * 0.5) {
                        // 如果OCR文本太短，也适当降低
                        lengthPenalty = ocrLen / (targetLen * 0.5);
                    }
                    
                    // 最终相似度 = 基础相似度 × 长度惩罚因子
                    let finalSimilarity = baseSimilarity * lengthPenalty;
                    
                    // 确保在 0-1 之间
                    finalSimilarity = Math.min(1, Math.max(0, finalSimilarity));
                    
                    console.log(`匹配字符: ${matchCount}/${targetLen}, 基础相似度: ${(baseSimilarity*100).toFixed(1)}%, OCR长度: ${ocrLen}, 惩罚因子: ${lengthPenalty.toFixed(2)}, 最终: ${(finalSimilarity*100).toFixed(1)}%`);
                    
                    return finalSimilarity;
                }
                
                // 滑动窗口匹配，取最佳相似度
                function validate(text) {
                    if (!text) return 0;
                    
                    const target = "drestryrobot.readthedocs.io";
                    const cleanText = text.toLowerCase().replace(/[\s\n\r\t]/g, '');
                    
                    let bestSimilarity = 0;
                    const targetLen = target.length;
                    const textLen = cleanText.length;
                    
                    // 滑动窗口匹配
                    for (let i = 0; i <= Math.max(0, textLen - 10); i++) {
                        // 窗口大小从目标长度的50%到150%
                        for (let windowSize = Math.floor(targetLen * 0.5); windowSize <= Math.min(textLen - i, Math.floor(targetLen * 1.5)); windowSize++) {
                            const sub = cleanText.substring(i, i + windowSize);
                            const sim = calculateSimilarity(sub, target);
                            if (sim > bestSimilarity) bestSimilarity = sim;
                        }
                    }
                    
                    // 也检查整个文本
                    const fullSim = calculateSimilarity(cleanText, target);
                    if (fullSim > bestSimilarity) bestSimilarity = fullSim;
                    
                    return Math.round(bestSimilarity * 100);
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
                    if (hideToastTimeout) clearTimeout(hideToastTimeout);
                    if (showRewardTimeout) clearTimeout(showRewardTimeout);
                    
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
                        
                        console.log('OCR识别结果:', text);
                        
                        const sim = validate(text);
                        const passed = sim >= 60;
                        
                        if (passed) {
                            showToast(`✅ 验证成功！匹配度: ${sim}%`);
                            hideToastTimeout = setTimeout(() => {
                                hideToast();
                                rewardCard.style.display = 'block';
                                showConfetti();
                            }, 800);
                        } else {
                            showToast(`❌ 验证失败！匹配度: ${sim}%`);
                            hideToastTimeout = setTimeout(hideToast, 3000);
                        }
                    } catch (err) {
                        console.error(err);
                        showToast('❌ 识别失败，请重试');
                        hideToastTimeout = setTimeout(hideToast, 3000);
                    }
                }
                
                updateBtn();
            })();
        </script>
    </body>
    </html>


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