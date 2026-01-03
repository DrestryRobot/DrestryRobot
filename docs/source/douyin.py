import requests
from urllib.parse import urlparse
from docutils import nodes
from docutils.parsers.rst import Directive

def get_real_url(share_url):
    """获取抖音分享链接的重定向地址"""
    session = requests.Session()
    resp = session.get(share_url, allow_redirects=False)
    return resp.headers['Location'] if resp.status_code == 302 else share_url

def extract_video_id(real_url):
    """从重定向地址提取视频ID"""
    path = urlparse(real_url).path
    return path.split('/')[-1] if path else None

def get_no_watermark_url(video_id):
    """构建无水印视频地址"""
    return f'https://aweme.snssdk.com/aweme/v1/play/?video_id={video_id}&ratio=720p&line=0'

class DouyinDirective(Directive):
    required_arguments = 1  # 一个参数：短链或视频URL

    def run(self):
        share_url = self.arguments[0]
        real_url = get_real_url(share_url)
        video_id = extract_video_id(real_url)
        if not video_id:
            error = nodes.error('', nodes.Text("无法解析视频ID"))
            return [error]

        no_wm_url = get_no_watermark_url(video_id)
        iframe_html = f"""
        <video width="560" height="315" controls>
          <source src="{no_wm_url}" type="video/mp4">
          您的浏览器不支持 video 标签。
        </video>
        """
        raw_node = nodes.raw('', iframe_html, format='html')
        return [raw_node]

def setup(app):
    app.add_directive("douyin", DouyinDirective)
