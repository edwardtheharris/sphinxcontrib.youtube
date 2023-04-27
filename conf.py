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
    "myst_parser",
    "myst_nb",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.githubpages"
]
#: -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
#: [html options](https://tinyurl.com/35zdr2a7)
html_static_path = ['_static']
nb_render_markdown_format = "myst"
project = 'Sphinx Contrib YouTube'
root_doc = 'readme'
source_suffix = {
    '.md': 'markdown',
}
templates_path = ['_templates']
