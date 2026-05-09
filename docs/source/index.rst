DrestryRobot
==============

基本介绍
-------------
DrestryRobot是一个机器人开发知识库，其涵盖了机器人开发所需要用到的各类技术知识和软件工具。

核心理念
-------------
DrestryRobot由Dream、Struggle、Youth和Robot组成，是一个热爱于机器人开发、有梦想、敢奋斗、充满青春活力的团队。

编撰原则
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
   :caption: 内容目录
   :glob:

   *

留言评论
-------------
.. raw:: html

   <!-- Artalk 评论系统 -->
   <link href="https://unpkg.com/artalk@2/dist/Artalk.css" rel="stylesheet">
   <div id="Comments"></div>
   <script>
     (function() {
       // 轮询检查 Artalk 是否已加载
       function initArtalk() {
         if (typeof Artalk !== 'undefined') {
           // Artalk 已加载，进行初始化
           new Artalk({
             el: '#Comments',
             pageKey: window.location.pathname,
             pageTitle: document.title,
             server: 'https://comment.drestryrobot.cn',
             site: 'DrestryRobot',
           });
         } else {
           // 如果还没加载，100ms 后再试
           setTimeout(initArtalk, 100);
         }
       }

       // 加载 Artalk 脚本
       var script = document.createElement('script');
       script.src = 'https://unpkg.com/artalk@2/dist/Artalk.js';
       script.onload = initArtalk;
       script.onerror = function() {
         console.error('Artalk.js 加载失败，请检查网络');
       };
       document.head.appendChild(script);
     })();
   </script>