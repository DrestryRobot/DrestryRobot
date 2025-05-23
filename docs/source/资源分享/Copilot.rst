Copilot
===========

Copilot
----------
Copilot，是微软开发的一款AI对话工具，基于GPT4大语言模型。

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