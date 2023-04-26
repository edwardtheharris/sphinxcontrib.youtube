"""Test module for youtube package."""
from sphinxcontrib.yt import youtube

def test_youtube_class():
    """Validate youtube class."""
    test_youtube = youtube.YouTube()
    assert isinstance(test_youtube, youtube.YouTube)
