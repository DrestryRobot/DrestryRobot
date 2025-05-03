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

   <!DOCTYPE html>
   <html lang="zh">
   <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>实时天气卡片</title>
      <style>
         .weather-card {
               background: rgba(255, 255, 255, 0.85);
               border-radius: 16px;
               padding: 10px;
               width: 260px;
               position: fixed;
               bottom: 20px;
               left: 50%;
               transform: translateX(-50%);
               box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
               transition: background 0.3s, color 0.3s;
         }

         .info {
               font-size: 16px;
               font-weight: bold;
               color: #222;
               margin: 8px 5px;
               text-align: left;
         }

         @media (prefers-color-scheme: dark) {
               .weather-card {
                  background: rgba(60, 60, 60, 0.85);
                  color: #F3F3F3;
               }
               .info {
                  color: #F3F3F3;
               }
         }
      </style>
   </head>
   <body>

      <div class="weather-card">
         <p id="time" class="info">⏰ 时间加载中...</p>
         <p id="location" class="info">📍 位置加载中...</p>
         <p id="weather" class="info">🌤 天气数据加载中...</p>
      </div>

      <script>
         function updateTime() {
               let now = new Date();
               let timeString = now.toLocaleString();
               document.getElementById("time").innerText = `⏰ 时间: ${timeString}`;
         }

         async function fetchWeather(lat, lon) {
               let apiKey = "fc86d110601a62e0d4d77e3d982c0a4c"; // 你的 OpenWeatherMap API Key
               let weatherUrl = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apiKey}&units=metric&lang=zh_cn`;

               try {
                  let response = await fetch(weatherUrl);
                  let weatherData = await response.json();
                  displayWeather(weatherData);
               } catch {
                  document.getElementById("weather").innerText = "❌ 无法获取天气信息，使用默认北京天气";
                  fetchWeather(39.9042, 116.4074); // 北京经纬度
               }
         }

         function displayWeather(weatherData) {
               let temperature = parseFloat(weatherData.main.temp).toFixed(1);
               let weatherCode = weatherData.weather[0].id;

               let tempEmoji = temperature <= 0 ? "❄" :
                              temperature <= 15 ? "🥶" :
                              temperature <= 25 ? "😊" :
                              temperature <= 35 ? "😅" : "🔥";

               let weatherMap = {
                  800: "☀ 晴朗", 801: "🌤 少云", 802: "⛅ 局部多云",
                  803: "☁ 阴天", 804: "☁ 多云",
                  500: "🌦 小雨", 501: "🌧 中雨", 502: "⛈ 大雨",
                  511: "❄ 冻雨", 600: "❄ 小雪", 601: "❄ 中雪",
                  602: "❄ 暴雪", 701: "🌫 雾霾", 781: "🌪 龙卷风"
               };

               let weatherDescription = weatherMap[weatherCode] || "🌍 天气数据未知";
               document.getElementById("weather").innerText = `${tempEmoji} 温度: ${temperature}°C | ${weatherDescription}`;
         }

         async function getLocationAndFetchWeather() {
               try {
                  let response = await fetch("https://ipinfo.io/json");
                  let data = await response.json();
                  let city = data.city || "北京";
                  let country = data.country || "中国";
                  let latlon = data.loc.split(",");

                  document.getElementById("location").innerText = `📍 位置: ${city}, ${country}`;
                  fetchWeather(latlon[0], latlon[1]);
               } catch {
                  document.getElementById("location").innerText = "📍 位置: 北京，中国";
                  fetchWeather(39.9042, 116.4074);
               }
         }

         setInterval(updateTime, 1000);
         getLocationAndFetchWeather();
      </script>

   </body>
   </html>




