# -*- coding:utf-8 -*-
"""Initialize the Sphinx Contrib yt module.

embedding youtube video to sphinx

usage:

First of all, add `sphinxcontrib.youtube` to sphinx extension list in conf.py

.. code-block:: python

   extensions = ['sphinxcontrib.yt']


then use `youtube` directive.

You can specify video by video url or video id.

.. code-block:: rst

   .. youtube:: http://www.youtube.com/watch?v=Ql9sn3aLLlI

   .. youtube:: Ql9sn3aLLlI


finally, build your sphinx project.

.. code-block:: sh

   $ make html

"""
from pathlib import Path
from . import youtube

repo_root = Path(f'{__file__}').parent.parent.parent
with Path(f'{repo_root}/version').open('r', encoding='utf-8') as v_fh:
    __version__ = v_fh.read()
__author__ = 'xandertheharris@gmail.com'

with Path(f'{repo_root}/license.md').open('r', encoding='utf-8') as v_fh:
    __license__ = v_fh.read()


def setup(app):
    """Set up the Sphinx application."""
    app.add_node(youtube.YouTube,
                 html=(youtube.visit, youtube.depart))
    app.add_directive('youtube', youtube.YoutubeDirective)
    return {
        'parallel_write_safe': True,
        'parallel_read_safe': True,
        'version': __version__
    }
