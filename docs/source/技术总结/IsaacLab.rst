Isaac Lab
==========
.. contents:: 目录

What Is Isaac Lab?
------------------
Isaac Lab is a unified and modular framework for robot learning that aims to simplify common workflows in robotics research (such as reinforcement learning, learning from demonstrations, and motion planning). It is built on NVIDIA Isaac Sim to leverage the latest simulation capabilities for photo-realistic scenes, and fast and efficient simulation.

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