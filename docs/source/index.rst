欢迎来到DrestryRobot😃
==========================
.. raw:: html

   <div style="margin-bottom: 20px;">
       <img src="https://img.shields.io/badge/版本-2025.05.02-blue.svg" 
       alt="版本" 
       style="width:130px; 
       text-align:left; 
       display:block;">
   </div>

.. figure:: images/蓝白橙色手写体自然景观旅行分享微信公众号封面.gif
   :alt: Version
   :align: center
   :width: 100%

.. raw:: html

   <br>

"发现美，创造美"
----------------
这是一个在线网页，旨在于资源分享、技术总结、项目开发和产品展示，欢迎学习与交流！

最近更新
---------
- 2025.05.02
   - 技术总结
   - 表情符号

- 2025.05.01
   - 技术标准
   - 导纳控制
   - 负载辨识
   
- 2025.04.30
   - 机械模型
   - 网页链接
   - 老资源库
  
.. toctree::
   :maxdepth: 2
   :caption: 内容目录

   资源分享
   技术总结
   项目开发
   产品展示








.. raw:: html

   <script>
      fetch("https://ipwhois.app/json/")
         .then(response => response.json())
         .then(data => {
            document.getElementById("weather").innerText = "📍 你的位置：" + data.city + "，国家：" + data.country;
         })
         .catch(error => document.getElementById("weather").innerText = "❌ 无法获取位置信息：" + error);
   </script>

   <p id="weather">获取位置信息...</p>



