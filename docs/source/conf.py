# Configuration file for the Sphinx documentation builder.
# -- Project information
project = 'DrestryRobot'
copyright = '2026, DrestryRobot'
author = 'DrestryRobot'

# -- General configuration
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / '_ext'))

extensions = [
    'video_links',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.mathjax',
    'sphinx_copybutton',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- 主题设置
pygments_style = "monokai"