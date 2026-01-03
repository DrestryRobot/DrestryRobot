from docutils import nodes
from docutils.parsers.rst import Directive

class DouyinDirective(Directive):
    # 需要一个参数：视频ID
    required_arguments = 1

    def run(self):
        video_id = self.arguments[0]
        iframe_html = f"""
        <iframe src="https://www.douyin.com/video/{video_id}"
                width="560" height="315"
                frameborder="0"
                allowfullscreen>
        </iframe>
        """
        raw_node = nodes.raw('', iframe_html, format='html')
        return [raw_node]

def setup(app):
    app.add_directive("douyin", DouyinDirective)
