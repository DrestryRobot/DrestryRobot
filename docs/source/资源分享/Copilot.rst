Copilot
===========
.. contents:: 目录

Copilot
----------
Copilot，是微软开发的一款AI对话工具，基于GPT4大语言模型。国内暂时无法访问，可通过科学上网工具，或者通过下文的命令行工具访问网站。

界面介绍
--------
.. figure:: images/Copilot.png
   :alt: 主页面
   :align: center
   :width: 100%
   :class: custom-figure

网页链接
-----------
网页链接：https://copilot.microsoft.com

国内使用方法
-------------
Windows
~~~~~~~~~~
CMD命令行运行下面代码
::

    Add-Content -Path "$env:windir\System32\drivers\etc\hosts" -Value "23.212.62.244 copilot.microsoft.com"

Linux
~~~~~~~~
终端运行下面代码
::

    echo "23.212.62.244 copilot.microsoft.com" | sudo tee -a /etc/hosts

.. note::

   1. 源于第三方网站，仅作交流分享用途
