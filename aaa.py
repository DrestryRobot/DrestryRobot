import requests
import os
import subprocess

# GitHub 仓库路径
GITHUB_REPO = "https://github.com/drestryrobot/icon-storage.git"
LOCAL_REPO_PATH = "icon-storage"

# 创建存储图标的目录
os.makedirs(f"{LOCAL_REPO_PATH}/icons", exist_ok=True)

# 设置请求头，模拟浏览器访问
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 获取网站图标
def fetch_icon(domain):
    urls = [
        f"https://{domain}/manifest.json",
        f"https://{domain}/apple-touch-icon.png",
        f"https://{domain}/favicon.ico",
        f"https://api.iowen.cn/favicon/{domain}.png"  # 兜底方案
    ]
    
    for url in urls:
        try:
            response = requests.get(url, headers=HEADERS, timeout=5)
            if response.status_code == 200:
                return url
        except requests.exceptions.RequestException:
            continue
    
    return None  # 如果所有图标都无法获取，则返回 None

# 保存图标到本地
def save_icon(domain):
    icon_url = fetch_icon(domain)
    if icon_url:
        response = requests.get(icon_url, headers=HEADERS, stream=True)
        if response.status_code == 200:
            with open(f"{LOCAL_REPO_PATH}/icons/{domain}.png", "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"✅ {domain} 图标已保存")
        else:
            print(f"❌ 无法获取 {domain} 图标")
    else:
        print(f"⚠️ {domain} 没有可用图标")

# 示例：抓取多个网站的图标
domains = ["example.com", "baidu.com", "taobao.com", "github.com", "google.com"]
for domain in domains:
    save_icon(domain)

# Git 操作：提交并推送到 GitHub
def git_push():
    try:
        subprocess.run(["git", "add", "."], cwd=LOCAL_REPO_PATH, check=True)
        subprocess.run(["git", "commit", "-m", "更新图标"], cwd=LOCAL_REPO_PATH, check=True)
        subprocess.run(["git", "push"], cwd=LOCAL_REPO_PATH, check=True)
        print("✅ 图标已推送到 GitHub")
    except Exception as e:
        print(f"❌ Git 操作失败: {e}")

git_push()
