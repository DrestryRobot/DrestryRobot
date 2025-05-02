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

   <style>
      /* 让天气卡片居底部中央 */
      .weather-card {
          background: rgba(255, 255, 255, 0.9);
          border-radius: 16px;
          padding: 20px;
          width: 300px;
          position: fixed;
          bottom: 20px;
          left: 50%;
          transform: translateX(-50%);
          box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
      }

      /* 让文字居左 */
      .info {
          font-size: 18px;
          font-weight: bold;
          color: #333;
          margin: 10px 0;
          text-align: left;
      }
   </style>

   <script>
      function updateTime() {
          let now = new Date();
          let timeString = now.toLocaleString();
          document.getElementById("time").innerText = `⏰ 时间: ${timeString}`;
      }

      // 获取位置
      fetch("https://ipapi.co/json/")
         .then(response => response.json())
         .then(data => {
            let city = data.city;
            let country = data.country;
            document.getElementById("location").innerText = `📍 位置: ${city}, ${country}`;

            // 使用 Open-Meteo 获取天气
            fetch(`https://api.open-meteo.com/v1/forecast?latitude=${data.latitude}&longitude=${data.longitude}&current_weather=true`)
               .then(response => response.json())
               .then(weatherData => {
                  let temperature = weatherData.current_weather.temperature;
                  let windspeed = weatherData.current_weather.windspeed;
                  document.getElementById("weather").innerText = `🌡 温度: ${temperature}°C | 💨 风速: ${windspeed}km/h`;
               })
               .catch(error => {
                  document.getElementById("weather").innerText = `❌ 无法获取天气信息: ${error}`;
               });
         })
         .catch(error => {
            document.getElementById("location").innerText = `❌ 无法获取位置信息: ${error}`;
         });

      // 定时更新时间
      setInterval(updateTime, 1000);
   </script>

   <!-- 天气信息卡片 -->
   <div class="weather-card">
       <p id="location" class="info">获取位置信息...</p>
       <p id="time" class="info">⏰ 时间加载中...</p>
       <p id="weather" class="info">🌤 天气数据加载中...</p>
   </div>



