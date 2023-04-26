"""Test module for youtube package."""
from sphinxcontrib.yt import youtube

def test_youtube_class():
    """Validate youtube class."""
    test_youtube = youtube.youtube()
    assert isinstance(test_youtube, type(youtube.youtube()))
