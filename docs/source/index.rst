欢迎来到DrestryRobot😃
==========================
.. raw:: html

   <div style="margin-bottom: 20px;">
       <img src="https://img.shields.io/badge/版本-2025.05.03-blue.svg" 
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
- 2025.05.03
   - 主页面新增实时天气卡片
      - 打开页面5s后自动收缩为胶囊状态
      - 点击可在卡片和胶囊状态之间切换
      - 显示当前时间、位置和天气
      - 支持夜间模式
      - 使用IP定位获取位置
      - 使用WeatherAPI获取天气数据
      - 温度emoji表情符号根据温度变化
      - 天气emoji表情符号根据天气变化
      - 适配手机和电脑屏幕
   
.. raw:: html

   <details>
   <summary style="font-size: 24px; font-weight: bold;">历史更新</summary>
   <pre>
   2025.05.02
      - 技术总结
      - 表情符号

   2025.05.01
      - 技术标准
      - 导纳控制
      - 负载辨识

   2025.04.30
      - 机械模型
      - 网页链接
      - 老资源库
   </pre>
   </details>

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
               width: 250px;
               position: fixed;
               bottom: 20px;
               left: 50%;
               transform: translateX(-50%);
               box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
               transition: all 0.3s ease-in-out;
               cursor: pointer;
               text-align: left;
         }

         .info {
               font-size: 16px;
               font-weight: bold;
               color: #222;
               margin: 8px 5px;
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

         /* 灵动岛胶囊状态 */
         .capsule {
               width: var(--capsule-width, 120px);
               height: var(--capsule-height, 30px);
               border-radius: var(--capsule-radius, 20px);
               font-size: var(--capsule-font-size, 16px);
               background: var(--capsule-bg, rgba(255, 255, 255, 0.85));
               color: var(--capsule-text-color, #222);
               
               display: flex;
               justify-content: center;
               align-items: center;
               text-align: center;
               padding: var(--capsule-padding, 5px);
               cursor: pointer;
         }

         /* 夜间模式适配 */
         @media (prefers-color-scheme: dark) {
               .capsule {
                  background: var(--capsule-bg-dark, rgba(60, 60, 60, 0.85));
                  color: var(--capsule-text-dark, #F3F3F3);
               }
         }

         .hidden {
               display: none;
         }
      </style>
   </head>
   <body>

      <div class="weather-card" id="weatherCard">
         <p id="time" class="info">⏰ 时间加载中...</p>
         <p id="location" class="info">📍 位置加载中...</p>
         <p id="weather" class="info">🌤 天气数据加载中...</p>
      </div>

      <script>
         function updateTime() {
               let now = new Date();
               let fullDate = now.toLocaleString();
               let shortTime = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });

               let isCapsule = document.getElementById("weatherCard").classList.contains("capsule");
               document.getElementById("time").innerText = isCapsule ? `⏰ ${shortTime}` : `⏰ 时间: ${fullDate}`;
         }

         document.getElementById("weatherCard").addEventListener("click", function () {
               this.classList.toggle("capsule");
               document.getElementById("location").classList.toggle("hidden");
               document.getElementById("weather").classList.toggle("hidden");
               updateTime();
         });

         setInterval(updateTime, 1000);

         // 5秒后自动切换为胶囊状态
         setTimeout(function () {
               document.getElementById("weatherCard").classList.add("capsule");
               document.getElementById("location").classList.add("hidden");
               document.getElementById("weather").classList.add("hidden");
               updateTime();
         }, 5000);

         async function fetchWeather(lat, lon) {
               let apiKey = "b8690305582b46789a892207250305"; // 替换为你的 WeatherAPI Key
               let weatherUrl = `https://api.weatherapi.com/v1/current.json?key=${apiKey}&q=${lat},${lon}&lang=zh`;

               try {
                  let response = await fetch(weatherUrl);
                  let weatherData = await response.json();
                  displayWeather(weatherData);
               } catch {
                  document.getElementById("weather").innerText = "❌ 无法获取天气信息，使用默认北京天气";
                  fetchWeather(39.9042, 116.4074);
               }
         }

         function displayWeather(weatherData) {
               let temperature = Math.ceil(weatherData.current.temp_c);
               let weatherCode = weatherData.current.condition.code;

               let tempEmoji = temperature <= 0 ? "❄" :
                              temperature <= 15 ? "🥶" :
                              temperature <= 25 ? "😊" :
                              temperature <= 35 ? "😅" : "🔥";

               let weatherMap = {
                  1000: "☀ 晴朗", 1003: "🌤 少云", 1006: "⛅ 局部多云",
                  1009: "☁ 阴天", 1063: "🌦 小雨", 1183: "🌧 中雨", 1273: "⛈ 雷阵雨",
                  1210: "❄ 小雪", 1225: "❄ 暴雪", 1135: "🌫 雾霾", 1087: "🌪 雷暴"
               };

               let weatherDescription = weatherMap[weatherCode] || weatherData.current.condition.text;
               document.getElementById("weather").innerText = `${tempEmoji} 温度: ${temperature}°C | ${weatherDescription}`;
         }

         async function getLocationAndFetchWeather() {
               try {
                  let response = await fetch("https://ipinfo.io/json");
                  let data = await response.json();
                  let city = data.city || "北京";
                  let country = data.country || "中国";
                  let latlon = data.loc ? data.loc.split(",") : ["39.9042", "116.4074"];

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


