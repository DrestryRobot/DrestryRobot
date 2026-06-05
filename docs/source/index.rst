🔥 DrestryRobot
=====================================
.. raw:: html

   <div style="text-align: center; margin: 20px 0; padding: 10px; background: #f5f5f5; border-radius: 5px;">
       <!-- 1. 加载完成前，显示“数据加载中...”的提示 -->
       <div id="counter-placeholder">
           📊 数据加载中...
       </div>

       <!-- 2. 加载完成后要显示的真实内容（初始时隐藏） -->
       <div id="counter-content" style="display: none;">
           <span id="vercount_container_site_pv" style="display: none;">
               🌐 本站总访问量：<span id="vercount_value_site_pv">0</span> 次
           </span>
           &nbsp;|&nbsp;
           <span id="vercount_container_site_uv" style="display: none;">
               👥 本站总访客数：<span id="vercount_value_site_uv">0</span> 人
           </span>
       </div>

       <!-- 3. 引入 Vercount 脚本，并添加一段自定义逻辑来切换显示 -->
       <script>
           // 先引入 Vercount 脚本
           var script = document.createElement('script');
           script.src = 'https://vercount.one/js';
           script.defer = true;
           document.head.appendChild(script);

           // 监听 Vercount 脚本是否执行完毕，通过检查其添加的全局变量或定时器
           var checkInterval = setInterval(function() {
               // 检查计数器容器是否已经从 display: none 变为显示（style.display变为"inline"）
               var pvContainer = document.getElementById('vercount_container_site_pv');
               if (pvContainer && pvContainer.style.display === 'inline') {
                   // 数据已加载完成，隐藏占位符，显示真实内容
                   document.getElementById('counter-placeholder').style.display = 'none';
                   document.getElementById('counter-content').style.display = 'block';
                   clearInterval(checkInterval); // 停止检查
               }
           }, 100); // 每 100 毫秒检查一次
       </script>
   </div>

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
