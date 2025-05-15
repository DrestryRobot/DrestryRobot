欢迎来到DrestryRobot😃
==========================
.. figure:: _images/主页面.gif
   :alt: 主页面
   :align: center
   :width: 100%
   :class: custom-figure

"发现美，创造美"
----------------
这是一个在线网页，旨在于资源分享、技术总结、项目开发和产品展示，欢迎学习与交流！

最近更新
---------
- 2025.05.15
   - `3Dfindit <https://drestryrobot.readthedocs.io/技术总结/3Dfindit.html>`_
   - `KnowMap <https://drestryrobot.readthedocs.io/_static/KnowMap/index.html>`_
      - 新增主页下方导航条快速访问
- 2025.05.14
   - `SolidWorks <https://drestryrobot.readthedocs.io/技术总结/SolidWorks.html>`_
   - `Ubuntu <https://drestryrobot.readthedocs.io/技术总结/Ubuntu.html>`_
- 2025.05.13
   - `IsaacSim <https://drestryrobot.readthedocs.io/技术总结/IsaacSim.html>`_ 
   - `IsaacLab <https://drestryrobot.readthedocs.io/技术总结/IsaacLab.html>`_ 
   - `C语言 <https://drestryrobot.readthedocs.io/技术总结/C语言.html>`_
- 2025.05.10
   - 主页面
      - 新增共同创作部分
   - 板块页面
      - 封面焕新，青春洋溢
   - 技术总结
      - 新增目录功能，支持快速跳转标题
      - 新增若干技术文档
   - RST文档
   - 六维力传感器
   - VisionMaster二次开发
- 2025.05.08
   - SiteSearch
      - 修复部分图标显示
   - TCP通信
   - 串口通信
- 2025.05.07
   - 主页面
      - 新增底部导航条，支持快速跳转至SiteSearch

.. 历史更新
.. raw:: html

   <details>
   <summary>点击查看历史更新</summary>
   <pre>
   - 2025.05.05
      - DigitalWorld
      - ModelView
      - SiteSearch
         - `SiteSearch <https://drestryrobot.readthedocs.io/_static/SiteSearch/index.html>`_ 官网导航
         - 优化界面UI设计
         - 新增和删减部分官网
   - 2025.05.04
      - SiteSearch
         - 支持快速搜索各大官网网址
         - 支持快速分类各大官网网址
         - 支持快速访问各大官网网址
   - 2025.05.03
      - DrestryRobot
         - DrestryRobot桌面应用程序
         - 软件界面自动跟随系统深浅色模式进行切换
         - 软件图标自动跟随系统深浅色模式进行切换
         - 与网页端保持一致的功能和设计
         - 支持Windows操作系统

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
   </pre>
   </details>
   <br>

更新规划
---------
- 2025.05
   - 支持中文搜索

.. toctree::
   :maxdepth: 2
   :caption: 内容目录

   资源分享
   技术总结
   项目开发
   产品展示

共同创作
---------
共同创作资源分享、技术总结板块内容，用户可通过 `Git <https://git-scm.com/>`_ + `VS Code <https://code.visualstudio.com/>`_ + `Github <https://github.com/>`_ 进行在线协同创作。

Github代码库地址：https://github.com/DrestryRobot/DrestryRobot.git

共同创作方法：
   - 使用Git克隆至本地文件夹
      - 打开本地文件夹，右键打开"Git Bash Here"工具
      - 输入"git clone https://github.com/DrestryRobot/DrestryRobot.git"，回车，等待克隆完成
   - 使用VS Code编辑本地文件夹
      - 在VS Code中打开"DrestryRobot/docs/source"
      - 打开资源分享、技术总结文件夹，新建并编辑.rst文件即可
   - 使用VS Code源代码管理上传至 `Github <https://github.com/>`_ 代码库
      - 源代码管理中先提交更改，再同步更改

投稿渠道
----------
如果你有好的资源、技术、项目或产品，欢迎投稿到邮箱：2371478179@qq.com。

根据稿件质量，给予5～15元/篇的激励，请在邮件中注明联系方式。

.. 天气卡片
.. includehtml:: _static/weather.html

.. 底部导航条
.. includehtml:: _static/quick.html
