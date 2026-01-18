控制 Qt
==================

Qt入门
---------
Qt是一个跨平台的应用程序开发软件，主要是基于C++的开发，也有一部分基于Python的。

一个基本的Qt项目工程主要包括如下部分：

.. list-table:: 
   :header-rows: 1
   :widths: 20 20 60

   * - 文件名
     - 文件类型
     - 描述
   * - untitled.pro
     - 项目文件
     - Qt 的工程配置文件，定义编译规则、包含的模块、资源等
   * - main.cpp
     - 源文件
     - 程序入口，通常包含 QApplication 初始化和主窗口显示
   * - mainwindow.h
     - 头文件
     - 主窗口类的声明，定义界面逻辑和槽函数接口
   * - mainwindow.cpp
     - 源文件
     - 主窗口类的实现，处理 UI 事件、信号与槽连接等
   * - mainwindow.ui
     - UI 文件
     - 使用 Qt Designer 生成的 XML 格式界面布局文件

QT是一款用于C++应用程序开发的软件,通过创建带窗口的项目,使用默认选项和编译器,生成基本的项目框架。在.ui文件中编辑界面,在.cpp文件中编写程序逻辑,最终实现主程序的运行。

▷00:01 QT简介

QT用于C++应用程序开发,包括欢迎界面、编辑界面等。

▷00:15 创建项目

创建带窗口的项目,使用默认qmake选项,选择编译器。

▷00:44 项目框架

项目框架包括.pro文件、main.c、mainwindow.c、.h和.ui文件,可编辑界面和编写程序逻辑。

▷01:30 运行项目

运行项目,渲染出一个空窗口。

.. raw:: html

   <div style="width: 100%; text-align: center;">
       <video width="100%" controls>
           <source src="https://drestryrobot.oss-cn-shanghai.aliyuncs.com/Qt%E5%85%A5%E9%97%A8.mp4" type="video/mp4">
       </video>
   </div>

视频来源：自制

上传时间：2026年01月11日

  






