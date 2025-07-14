IsaacLab
==========
.. contents:: 目录

IsaacLab
------------------
IsaacLab，是一个统一的、模块化的机器人学习框架，旨在简化机器人研究中的常见工作流程（如强化学习、从演示中学习和运动规划）。它基于NVIDIA Isaac Sim构建，利用最新的模拟功能实现照片级逼真场景，以及快速高效的模拟。

IsaacLab安装
---------------
推荐使用本方法安装IsaacSim和IsaacLab，不用下载安装包，终端运行指令即可完成下载、安装。

官网教程🔗：https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/pip_installation.html

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

IsaacLab资产包
---------------
IsaacLab资产包和IsaacSim资产包是一样的，只不过配置方法有些不同。

CSDN教程🔗：https://blog.csdn.net/qq_45906972/article/details/146094971

配置教程：

- 配置前先完成 `IsaacSim资产包🔗 <https://drestryrobot.readthedocs.io/IsaacSim.html#isaacsim>`_ 相关教程
- 打开配置文件

.. code:: bash

	/home/<username>/IsaacLab/source/isaaclab/isaaclab/utils/assets.py

- 找到这行代码 

.. code:: bash

	NUCLEUS_ASSET_ROOT_DIR = carb.settings.get_settings().get("/persistent/isaac/asset_root/cloud")

- 修改这行代码

.. code:: bash

	NUCLEUS_ASSET_ROOT_DIR = ("/home/<username/isaacsim_assets/Assets/Isaac/4.5")
	
- 保存配置文件，即完成IsaacLab资产包配置

IsaacLab疑难解答
------------------
.. error:: 

	AttributeError: 'Articulation' object has no attribute '_data'. Did you mean: 'data'?

.. hint:: 
	
	请访问🔗：https://github.com/isaac-sim/IsaacLab/discussions/623

.. error:: 
	
	AttributeError: 'NoneType' object has no attribute 'GetPath'?

.. hint:: 

	出现这样的报错信息，表示IsaacLab资产包未正确配置，按照 `IsaacLab资产包🔗 <https://drestryrobot.readthedocs.io/IsaacLab.html#isaaclab>`_ 相关教程进行配置即可。