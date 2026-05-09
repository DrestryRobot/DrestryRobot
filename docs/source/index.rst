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

   <!-- Artalk 样式 -->
   <link href="https://comment.drestryrobot.cn/artalk/Artalk.css" rel="stylesheet">
   <!-- 评论容器 -->
   <div id="Comments"></div>
   
   <!-- 自包含的评论区初始化脚本 -->
   <script>
     (function() {
       // 1. 创建一个 script 标签来加载 Artalk 的核心 JS
       var script = document.createElement('script');
       script.src = 'https://comment.drestryrobot.cn/artalk/Artalk.js';
       // 2. 确保脚本加载完成后再进行初始化
       script.onload = function() {
         // 3. 显式检查 Artalk 是否存在于全局对象 (window)
         if (window.Artalk && typeof window.Artalk === 'function') {
           // 4. 一切就绪，创建 Artalk 实例
           new window.Artalk({
             el: '#Comments',
             pageKey: window.location.pathname,
             pageTitle: document.title,
             server: 'https://comment.drestryrobot.cn',
             site: 'DrestryRobot'
           });
         } else {
           console.error('❌ Artalk 构造函数未找到或未正确导出。');
           console.log('🔍 调试信息: window.Artalk 的类型是', typeof window.Artalk, '值为', window.Artalk);
         }
       };
       
       // 5. 脚本加载失败时的错误处理
       script.onerror = function() {
         console.error('❌ 无法加载 Artalk JS 文件，请检查网络或路径');
       };
       
       // 6. 将 script 标签添加到页面，开始加载
       document.head.appendChild(script);
     })();
   </script>