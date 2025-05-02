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
          background: rgba(255, 255, 255, 0.85); /* 增加透明度 */
          border-radius: 16px;
          padding: 10px;
          width: 220px;
          position: fixed;
          bottom: 20px;
          left: 50%;
          transform: translateX(-50%);
          box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
          transition: background 0.3s, color 0.3s;
      }

      /* 让文字居左 */
      .info {
          font-size: 16px;
          font-weight: bold;
          color: #222; /* 稍深的默认字体颜色 */
          margin: 8px 5px;
          text-align: left;
      }

      /* 适配夜间模式 */
      @media (prefers-color-scheme: dark) {
          .weather-card {
              background: rgba(30, 30, 30, 0.85); /* 调整暗色背景的透明度 */
              color: #F3F3F3;
          }
          .info {
              color: #F3F3F3;
          }
      }
   </style>

   <script>
      function updateTime() {
          let now = new Date();
          let timeString = now.toLocaleString();
          document.getElementById("time").innerText = `⏰ 时间: ${timeString}`;
      }

      // 获取天气信息（不获取位置）
      fetch("https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&current_weather=true")
         .then(response => response.json())
         .then(weatherData => {
            let temperature = weatherData.current_weather.temperature;
            let weatherCode = weatherData.current_weather.weathercode;

            // 温度表情符号映射
            let tempEmoji = temperature <= 0 ? "❄" :
                            temperature <= 15 ? "🥶" :
                            temperature <= 25 ? "😊" :
                            temperature <= 35 ? "😅" : "🔥";

            // 天气代码映射
            let weatherMap = {
               0: "☀ 晴朗", 1: "🌤 多云", 2: "☁ 阴天", 3: "🌧 小雨",
               45: "🌫 雾霾", 48: "🌫 大雾", 51: "🌦 局部小雨",
               61: "🌧 中雨", 63: "⛈ 雷雨", 71: "❄ 小雪", 75: "❄ 暴雪"
            };

            let weatherDescription = weatherMap[weatherCode] || "🌍 天气数据未知";

            document.getElementById("weather").innerText = `${tempEmoji} 温度: ${temperature}°C | ${weatherDescription}`;
         })
         .catch(error => {
            document.getElementById("weather").innerText = `❌ 无法获取天气信息: ${error}`;
         });

      // 定时更新时间
      setInterval(updateTime, 1000);
   </script>

   <!-- 天气信息卡片 -->
   <div class="weather-card">
       <p id="time" class="info">⏰ 时间加载中...</p>
       <p id="weather" class="info">🌤 天气数据加载中...</p>
   </div>
