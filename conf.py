#!/usr/bin/env python3
# pylint: disable=invalid-name,redefined-builtin
"""Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the
[documentation](https://www.sphinx-doc.org/en/master/usage/configuration.html).

```{rubric} Project information
```

[Project information](https://tinyurl.com/255t89n7)
"""
from pathlib import Path
import sys

sys.path.append('.src/')
sys.path.append('.')
print(sys.path)

author = 'Xander Harris'
copyright = '2023, The Internet'
exclude_patterns = [
    '_build',
    '.DS_Store',
    '.pytest_cache',
    '.venv/*',
    'Thumbs.db',
]
#: -- General configuration ---------------------------------------------------

with Path('version').open('r', encoding='utf-8') as v_fh:
    release = v_fh.read()

#: [general configuration](https://tinyurl.com/4vys37ez)
extensions = [
    "myst_nb",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.duration",
    "sphinx.ext.githubpages",
    "sphinx.ext.graphviz"
]
#: -- Options for HTML output -------------------------------------------------
html_theme = 'pydata_sphinx_theme'
#: [html options](https://tinyurl.com/35zdr2a7)
html_static_path = ['_static']
project = 'Sphinx Contrib YouTube'
root_doc = 'index'
source_suffix = {
    '.md': 'myst-nb',
    '.ipynb': 'myst-nb',
    '.myst': 'myst-nb',
}
templates_path = ['_templates']
