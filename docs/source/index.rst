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

       @media (min-width: 601px) {
           .mobile-text { display: none; }
           .desktop-text { display: inline; }
       }
       @media (max-width: 600px) {
           .mobile-text { display: inline; }
           .desktop-text { display: none; }
       }
   </style>

   <div style="text-align: center; margin: 20px 0; padding: 10px;">

       <div id="counter-placeholder" style="display: flex; align-items: center; justify-content: center; gap: 8px;">
           <div class="spinner"></div>
           <span>数据加载中...</span>
       </div>

       <div id="counter-content" style="display: none;">
           <span id="vercount_container_site_pv" style="display: none;">
               <span class="desktop-text">🌐 本站总访问量: </span>
               <span class="mobile-text">🌐 访问量: </span>
               <span id="vercount_value_site_pv">0</span> 次
           </span>
           &nbsp;|&nbsp;
           <span id="vercount_container_site_uv" style="display: none;">
               <span class="desktop-text">👥 本站总访客数: </span>
               <span class="mobile-text">👥 访客数: </span>
               <span id="vercount_value_site_uv">0</span> 人
           </span>
       </div>
   </div>

   <script>
       var script = document.createElement('script');
       script.src = 'https://vercount.one/js';
       script.defer = true;
       document.head.appendChild(script);

       var checkInterval = setInterval(function() {
           var pvContainer = document.getElementById('vercount_container_site_pv');
           if (pvContainer && pvContainer.style.display === 'inline') {
               document.getElementById('counter-placeholder').style.display = 'none';
               document.getElementById('counter-content').style.display = 'block';
               clearInterval(checkInterval);
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
