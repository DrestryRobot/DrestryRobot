# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'DrestryRobot'
copyright = '2025, DrestryRobot'
author = 'DrestryRobot'

release = '2025.05.01'
version = '2025.05.01'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    # 'sphinx_comments',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
html_static_path = ['_static']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# 添加 Google Analytics 跟踪代码
html_js_files = [
    'https://www.googletagmanager.com/gtag/js?id=G-X0VQVVBVYP',
    'analytics.js',
]

# # 配置评论服务，例如 Disqus 或 Giscus
# comments_config = {
#     "hypothesis": False,  # 如果你要使用 Hypothesis 注释功能，可以改为 True
#     "utterances": {
#         "repo": "https://github.com/DrestryRobot/DrestryRobot",  # 如果使用 Giscus，请替换为你的仓库名称
#         "theme": "github-light",  # 主题（可选：github-dark）
#     },
#     "disqus": {
#         "shortname": "http://disqus.com/by/disqus_pInaIyoktw"  # 如果使用 Disqus，请填写你的短名称
#     },
# }



