#-*- coding:utf-8 -*-
"""YouTube module for Sphinx Contrib YouTube extension."""
#Import urlparse in Python 2 or urllib.parse in Python 3

try:
    import urlparse

except ImportError:
    import urllib.parse as urlparse

from docutils import nodes
from docutils.parsers import rst


class YouTube(nodes.General, nodes.Element):
    """Instantiates YouTube objects."""

    video_id = None


def is_url(url_str):
    """Check that a string is a url."""
    if url_str.startswith('http://') or url_str.startswith('https://'):
        return True

    return False


def get_video_id(url):
    """Get the url of a video."""
    return urlparse.parse_qs(urlparse.urlparse(url).query)['v'][0]


def visit(self, node):
    """Visit a document's node.

    :param node: The node being visited
    """
    video_id = node.video_id
    url = f'https://www.youtube.com/embed/{video_id}'
    tag = ('<iframe width="640" height="360" style="margin-bottom: 25px"'
           f' src="{url}" frameborder="0" allowfullscreen="1">&nbsp;</iframe>')
    self.body.append(tag)


def depart(self, node):
    """Depart a node."""
    print(self)
    print(node)


class YoutubeDirective(rst.Directive):
    """Instantiate Youtube directives."""

    #: name of the directive
    name = 'youtube'
    #: class of the node
    node_class = YouTube
    #: node has no content
    has_content = False
    #: single required argument
    required_arguments = 1
    #: no optional arguments
    optional_arguments = 0
    #: no whitespace in last argument
    final_argument_whitespace = False
    #: option spec is empty
    option_spec = {}

    def run(self):
        """Execute the youtube directive."""
        node = self.node_class()

        arg = self.arguments[0]

        if is_url(arg):
            node.video_id = get_video_id(arg)
        else:
            node.video_id = arg

        return [node]
