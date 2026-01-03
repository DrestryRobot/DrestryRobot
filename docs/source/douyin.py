import requests
from bs4 import BeautifulSoup
from docutils import nodes
from docutils.parsers.rst import Directive

class DouyinDirective(Directive):
    required_arguments = 1  # 一个参数：抖音短链

    def run(self):
        share_url = self.arguments[0]

        try:
            # 调用 ShowBL 解析服务
            resp = requests.post(
                "https://www.showbl.com/lab/douyin",
                data={"url": share_url},
                headers={"User-Agent": "Mozilla/5.0"}
            )
            soup = BeautifulSoup(resp.text, "html.parser")

            # 找到视频直链（ShowBL 页面里通常有下载按钮）
            video_link = soup.find("a", string="下载视频")
            if video_link:
                mp4_url = video_link["href"]
                html = f"""
                <video width="560" height="315" controls>
                  <source src="{mp4_url}" type="video/mp4">
                  您的浏览器不支持 video 标签。
                </video>
                """
                return [nodes.raw('', html, format='html')]
            else:
                return [nodes.paragraph(text="未能解析到视频直链")]
        except Exception as e:
            return [nodes.paragraph(text=f"解析失败: {e}")]

def setup(app):
    app.add_directive("douyin", DouyinDirective)
