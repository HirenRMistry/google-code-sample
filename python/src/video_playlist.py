"""A video playlist class."""
from .video import Video


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self, name):
        self._videos = {}
        self._original_name = name
    
    def add_video(self, video):
        self._videos[video.video_id] = video

    def get_video(self, video_id):
        """Returns the video object (title, url, tags) from the video library.

        Args:
            video_id: The video url.

        Returns:
            The Video object for the requested video_id. None if the video
            does not exist.
        """
        return self._videos.get(video_id, None) 
    
    def get_orginal_name(self):
        return  self._original_name
    
    def get_all_videos(self):
        return self._videos.values()
    
    def delete_video(self, video_id):
        return self._videos.pop(video_id, None)
    
    def delete_all_vids(self):
        self._videos.clear()
