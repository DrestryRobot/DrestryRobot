Git
=======
.. contents:: 目录

Git
-----
Git，是一个代码版本管理工具。可将Github代码储存库克隆至本地Git仓库，在本地对代码进行编辑后，先将代码提交到本地Git仓库，再从本地Git仓库将暂存的修改的代码推送到Github代码储存库，同时也可通过Git将Github代码储存库最新代码拉取更新到本地。

Git安装
--------
直接从 `Git官网 <https://git-scm.com/downloads>`_ 下载即可。

Git指令
----------
记住几条简单的命令行指令即可，在Git Bash命令行工具中执行这些指令。

- 克隆

.. code:: bash
    
    git clone <github代码库地址>

- 拉取

.. code:: bash

    git pull

- 暂存

.. code:: bash

    git add .

- 提交

.. code:: bash

    git commit -m "修改了什么"

- 推送

.. code:: bash

    git push

- 状态

.. code:: bash

    git status

- 帮助

.. code:: bash

    git help

Git使用
--------
1、使用Git前请先完成 **Git安装**

2、打开GitHub存储库 **Code页面** ，点击 **Code** 复制 **HTTPS** 或 **SSH** 链接

3、打开本地文件夹，右键点击 **Git Bash Here**

4、在 **Git Bash** 中运行 **"git clone <HTTPS或SSH链接>"**，例如：

.. code:: bash

    git clone https://github.com/DrestryRobot/DrestryRobot.git

    git clone git@github.com:DrestryRobot/DrestryRobot.git

5、本地文件夹通过克隆生成 **Git本地仓库** 文件夹

6、修改 **Git本地仓库** 文件夹中的文件，修改完成后开始使用Git上传

7、选中 **Git本地仓库** 文件夹，右键点击 **Git Bash Here**

8、在 **Git Bash** 中依次运行以下指令：

.. code:: bash

    git add .

    git commit -m "修改了什么"

    git push

9、指令完成运行，即上传成功

Git配合VS Code使用
-------------------
1、使用Git前请先完成 **Git安装**

2、打开GitHub存储库 **Code页面** ，点击 **Code** 复制 **HTTPS** 或 **SSH** 链接

3、打开本地文件夹，右键点击 **Git Bash Here**

4、在 **Git Bash** 中运行 **"git clone <HTTPS或SSH链接>"**，例如：

.. code:: bash

    git clone https://github.com/DrestryRobot/DrestryRobot.git

    git clone git@github.com:DrestryRobot/DrestryRobot.git

5、本地文件夹通过克隆生成 **Git本地仓库** 文件夹

6、将 **Git本地仓库** 文件夹添加到VS Code工作区

7、修改 **Git本地仓库** 文件夹中的文件，修改完成后开始使用Git上传

8、打开与 **资源管理器** 同目录的 **源代码管理** ， 点击完成Git配置

.. note::

    VS Code会自动扫描Git本地仓库，并链接远程储存库

9、**更改框** 中填写修改信息，然后点击 **提交** ，最后点击 **同步更改** ，即上传成功

