# Configuration file for the Sphinx documentation builder.
# -- Project information
project = 'DrestryRobot'
copyright = '2025, DrestryRobot'
author = 'DrestryRobot'

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

# -- 主题设置
pygments_style = "monokai"

# -- 文件排序
def sort_by_mtime(app):
    from pathlib import Path
    srcdir = app.srcdir
    rst_files = sorted(
        Path(srcdir).glob('*.rst'),
        key=lambda f: f.stat().st_mtime,
        reverse=True
    )
    
    index_file = Path(srcdir) / 'index.rst'
    toc_content = ".. toctree::\n   :maxdepth: 2\n   :caption: 动态排序目录\n\n" + \
                 "\n".join(f"   {p.stem}" for p in rst_files 
                          if p.stem != 'index' and not p.name.startswith('_'))
    
    # 读取和写入时强制使用 UTF-8 编码
    try:
        original_content = ""
        if index_file.exists():
            with open(index_file, 'r', encoding='utf-8') as f:
                original_content = f.read()
        
        if ".. toctree::" in original_content:
            new_content = original_content.split(".. toctree::")[0] + toc_content
        else:
            new_content = original_content + "\n\n" + toc_content
        
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
    except UnicodeDecodeError as e:
        raise RuntimeError(f"文件编码错误: {e}. 请确保所有 .rst 文件使用 UTF-8 编码") from e

def setup(app):
    app.connect('builder-inited', sort_by_mtime)

# -- 悬浮窗
html_theme_options = {
    # 固定导航栏和目录
    "sticky_navigation": True,  
    # 目录跟随滚动
    "navigation_depth": 4,
    "collapse_navigation": False,
    # 其他优化
    "includehidden": True,      # 显示隐藏页面
    "titles_only": False        # 显示完整目录层级（非仅标题）
}