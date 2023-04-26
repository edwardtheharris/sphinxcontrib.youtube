#-*- coding:utf-8 -*-
"""Sphinx Contrib YouTube package.

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
<<<<<<< Updated upstream

'''
=======
"""
from pathlib import Path
from . import youtube
>>>>>>> Stashed changes

__version__ = '0.2.3'
__author__ = 'xandertheharris@gmail.com'
__license__ = 'Unlicense'



def setup(app):

    from . import youtube

    app.add_node(youtube.youtube,
                 html=(youtube.visit, youtube.depart))
    app.add_directive('youtube', youtube.YoutubeDirective)
    return {'parallel_read_safe': True}
