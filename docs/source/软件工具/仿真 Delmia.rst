仿真 Delmia
==================

Delmia入门
------------
Delmia是一个数字化制造软件平台，主要用于工业运营的虚拟仿真、流程优化和制造执行管理。

Delmia界面比较复古，但是功能极其强大，比较常用的功能包括最简单的零件绘制、设备构建、流程仿真等。

零件绘制就是最基本的三维建模，设备构建是将装配体（例如机械臂）通过配合关系、运动学原理等构建为可动可仿真的机械装置，而流程仿真顾名思义，就是构建基于机械装置的数字化制造场景进行仿真，以优化流程。

如何快速上手Delmia软件,包括软件配置、文件类型、视图操作、对齐视点与指南针、文件架构与编辑模式以及其他操作。通过学习这些基本操作,可以更好地使用Delmia软件进行设计和仿真。

▷00:04 软件配置

自定义快捷操作,包括常用的菜单项和工具栏操作。

▷01:42 文件类型

介绍了Demo中支持的文件类型,包括Pad、process、product和Pro size。

▷03:21 视图操作

视图操作依靠中键,包括移动、缩放和旋转。

▷04:10 对齐视点与指南针

对齐视点和指南针操作,用于快速定位和移动对象。

▷05:33 文件架构与编辑模式

文件架构和编辑模式,双击进入不同的编辑页面。

▷09:29 其他操作

隐藏操作可通过右下角小箭头拖出。

.. raw:: html

   <div style="width: 100%; text-align: center;">
       <video width="100%" controls>
           <source src="https://drestryrobot.oss-cn-shanghai.aliyuncs.com/Delmia%E5%85%A5%E9%97%A8.mp4" type="video/mp4">
       </video>
   </div>

视频来源：自制

上传时间：2026年01月11日

Delmia机械装置
----------------
如何在Delmia中生成库卡机器人的机械装置,包括导入STP模型、删除不必要模块、定义坐标系、组装各部件、设置旋转关系、进行运动学正解和更改TCP点。通过这些步骤,可以在Delmia中搭建机器人的机械装置,并实现对机器人运动的模拟和分析。

▷00:02 引言

▷00:26 基座

导入STP模型,删除不必要模块,将机器人分为7个模块,新建product文件,处理零件,定义坐标系。

▷ 02:29 Link1

导入link1,定义坐标系,保存为Link1.CATProduct模块。

▷03:43 Link2

导入link2,定义坐标系,保存为Link2.CATProduct模块。

▷04:58 Link3

导入link3,定义坐标系,保存为Link3.CATProduct模块。

▷06:18 Link4

导入link4,定义坐标系,保存为Link4.CATProduct模块。

▷07:15 Link5

导入link5,定义坐标系,保存为Link5.CATProduct模块。

▷08:20 Link6

导入link6,定义坐标系,保存为Link6.CATProduct模块。

▷09:32 机械装置的组装与模拟

新建product模块,导入所有product模块,生成机械装置,设置旋转关系,模拟机械装置。

▷11:45 运动学正解

点击运动学正解工具,创建正运动学,设置命令,运行仿真。

▷13:47 TCP点的更改

新建process,导入机器人和工具,定义坐标系,通过捕捉工具对齐坐标系,更改TCP点。

.. raw:: html

   <div style="width: 100%; text-align: center;">
       <video width="100%" controls>
           <source src="https://drestryrobot.oss-cn-shanghai.aliyuncs.com/Delmia%E6%9C%BA%E6%A2%B0%E8%A3%85%E7%BD%AE.mp4" type="video/mp4">
       </video>
   </div>

视频来源：自制

上传时间：2026年01月11日

