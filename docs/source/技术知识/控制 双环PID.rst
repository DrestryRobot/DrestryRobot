控制 双环PID
===============

双环PID
----------
双环PID控制在无人机高度控制中的应用。单环PID控制可能导致加速度过大,而双环PID通过引入速度环,限制速度,使无人机上升过程更平稳,避免水洒出。

▷00:00 引言

▷00:10 单环PID

以无人机为例,单环PID通过位置偏差计算电机电流,实现高度控制,但加速度变化大,可能导致水洒出。

▷01:49 双环PID

双环PID引入速度环,限制速度,避免加速度过大,使无人机上升过程更平稳。

.. raw:: html

   <div style="width: 100%; text-align: center;">
       <video width="100%" controls>
           <source src="https://drestryrobot.oss-cn-shanghai.aliyuncs.com/%E5%8F%8C%E7%8E%AFPID.mp4" type="video/mp4">
       </video>
   </div>

视频来源：自制

上传时间：2026年01月05日