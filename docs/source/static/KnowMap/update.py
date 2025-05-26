import os
import json

# 获取当前脚本所在目录
base_dir = os.path.dirname(os.path.abspath(__file__))

# 计算相对路径
source_dir = os.path.join(base_dir, "..", "..", "技术总结")
json_path = os.path.join(base_dir, "sites.json")

# 关键词分类映射
categories = {
    "算法": [
        "计算", "算法", "矩阵", "优化", "神经网络", "机器学习", "深度学习", "回归",
        "分类", "聚类", "特征提取", "数据结构", "图像处理", "路径规划", "强化学习",
        "离散数学", "概率", "统计", "人工智能", "数值分析", "图算法", "搜索算法",
        "模式识别", "傅里叶变换", "边缘检测", "图像分割", "智能优化", "计算机视觉",
        "信号处理", "特征工程", "贝叶斯理论", "梯度下降", "神经网络训练"
    ],
    "控制": [
        "PID", "传感器", "通信", "反馈", "驱动", "控制", "自动控制", "模糊控制",
        "力控", "增益调节", "闭环控制", "开环控制", "自适应控制", "机器人控制",
        "动力学", "伺服系统", "电机控制", "CAN总线", "TCP/IP", "串口", "调制解调",
        "远程控制", "数据采集", "工业控制", "分布式控制", "状态反馈", "系统辨识",
        "鲁棒控制", "非线性控制", "自适应滤波", "数字控制", "实时控制", "系统建模",
        "动态响应", "液压控制", "气动控制", "智能控制", "压力调节", "电磁控制"
    ],
    "机械": [
        "SolidWorks", "装配", "机构", "轴", "负载", "力学", "刚度", "材料",
        "运动学", "气动系统", "液压系统", "工程制图", "机械设计", "应力分析",
        "有限元分析", "传动系统", "电动推杆", "线性导轨", "滚珠丝杠", "齿轮",
        "机床", "制造工艺", "机器人结构", "执行器", "机械臂", "夹具",
        "摩擦学", "机械连接", "焊接工艺", "机加工", "弹簧", "轴承", "传动",
        "机电一体化", "机械动力学", "机构设计", "扭矩计算", "刚度分析", "摩擦损耗",
        "热力学", "流体力学", "材料力学", "动力学仿真", "3D建模", "逆向工程",
        "机械"
    ]
}

def classify_document(content):
    """ 根据文档内容分类 """
    for category, keywords in categories.items():
        if any(keyword in content for keyword in keywords):
            return category
    return "其它"

# 确保路径存在
if not os.path.exists(source_dir):
    raise FileNotFoundError(f"路径不存在: {source_dir}")

# 读取 .rst 文件
data = []
for filename in os.listdir(source_dir):
    if filename.endswith(".rst"):
        name = filename.replace(".rst", "")
        link = f"https://drestryrobot.readthedocs.io/技术总结/{name}.html"

        # 读取文档内容并分类
        with open(os.path.join(source_dir, filename), "r", encoding="utf-8") as f:
            content = f.read()
        category = classify_document(content)

        data.append({"name": name, "category": category})

# 写入 JSON
with open(json_path, "w", encoding="utf-8") as f:
    f.write("[\n")
    for i, item in enumerate(data):
        json_line = f'    {json.dumps(item, ensure_ascii=False)}'
        if i < len(data) - 1:
            json_line += ",\n"  # 添加逗号但避免最后一个多余的换行
        else:
            json_line += "\n"
        f.write(json_line)
    f.write("]\n")


print(f"JSON 文件已更新: {json_path}")
