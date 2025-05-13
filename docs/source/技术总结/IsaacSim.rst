Isaac Sim
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

安装步骤：

- 安装pip环境
	- 终端运行 sudo apt install python3-pip
	- 终端运行 pip --version # 运行出现pip版本即安装成功，反之未成功
- 安装conda环境
	- 终端运行 wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh # 下载miniconda
	- 终端运行 bash Miniconda3-latest-Linux-x86_64.sh # 安装miniconda
	- 配置环境变量
		- 终端运行 echo 'export PATH=~/anaconda3/bin:$PATH' >> ~/.bashrc
		- 终端运行 source ~/.bashrc
	- 终端运行 conda --version # 运行出现conda版本即安装成功，反之未成功
- 激活conda环境
	- 终端运行 conda create -n env_isaaclab python=3.10 # 创建env_isaaclab环境，isaaclab都是基于这个环境运行的
	- 终端运行 conda activate env_isaaclab # 激活env_isaaclab环境
- 安装PyTorch
	- 终端运行 pip install torch==2.5.1 torchvision==0.20.1 --index-url https://download.pytorch.org/whl/cu118
- 安装isaacsim
	- 终端运行 pip install --upgrade pip # 升级pip至最新版
	- 终端运行 pip install 'isaacsim[all,extscache]==4.5.0' --extra-index-url https://pypi.nvidia.com # 下载安装isaacsim
- 测试isaacsim
	- 终端运行 conda activate env_isaaclab # 激活env_isaaclab环境
	- 终端运行 cd IsaacLab # 打开IsaacLab文件夹目录
	- 终端运行 isaacsim # env_isaaclab环境下自带的命令，运行即可打开isaacsim
- 安装git
	- 终端运行 sudo apt install git # 下载安装git
	- 终端运行 git --version # 运行出现git版本即安装成功，反之未成功
- 克隆isaaclab
	- 终端运行 git clone git@github.com:isaac-sim/IsaacLab.git # SSH方法，克隆isaaclab远程git库代码
	- 或者终端运行 git clone https://github.com/isaac-sim/IsaacLab.git # HTTPS方法，克隆isaaclab远程git库代码
- 安装isaaclab
	- 终端运行 conda activate env_isaaclab # 激活env_isaaclab环境
	- 终端运行 cd IsaacLab # 打开IsaacLab文件夹目录
	- 终端运行 ./isaaclab.sh --install # 安装isaaclab，PS:容易出现某些插件安装不成功的问题，建议先运行下面的切换国内镜像源指令
		- 终端运行 mkdir -p ~/.pip
		- 终端运行 echo "[global]" > ~/.pip/pip.conf
		- 终端运行 echo "index-url = https://pypi.tuna.tsinghua.edu.cn/simple" >> ~/.pip/pip.conf
- 测试isaaclab
	- 终端运行 conda activate env_isaaclab # 激活env_isaaclab环境
	- 终端运行 cd IsaacLab # 打开IsaacLab文件夹目录
	- 终端运行 ./isaaclab.sh -p scripts/tutorials/00_sim/create_empty.py # 此指令运行不成功则运行下条指令，功能是一样的
	- 或者终端运行 python scripts/tutorials/00_sim/create_empty.py # GUI界面窗口正常加载，即完成isaaclab安装

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
官网教程：https://docs.isaacsim.omniverse.nvidia.com/latest/installation/install_faq.html#isaac-sim-setup-assets-content-pack

安装步骤：

- 下载 `资产包 <https://pan.baidu.com/s/1H0BrGP3T-2Sm5rB-56RkOg?pwd=0000>`_
	- 将三个压缩包文件下载至"/home/<username>/Downloads"
- 安装资产包
	- 终端运行以下指令
	:: 
	
		mkdir ~/isaacsim_assets
		cd ~/Downloads
		unzip "isaac-sim-assets-1@4.5.0-rc.36+release.19112.f59b3005.zip" -d ~/isaacsim_assets
		unzip "isaac-sim-assets-2@4.5.0-rc.36+release.19112.f59b3005.zip" -d ~/isaacsim_assets
		unzip "isaac-sim-assets-3@4.5.0-rc.36+release.19112.f59b3005.zip" -d ~/isaacsim_assets
- 修改配置文件
	- 打开isaacsim安装目录，找到“isaacsim/apps/isaacsim.exp.base.kit”文件，终端运行以下指令
	::

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
	- isaacsim.exp.base.kit文件详细路径如下
	::
		
		路径一：”/home/<username>/isaacsim/apps/isaacsim.exp.base.kit“
		路径二：“/home/<username>/miniconda3/envs/env_isaaclab/lib/python3.10/site-packages/isaacsim/apps/isaacsim.exp.base.kit”
		# 注意“<username>”需要修改为自己的用户名