IsaacLab
==========
.. contents:: 目录

What Is Isaac Lab?
------------------
Isaac Lab is a unified and modular framework for robot learning that aims to simplify common workflows in robotics research (such as reinforcement learning, learning from demonstrations, and motion planning). It is built on NVIDIA Isaac Sim to leverage the latest simulation capabilities for photo-realistic scenes, and fast and efficient simulation.

Pip安装IsaacSim和IsaacLab
-------------------------
推荐使用本方法安装IsaacSim和IsaacLab，不用下载安装包，终端运行指令即可完成下载、安装。

官网教程：https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/pip_installation.html

安装步骤：(linux终端运行以下命令安装)

- 安装pip环境

::

	# 下载安装pip
	sudo apt install python3-pip

	# 检查pip安装
	pip --version # 运行出现pip版本即安装成功，反之未成功

- 安装conda环境

::

	# 下载安装conda
	wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh 
	bash Miniconda3-latest-Linux-x86_64.sh

	# 配置环境变量
	echo 'export PATH=~/anaconda3/bin:$PATH' >> ~/.bashrc
	source ~/.bashrc

	# 检查conda安装
	conda --version  # 运行出现conda版本即安装成功，反之未成功

- 激活conda环境

::

	# 创建env_isaaclab环境
	conda create -n env_isaaclab python=3.10

	# 激活env_isaaclab环境
	conda activate env_isaaclab 

- 安装PyTorch

::

	pip install torch==2.5.1 torchvision==0.20.1 --index-url https://download.pytorch.org/whl/cu118

- 安装isaacsim

::

	# 升级pip至最新版
	pip install --upgrade pip 

	# 下载安装isaacsim
	pip install 'isaacsim[all,extscache]==4.5.0' --extra-index-url https://pypi.nvidia.com 

- 测试isaacsim

::

	# 激活env_isaaclab环境
	conda activate env_isaaclab 

	# 打开IsaacLab文件夹目录
	cd IsaacLab 

	# 打开isaacsim
	isaacsim 

- 安装git

::

	# 下载安装git
	sudo apt install git 

	# 检查git安装
	git --version # 运行出现git版本即安装成功，反之未成功

- 克隆isaaclab

::

	# SSH方法
	git clone git@github.com:isaac-sim/IsaacLab.git

	# HTTPS方法
	git clone https://github.com/isaac-sim/IsaacLab.git

- 安装isaaclab

::

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

::

	# 激活env_isaaclab环境
	conda activate env_isaaclab 

	# 打开IsaacLab文件夹目录
	cd IsaacLab 

	# 测试指令一
	./isaaclab.sh -p scripts/tutorials/00_sim/create_empty.py

	# 测试指令二
	python scripts/tutorials/00_sim/create_empty.py

IsaacLab资产包
---------------
IsaacLab资产包和IsaacSim资产包是一样的，只不过配置方法有些不同。

CSDN教程🔗：https://blog.csdn.net/qq_45906972/article/details/146094971

配置教程：

- 配置前先完成 `IsaacSim资产包 <https://drestryrobot.readthedocs.io/zh-cn/latest/%E6%8A%80%E6%9C%AF%E6%80%BB%E7%BB%93/IsaacSim.html#isaacsim>`_ 相关教程
- 打开配置文件

::

	/home/<username>/IsaacLab/source/isaaclab/isaaclab/utils/assets.py

- 找到这行代码 

::

	NUCLEUS_ASSET_ROOT_DIR = carb.settings.get_settings().get("/persistent/isaac/asset_root/cloud")

- 修改这行代码

::

	NUCLEUS_ASSET_ROOT_DIR = ("/home/<username/isaacsim_assets/Assets/Isaac/4.5")
	
- 保存配置文件，即完成IsaacLab资产包配置

报错信息
-----------
AttributeError: 'Articulation' object has no attribute '_data'. Did you mean: 'data'?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
https://github.com/isaac-sim/IsaacLab/discussions/623

AttributeError: 'NoneType' object has no attribute 'GetPath'?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
出现这样的报错信息，表示IsaacLab资产包未正确配置，按照 `IsaacLab资产包 <https://drestryrobot.readthedocs.io/zh-cn/latest/%E6%8A%80%E6%9C%AF%E6%80%BB%E7%BB%93/IsaacLab.html#isaaclab>`_ 相关教程进行配置即可。