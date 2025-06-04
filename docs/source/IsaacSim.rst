IsaacSim
==========
.. contents:: 目录

What Is Isaac Sim?
------------------
NVIDIA Isaac Sim™ is a reference application built on NVIDIA Omniverse that enables developers to develop, simulate, and test AI-driven robots in physically-based virtual environments.
IsaacSim，是一个机器人仿真软件，最新版本是4.5.0，从英伟达官网下载安装后，可在该平台上构建机器人仿真场景环境，通过编写python库代码对机器人进行控制。

Pip安装IsaacSim和IsaacLab
-------------------------
推荐使用本方法安装IsaacSim和IsaacLab，不用下载安装包，终端运行指令即可完成下载、安装。

官网教程：https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/pip_installation.html

安装步骤：(linux终端运行以下命令安装)

- 安装pip环境

.. code:: bash

	# 下载安装pip
	sudo apt install python3-pip

	# 检查pip安装
	pip --version # 运行出现pip版本即安装成功，反之未成功

- 安装conda环境

.. code:: bash

	# 下载安装conda
	wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh 
	bash Miniconda3-latest-Linux-x86_64.sh

	# 配置环境变量
	echo 'export PATH=~/anaconda3/bin:$PATH' >> ~/.bashrc
	source ~/.bashrc

	# 检查conda安装
	conda --version  # 运行出现conda版本即安装成功，反之未成功

- 激活conda环境

.. code:: bash

	# 创建env_isaaclab环境
	conda create -n env_isaaclab python=3.10

	# 激活env_isaaclab环境
	conda activate env_isaaclab 

- 安装PyTorch

.. code:: bash

	pip install torch==2.5.1 torchvision==0.20.1 --index-url https://download.pytorch.org/whl/cu118

- 安装isaacsim

.. code:: bash

	# 升级pip至最新版
	pip install --upgrade pip 

	# 下载安装isaacsim
	pip install 'isaacsim[all,extscache]==4.5.0' --extra-index-url https://pypi.nvidia.com 

- 测试isaacsim

.. code:: bash

	# 激活env_isaaclab环境
	conda activate env_isaaclab 

	# 打开IsaacLab文件夹目录
	cd IsaacLab 

	# 打开isaacsim
	isaacsim 

- 安装git

.. code:: bash

	# 下载安装git
	sudo apt install git 

	# 检查git安装
	git --version # 运行出现git版本即安装成功，反之未成功

- 克隆isaaclab

.. code:: bash

	# SSH方法
	git clone git@github.com:isaac-sim/IsaacLab.git

	# HTTPS方法
	git clone https://github.com/isaac-sim/IsaacLab.git

- 安装isaaclab

.. code:: bash

	# 激活env_isaaclab环境
	conda activate env_isaaclab 
	
	# 打开IsaacLab文件夹目录
	cd IsaacLab

	# 切换国内镜像源（可选）
	mkdir -p ~/.pip
	echo "[global]" > ~/.pip/pip.conf
	echo "index-url = https://pypi.tuna.tsinghua.edu.cn/simple" >> ~/.pip/pip.conf

	# 安装isaaclab
	./isaaclab.sh --install

- 测试isaaclab

.. code:: bash

	# 激活env_isaaclab环境
	conda activate env_isaaclab 

	# 打开IsaacLab文件夹目录
	cd IsaacLab 

	# 测试指令一
	./isaaclab.sh -p scripts/tutorials/00_sim/create_empty.py

	# 测试指令二
	python scripts/tutorials/00_sim/create_empty.py

IsaacSim资产包
----------------
资产包下载
~~~~~~~~~~~~~~~~~~
百度网盘下载链接🔗：https://pan.baidu.com/s/1H0BrGP3T-2Sm5rB-56RkOg?pwd=0000

文件目录：

- isaac-sim-assets-1@4.5.0-rc.36+release.19112.f59b3005.zip
- isaac-sim-assets-2@4.5.0-rc.36+release.19112.f59b3005.zip
- isaac-sim-assets-3@4.5.0-rc.36+release.19112.f59b3005.zip

下载安装方法
~~~~~~~~~~~~~~~~~~
官网教程🔗：https://docs.isaacsim.omniverse.nvidia.com/latest/installation/install_faq.html#isaac-sim-setup-assets-content-pack

安装步骤：

- 下载 `资产包 <https://pan.baidu.com/s/1H0BrGP3T-2Sm5rB-56RkOg?pwd=0000>`_ 🔗，移动到"/home/<username>/Downloads"文件夹
- 安装资产包

.. code:: bash

	mkdir ~/isaacsim_assets
	cd ~/Downloads
	unzip "isaac-sim-assets-1@4.5.0-rc.36+release.19112.f59b3005.zip" -d ~/isaacsim_assets
	unzip "isaac-sim-assets-2@4.5.0-rc.36+release.19112.f59b3005.zip" -d ~/isaacsim_assets
	unzip "isaac-sim-assets-3@4.5.0-rc.36+release.19112.f59b3005.zip" -d ~/isaacsim_assets

- 打开配置文件

.. code:: bash

	# 路径一
	/home/<username>/isaacsim/apps/isaacsim.exp.base.kit

	# 路径二
	/home/<username>/miniconda3/envs/env_isaaclab/lib/python3.10/site-packages/isaacsim/apps/isaacsim.exp.base.kit

	注意“<username>”需要修改为自己的Linux用户名

- 修改配置文件，文件末尾添加以下代码

.. code:: bash

	[settings]
	persistent.isaac.asset_root.default = "/home/<username>/isaacsim_assets/Assets/Isaac/4.5"
	exts."isaacsim.asset.browser".folders = [
		"/home/<username>/isaacsim_assets/Assets/Isaac/4.5/Isaac/Robots",
		"/home/<username>/isaacsim_assets/Assets/Isaac/4.5/Isaac/People",
		"/home/<username>/isaacsim_assets/Assets/Isaac/4.5/Isaac/IsaacLab",
		"/home/<username>/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props",
		"/home/<username>/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments",
		"/home/<username>/isaacsim_assets/Assets/Isaac/4.5/Isaac/Materials",
		"/home/<username>/isaacsim_assets/Assets/Isaac/4.5/Isaac/Samples",
		"/home/<username>/isaacsim_assets/Assets/Isaac/4.5/Isaac/Sensors",
	]

使用Extension进行编程
-------------------------
使用Extension进行编程，实际使用的是IsaacSim的Extension Template Generator（扩展模板生成器）开发工具。扩展模板生成器有四种模板可供使用，分别是：
- Load Scenario Template（加载场景模板）
- Scripting Template（脚本模板）
- Configuration Tooling Template（配置工具模板）
- UI Component Library Template（UI组件库模板）

官方教程🔗：https://docs.isaacsim.omniverse.nvidia.com/latest/utilities/extension_template_generator.html

使用方法：

- 新建Extensions文件夹
	- 位置随意，但一定要保证是空文件夹，否则IsaacSim会崩掉
	- 用来储存后面用Extension Template Generator生成的扩展
- 使用Extension Template Generator生成扩展
