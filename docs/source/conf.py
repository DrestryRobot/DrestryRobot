# Configuration file for the Sphinx documentation builder.
# -- Project information

project = 'DrestryRobot'
copyright = '2025, DrestryRobot'
author = 'DrestryRobot'

# release = '2025.05.04'
# version = '2025.05.04'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.mathjax',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

html_static_path = ['_static']

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- 添加 Google Analytics 跟踪代码
html_js_files = [
    'https://www.googletagmanager.com/gtag/js?id=G-X0VQVVBVYP',
    'analytics.js',
]

# -- 自定义CSS样式
html_css_files = ['custom.css']

# -- 自定义网页包含指令
from docutils import nodes
from docutils.parsers.rst import Directive

class IncludeHTML(Directive):
    """
    自定义指令，用于插入外部的 HTML 文件内容。
    使用方法：
    .. includehtml:: path/to/weather.html
    """
    required_arguments = 1
    final_argument_whitespace = True

    def run(self):
        env = self.state.document.settings.env
        rel_path, abs_path = env.relfn2path(self.arguments[0])
        try:
            with open(abs_path, "r", encoding="utf-8") as f:
                html_content = f.read()
        except Exception as err:
            error = self.state_machine.reporter.error(
                f"无法包含文件 {abs_path}: {err}",
                nodes.literal_block(self.block_text, self.block_text),
                line=self.lineno)
            return [error]
        return [nodes.raw("", html_content, format="html")]

def setup(app):
    app.add_directive("includehtml", IncludeHTML)
