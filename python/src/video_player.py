"""A video player class."""

from .video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.current_video = None
        self.pause = False

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        vids = sorted(self._video_library.get_all_videos(), key=lambda x: x.title)
        print("Here's a list of all available videos:")
        for v in vids:
            if str(v.tags):
                all_tags = str(v.tags).replace("'", "").replace(",", "").replace("(", "").replace(")", "")

            print(f" {v.title} ({v.video_id}) [{all_tags}]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        #if video exists
        video = self._video_library.get_video(video_id)
        if video:
                
            #If there is a video currently playing, stop video
            if self.current_video:
                print("Stopping video:", self.current_video.title)

            #print playing video and update current video
            print("Playing video:", video.title)
            self.current_video = video
            self.pause = False
        
        else:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""

        #If there is a video currently playing, stop video
        if self.current_video:
            print("Stopping video:", self.current_video.title)
            self.current_video = None
        
        #print no video message video 
        else:
            print("Cannot stop video: No video is currently playing")



    def play_random_video(self):
        """Plays a random video from the video library."""
        #No videos?
        num_videos = len(self._video_library.get_all_videos())

        if not num_videos:
            print("No videos available")
        
        else:
            random_number = random.randint(0, num_videos-1)
            vid_id = self._video_library.get_all_videos()[random_number].video_id
            self.play_video(vid_id)
            self.pause = False

    def pause_video(self):
        """Pauses the current video."""
        if not self.current_video:
            print("Cannot pause video: No video is currently playing")
            return
        elif self.pause:
            print(f"Video already paused: {self.current_video.title}")
            return
        else:
            print(f"Pausing video: {self.current_video.title}")
            self.pause = True
    
    def continue_video(self):
        """Resumes playing the current video."""
        if not self.current_video:
            print("Cannot continue video: No video is currently playing")
            return
        if not self.pause:
            print("Cannot continue video: Video is not paused")
        else:
            print(f"Continuing video: {self.current_video.title}")
            self.pause = False


    def show_playing(self):
        """Displays video currently playing."""

        if self.current_video:
            v = self.current_video
            if str(v.tags):
                all_tags = str(v.tags).replace("'", "").replace(",", "").replace("(", "").replace(")", "")
            p = ""
            if self.pause:
                p = "- PAUSED"
            print(f"Currently playing: {v.title} ({v.video_id}) [{all_tags}] {p}")
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
