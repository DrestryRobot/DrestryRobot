算法 C语言
==================
`点击这里下载 <https://drestryrobot.oss-cn-shanghai.aliyuncs.com/C%E8%AF%AD%E8%A8%80%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1.pdf>`_

.. raw:: html

   <!DOCTYPE html>
   <html>
   <head>
       <title>PDF Viewer - 大文件优化版</title>
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
               position: fixed;
               top: 0;
               left: 0;
               right: 0;
               background: #333;
               color: white;
               padding: 10px;
               text-align: center;
               z-index: 100;
               box-shadow: 0 2px 5px rgba(0,0,0,0.2);
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
               margin-top: 50px;
               padding: 20px;
               text-align: center;
           }
           canvas {
               margin: 0 auto;
               box-shadow: 0 0 10px rgba(0,0,0,0.3);
               background: white;
           }
           .loading {
               position: fixed;
               top: 50%;
               left: 50%;
               transform: translate(-50%, -50%);
               background: rgba(0,0,0,0.8);
               color: white;
               padding: 20px;
               border-radius: 10px;
               z-index: 1000;
           }
           .error {
               color: red;
               text-align: center;
               padding: 20px;
               margin-top: 60px;
           }
       </style>
       <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.16.105/pdf.min.js"></script>
   </head>
   <body>
       <div id="controls">
           <button id="prev" disabled>上一页</button>
           <span id="page-info">第 0 / 0 页</span>
           <button id="next" disabled>下一页</button>
           <input type="number" id="page-input" placeholder="跳转" style="width:60px; margin-left:10px;">
           <button id="go">跳转</button>
       </div>
       <div id="pdf-container"></div>
       
       <div id="loading" class="loading" style="display: none;">
           加载中... (大文件可能需要一些时间)
       </div>

       <script>
           var url = 'https://drestryrobot.oss-cn-shanghai.aliyuncs.com/C%E8%AF%AD%E8%A8%80%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1.pdf';
           
           var pdfDoc = null;
           var currentPage = 1;
           var totalPages = 0;
           var scale = 1.2;
           
           function showLoading(show) {
               document.getElementById('loading').style.display = show ? 'flex' : 'none';
           }
           
           function showError(message) {
               var container = document.getElementById('pdf-container');
               container.innerHTML = '<div class="error"><strong>加载失败：</strong><br>' + message + '<br><br>请检查：<br>1. 文件是否支持跨域访问(CORS)<br>2. 文件URL是否正确<br>3. 文件是否损坏</div>';
           }
           
           function renderPage(pageNum) {
               showLoading(true);
               
               pdfDoc.getPage(pageNum).then(function(page) {
                   var viewport = page.getViewport({scale: scale});
                   var container = document.getElementById('pdf-container');
                   
                   var canvas = document.getElementById('page-canvas');
                   if (!canvas) {
                       canvas = document.createElement('canvas');
                       canvas.id = 'page-canvas';
                       container.innerHTML = '';
                       container.appendChild(canvas);
                   }
                   
                   var context = canvas.getContext('2d');
                   canvas.height = viewport.height;
                   canvas.width = viewport.width;
                   
                   var renderContext = {
                       canvasContext: context,
                       viewport: viewport
                   };
                   
                   page.render(renderContext).promise.then(function() {
                       showLoading(false);
                       document.getElementById('page-info').innerText = '第 ' + pageNum + ' / ' + totalPages + ' 页';
                       
                       document.getElementById('prev').disabled = (pageNum <= 1);
                       document.getElementById('next').disabled = (pageNum >= totalPages);
                   }).catch(function(error) {
                       showLoading(false);
                       console.error('渲染错误:', error);
                   });
               }).catch(function(error) {
                   showLoading(false);
                   console.error('获取页面错误:', error);
               });
           }
           
           function initPDF() {
               showLoading(true);
               
               pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.16.105/pdf.worker.min.js';
               
               var loadingTask = pdfjsLib.getDocument({
                   url: url,
                   disableRange: false,
                   disableStream: false,
                   httpHeaders: {},
                   maxImageSize: -1,
                   cMapUrl: 'https://cdn.jsdelivr.net/npm/pdf.js-dist@2.16.105/cmaps/',
                   cMapPacked: true,
               });
               
               loadingTask.promise.then(function(pdf) {
                   pdfDoc = pdf;
                   totalPages = pdf.numPages;
                   currentPage = 1;
                   
                   document.getElementById('page-info').innerText = '第 1 / ' + totalPages + ' 页';
                   document.getElementById('prev').disabled = true;
                   document.getElementById('next').disabled = (totalPages <= 1);
                   
                   renderPage(currentPage);
                   showLoading(false);
               }).catch(function(error) {
                   showLoading(false);
                   console.error('PDF加载错误:', error);
                   showError(error.message);
               });
           }
           
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
           
           initPDF();
       </script>
   </body>
   </html>