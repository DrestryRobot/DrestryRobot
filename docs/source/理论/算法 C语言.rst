算法 C语言
==================
`点击这里下载 <https://drestryrobot.oss-cn-shanghai.aliyuncs.com/C%E8%AF%AD%E8%A8%80%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1.pdf>`_

.. raw:: html

   <iframe src="about:blank" id="pdf-frame" width="100%" height="800px" style="border: 2px solid #ccc; border-radius: 8px;"></iframe>
   
   <script>
       var iframe = document.getElementById('pdf-frame');
       var iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
       
       iframeDoc.open();
       iframeDoc.write(`
           <!DOCTYPE html>
           <html>
           <head>
               <title>PDF Viewer</title>
               <style>
                   * {
                       margin: 0;
                       padding: 0;
                       box-sizing: border-box;
                   }
                   body {
                       background: #525659;
                       font-family: sans-serif;
                   }
                   #controls {
                       position: sticky;
                       top: 0;
                       background: #333;
                       color: white;
                       padding: 10px;
                       text-align: center;
                       z-index: 100;
                   }
                   button {
                       padding: 8px 16px;
                       margin: 0 5px;
                       cursor: pointer;
                       background: #007bff;
                       color: white;
                       border: none;
                       border-radius: 4px;
                   }
                   button:hover {
                       background: #0056b3;
                   }
                   button:disabled {
                       background: #6c757d;
                       cursor: not-allowed;
                   }
                   #page-info {
                       display: inline-block;
                       margin: 0 15px;
                       color: white;
                   }
                   #pdf-container {
                       padding: 20px;
                       text-align: center;
                       min-height: 600px;
                   }
                   canvas {
                       margin: 0 auto;
                       box-shadow: 0 0 10px rgba(0,0,0,0.3);
                       background: white;
                       max-width: 100%;
                       height: auto;
                   }
                   .loading {
                       text-align: center;
                       padding: 50px;
                       color: white;
                       font-size: 18px;
                   }
                   .progress-bar {
                       width: 80%;
                       max-width: 400px;
                       height: 6px;
                       background: #444;
                       border-radius: 3px;
                       margin: 15px auto;
                       overflow: hidden;
                   }
                   .progress-fill {
                       width: 0%;
                       height: 100%;
                       background: #007bff;
                       transition: width 0.3s;
                   }
                   .error {
                       color: #ff6b6b;
                       text-align: center;
                       padding: 50px;
                       background: #333;
                       margin: 20px;
                       border-radius: 8px;
                   }
               </style>
               <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.16.105/pdf.min.js"><\/script>
           </head>
           <body>
               <div id="controls">
                   <button id="prev" disabled>上一页</button>
                   <span id="page-info">加载中...</span>
                   <button id="next" disabled>下一页</button>
                   <input type="number" id="page-input" placeholder="页码" style="width:60px; margin-left:10px;">
                   <button id="go" disabled>跳转</button>
               </div>
               <div id="pdf-container">
                   <div class="loading">
                       📄 正在加载PDF文件<br>
                       <div class="progress-bar">
                           <div class="progress-fill" id="progress-fill"></div>
                       </div>
                       <span id="progress-text">0%</span>
                   </div>
               </div>
               
               <script>
                   var url = 'https://drestryrobot.oss-cn-shanghai.aliyuncs.com/C%E8%AF%AD%E8%A8%80%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1.pdf';
                   var pdfDoc = null;
                   var currentPage = 1;
                   var totalPages = 0;
                   var scale = 1.2;
                   var loadingTask = null;
                   
                   // 更新进度
                   function updateProgress(percent) {
                       var fill = document.getElementById('progress-fill');
                       var text = document.getElementById('progress-text');
                       if (fill) fill.style.width = percent + '%';
                       if (text) text.innerText = Math.floor(percent) + '%';
                   }
                   
                   function showError(message) {
                       var container = document.getElementById('pdf-container');
                       container.innerHTML = '<div class="error"><strong>⚠️ 加载失败</strong><br>' + message + '<br><br>💡 建议：<a href="' + url + '" target="_blank">点击这里直接下载</a> 后用本地阅读器打开</div>';
                       document.getElementById('page-info').innerText = '加载失败';
                   }
                   
                   function renderPage(pageNum) {
                       if (!pdfDoc) return;
                       
                       var container = document.getElementById('pdf-container');
                       container.innerHTML = '<div class="loading">📖 渲染第 ' + pageNum + ' 页...</div>';
                       
                       pdfDoc.getPage(pageNum).then(function(page) {
                           var viewport = page.getViewport({scale: scale});
                           
                           // 限制canvas最大宽度，提高渲染速度
                           var maxWidth = container.clientWidth - 40;
                           if (viewport.width > maxWidth) {
                               scale = maxWidth / viewport.width;
                               var newViewport = page.getViewport({scale: scale});
                               canvas.height = newViewport.height;
                               canvas.width = newViewport.width;
                           } else {
                               canvas.height = viewport.height;
                               canvas.width = viewport.width;
                           }
                           
                           var canvas = document.createElement('canvas');
                           var context = canvas.getContext('2d');
                           canvas.height = viewport.height;
                           canvas.width = viewport.width;
                           
                           container.innerHTML = '';
                           container.appendChild(canvas);
                           
                           var renderContext = {
                               canvasContext: context,
                               viewport: viewport
                           };
                           
                           page.render(renderContext).promise.then(function() {
                               document.getElementById('page-info').innerHTML = '📄 第 ' + pageNum + ' / ' + totalPages + ' 页';
                               document.getElementById('prev').disabled = (pageNum <= 1);
                               document.getElementById('next').disabled = (pageNum >= totalPages);
                               document.getElementById('go').disabled = false;
                           }).catch(function(error) {
                               container.innerHTML = '<div class="error">渲染错误: ' + error.message + '</div>';
                           });
                       }).catch(function(error) {
                           container.innerHTML = '<div class="error">获取页面失败: ' + error.message + '</div>';
                       });
                   }
                   
                   function initPDF() {
                       pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.16.105/pdf.worker.min.js';
                       
                       // 配置优化参数，提高大文件加载速度
                       loadingTask = pdfjsLib.getDocument({
                           url: url,
                           cMapUrl: 'https://cdn.jsdelivr.net/npm/pdf.js-dist@2.16.105/cmaps/',
                           cMapPacked: true,
                           // 优化：禁用字体缓存（减少内存）
                           disableFontFace: false,
                           // 优化：使用本地字体
                           nativeImageDecoderSupport: 'none',
                           // 优化：设置更大的图片尺寸限制
                           maxImageSize: -1,
                           // 关键优化：启用范围请求，只加载需要的数据
                           disableRange: false,
                           disableStream: false,
                           // 进度回调
                           onProgress: function(progress) {
                               var percent = (progress.loaded / progress.total) * 100;
                               updateProgress(percent);
                           }
                       });
                       
                       loadingTask.promise.then(function(pdf) {
                           pdfDoc = pdf;
                           totalPages = pdf.numPages;
                           currentPage = 1;
                           
                           document.getElementById('page-info').innerHTML = '📄 第 1 / ' + totalPages + ' 页';
                           document.getElementById('prev').disabled = true;
                           document.getElementById('next').disabled = (totalPages <= 1);
                           
                           renderPage(currentPage);
                       }).catch(function(error) {
                           console.error('PDF加载错误:', error);
                           // 如果是CORS错误，提供友好提示
                           if (error.message.includes('CORS') || error.message.includes('cross-origin')) {
                               showError('跨域访问被阻止。请将PDF文件放在支持CORS的服务器上，或直接下载后查看。');
                           } else if (error.message.includes('range')) {
                               showError('服务器不支持范围请求，无法进行优化加载。建议直接下载。');
                           } else {
                               showError(error.message);
                           }
                       });
                   }
                   
                   // 绑定事件
                   document.getElementById('prev').addEventListener('click', function() {
                       if (pdfDoc && currentPage > 1) {
                           currentPage--;
                           renderPage(currentPage);
                       }
                   });
                   
                   document.getElementById('next').addEventListener('click', function() {
                       if (pdfDoc && currentPage < totalPages) {
                           currentPage++;
                           renderPage(currentPage);
                       }
                   });
                   
                   document.getElementById('go').addEventListener('click', function() {
                       var pageNum = parseInt(document.getElementById('page-input').value);
                       if (pdfDoc && pageNum >= 1 && pageNum <= totalPages) {
                           currentPage = pageNum;
                           renderPage(currentPage);
                       }
                   });
                   
                   // 开始加载
                   initPDF();
               <\/script>
           </body>
           </html>
       `);
       iframeDoc.close();
   </script>