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

   <link href="https://comment.drestryrobot.cn/artalk/Artalk.css" rel="stylesheet">
   <div id="Comments"></div>
   <script>
     (function() {
       var script = document.createElement('script');
       script.src = 'https://comment.drestryrobot.cn/artalk/Artalk.js';
       script.onload = function() {
         // Artalk 是以 ES Module 形式导出的，构造函数在 default 属性中
         if (window.Artalk && window.Artalk.default) {
           new window.Artalk.default({
             el: '#Comments',
             pageKey: '/',  // 固定为根路径，确保所有设备评论互通
             pageTitle: document.title,
             server: 'https://comment.drestryrobot.cn',
             site: 'DrestryRobot'
           });
           console.log('Artalk 初始化成功');
         } else {
           console.error('Artalk 加载失败，无法找到构造函数');
         }
       };
       script.onerror = function() {
         console.error('Artalk.js 文件加载失败');
       };
       document.head.appendChild(script);
     })();
   </script>
   
留言评论
-------------
.. raw:: html

   <link href="https://comment.drestryrobot.cn/artalk/Artalk.css" rel="stylesheet">
   <div id="Comments"></div>
   <script>
     (function() {
       var script = document.createElement('script');
       script.src = 'https://comment.drestryrobot.cn/artalk/Artalk.js';
       script.onload = function() {
         // Artalk 是以 ES Module 形式导出的，构造函数在 default 属性中
         if (window.Artalk && window.Artalk.default) {
           new window.Artalk.default({
             el: '#Comments',
             pageKey: window.location.pathname,
             pageTitle: document.title,
             server: 'https://comment.drestryrobot.cn',
             site: 'DrestryRobot'
           });
           console.log('Artalk 初始化成功');
         } else {
           console.error('Artalk 加载失败，无法找到构造函数');
         }
       };
       script.onerror = function() {
         console.error('Artalk.js 文件加载失败');
       };
       document.head.appendChild(script);
     })();
   </script>