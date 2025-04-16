YRobot
======
版本：2025.04.16

1 概述
-------
YRobot（青春机器人），功能为家务机器人（简称“家务机”），定位为科技时代新家电产品，拥有移动底盘、升降平台和抓取手臂等类人特征机构，可逐步实现整理、清洁、陪伴等智能家务功能。

2 技术
-------
2.1 机械
~~~~~~~~
2.1.1 组成
^^^^^^^^^^
全向移动底盘、竖直升降平台、左右抓取手臂

2.1.2 移动
^^^^^^^^^^
**全向轮组**、**自适应底盘**

2.1.3 升降
^^^^^^^^^^
**线性导轨**、**手臂基座**

2.1.4 抓取
^^^^^^^^^^
**多自由度手臂**、**抓取机构**

2.1.5 选型
^^^^^^^^^^
.. list-table::
   :header-rows: 1
   :widths: 1 2 2 2 2

   * - 序号
     - 名称
     - 型号
     - 品牌
     - 链接
   * - 1
     - 全向轮
     - OMNIA™全向轮
     - Rotacaster
     - [OMNIA™全向轮](https://www.hi-robot.com.cn/Product-Omniwheel/OMNIA_Wheel_CN.html)
   * - 2
     - 线性导轨
     - HGW15CC, MSA15A, BRH15A
     - HIWIN, PMI, ABBA
     - [直线导轨型号大全](http://forrun.net/article-zhixiandaoguixinghaodaqu.html)
   * - 3
     - 轮组电机
     - MXUS鑫峰48V500W
     - Chamrider
     - [电机轮组](https://m.1688.com/brand/-b5e7bbfac2d6d7e9.html)
   * - 4
     - 关节电机
     - GO-M8010-6
     - Unitree Robotics
     - [GO Motor](https://www.unitree.com/cn/go1/motor/)
   * - 5
     - 直线电机
     - Yaskawa, Tecnotion, Hiwin
     - 安川, 泰科诺, 上银
     - [直线电机品牌排行榜](https://www.chinabgao.com/top/brand/99823.html)
   * - 6
     - 梯形丝杆
     - THK 梯形丝杠
     - THK
     - [THK 梯形丝杠](https://www.mechtool.cn/catalog/catalog_thkscrewnut.html)
   * - 7
     - 关节电机
     - SETZ120系列
     - SEMOTOR
     - [SETZ120系列关节电机](https://semotoren.com/cnproducts/20-SETZ120%20series%20joint%20motor.html)

.. note::
   1. 选型均为demo版本，实际选型根据具体需求进行调整。

2.2 控制
~~~~~~~~
2.2.1 硬件
^^^^^^^^^^
.. list-table::
   :header-rows: 1
   :widths: 1 2 2 2 2

   * - 序号
     - 名称
     - 型号
     - 品牌
     - 链接
   * - 1
     - 内置电池
     - 
     - 
     - 
   * - 2
     - 控制器
     - 
     - 
     - 
   * - 3
     - 电机驱动
     - 
     - 
     - 
   * - 4
     - 电源线缆
     - 
     - 
     - 
   * - 5
     - 信号线缆
     - 
     - 
     - 
   * - 6
     - 按键开关
     - 
     - 
     -     

2.2.2 软件
^^^^^^^^^^


2.3 算法
~~~~~~~~
2.3.1 硬件
^^^^^^^^^^
.. list-table::
   :header-rows: 1
   :widths: 1 2 2 2 2

   * - 序号
     - 名称
     - 型号
     - 品牌
     - 链接
   * - 1
     - 3D雷达
     - Mid360
     - 大疆
     - 
   * - 2
     - 深度相机
     - Intersense D435i
     - Inter
     - 
   * - 3
     - 计算平台
     - NX
     - NVIDIA
     - 

2.3.2 软件
^^^^^^^^^^

2.3.3 代码（demo）
^^^^^^^^^^^^^^^^^^
::
    
    //Python
    print("Hello, YRobot")    

    //C
    #include <stdio.h>
    int main() {
        printf("Hello, YRobot\n");
        return 0;
    }

    //C++
    #include <iostream>
    int main() {
        std::cout << "Hello, YRobot" << std::endl;
        return 0;
    }

    //Java
    public class Main {
        public static void main(String[] args) {
            System.out.println("Hello, YRobot");
        }
    }

2.4 仿真
~~~~~~~~
.. note::
   1. 机械臂的运动学和动力学模型需要在仿真环境中进行验证。
   2. 强化学习算法的训练和测试需要在仿真环境中进行，以确保安全性和有效性。

3 规划
-------
.. list-table::
   :header-rows: 1
   :widths: 1 2 5
   
   * - 时间
     - 型号
     - 细节
   * - 2025
     - YRobot A1
     - YRobot初代原型机的设计和仿真
   * - 2026
     - 
     - 

4 商业
-------



