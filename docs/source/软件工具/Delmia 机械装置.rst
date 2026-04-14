Delmia 机械装置
==================
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

Delmia龙门安装机器人
----------------------
如何在Delmia的Process流程文件中,将机器人提速移动至龙门移动平台上进行安装固定。首先使用snap resource工具建立物理关系,然后使用附加工具添加父子级关系,实现机器人与龙门的移动配合。

▷00:04 建立物理关系

使用snap resource工具建立龙门与机器人的物理关系,调整参考坐标系方向。

▷01:21 添加父子级关系

使用附加工具添加龙门与机器人的父子级关系,实现移动配合。

.. raw:: html

   <div style="width: 100%; text-align: center;">
       <video width="100%" controls>
           <source src="https://drestryrobot.oss-cn-shanghai.aliyuncs.com/202604%20Delmia%E9%BE%99%E9%97%A8%E5%AE%89%E8%A3%85%E6%9C%BA%E5%99%A8%E4%BA%BA.mp4" type="video/mp4">
       </video>
   </div>

视频来源：自制

上传时间：2026年04月06日