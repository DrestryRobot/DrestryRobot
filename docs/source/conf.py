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
    'sphinx_copybutton',
    'sphinx_reredirects',
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

# 主题设置
pygments_style = "monokai"


# 文件排序
def sort_by_mtime(app):
    from pathlib import Path
    app.config.master_doc = 'index'
    rst_files = sorted(
        Path('.').glob('*.rst'),
        key=lambda f: f.stat().st_mtime,
        reverse=True
    )
    with open('index.rst', 'w') as f:
        f.write(".. toctree::\n   :maxdepth: 2\n   :caption: 动态排序目录\n\n" +
               "\n".join(f"   {p.stem}" for p in rst_files if p.stem != 'index'))

def setup(app):
    app.connect('builder-inited', sort_by_mtime)