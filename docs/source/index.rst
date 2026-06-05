🔥 DrestryRobot
=====================================
.. raw:: html

   <style>
       /* 加载动画 */
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

       /* 响应式：电脑端显示完整文字，手机端显示精简文字 */
       .counter-text-full { display: inline; }
       .counter-text-short { display: none; }

       @media (max-width: 600px) {
           .counter-text-full { display: none; }
           .counter-text-short { display: inline; }
       }
   </style>

   <div style="text-align: center; margin: 20px 0; padding: 10px; background: #f5f5f5; border-radius: 5px;">
       <!-- 加载占位符 -->
       <div id="counter-placeholder" style="display: flex; align-items: center; justify-content: center; gap: 8px;">
           <div class="spinner"></div>
           <span>数据加载中...</span>
       </div>

       <!-- 加载完成后显示的真实内容 -->
       <div id="counter-content" style="display: none;">

           <!-- 电脑端：完整文字 -->
           <span class="counter-text-full">
               <span id="vercount_container_site_pv" style="display: none;">
                   🌐 本站总访问量：<span id="vercount_value_site_pv">0</span> 次
               </span>
               &nbsp;|&nbsp;
               <span id="vercount_container_site_uv" style="display: none;">
                   👥 本站总访客数：<span id="vercount_value_site_uv">0</span> 人
               </span>
           </span>

           <!-- 手机端：精简文字 -->
           <span class="counter-text-short">
               <span id="vercount_container_site_pv_short" style="display: none;">
                   🌐 访问量：<span id="vercount_value_site_pv">0</span> 次
               </span>
               &nbsp;|&nbsp;
               <span id="vercount_container_site_uv_short" style="display: none;">
                   👥 访客数：<span id="vercount_value_site_uv">0</span> 人
               </span>
           </span>

       </div>
   </div>

   <script>
       // 引入 Vercount 脚本
       var script = document.createElement('script');
       script.src = 'https://vercount.one/js';
       script.defer = true;
       document.head.appendChild(script);

       // 手动控制手机端容器的显示
       var checkInterval = setInterval(function() {
           var pvContainer = document.getElementById('vercount_container_site_pv');
           // 检查电脑端容器是否已经显示
           if (pvContainer && pvContainer.style.display === 'inline') {
               // 数据已加载完成，隐藏占位符，显示真实内容
               document.getElementById('counter-placeholder').style.display = 'none';
               document.getElementById('counter-content').style.display = 'block';
               
               // 手动将手机端容器的样式也设置为显示
               var pvContainerShort = document.getElementById('vercount_container_site_pv_short');
               var uvContainerShort = document.getElementById('vercount_container_site_uv_short');
               if (pvContainerShort) pvContainerShort.style.display = 'inline';
               if (uvContainerShort) uvContainerShort.style.display = 'inline';
               
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
