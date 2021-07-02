"""A video player class."""

from typing import ValuesView
from .video_playlist import Playlist
from .video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.current_video = None
        self.pause = False
        self.playlists = {}

    def check_video_exists(self, video_id):
        """Checks if a given video_id exists in the Video Library
    
        Args:
            video_id: The video_id to be played.
        """
        return self._video_library.get_video(video_id)
    
    def check_pl_exists(self, playlist_name):
        """Checks if a given playlist_name exists
        
        Args:
            playlist_name: The playlist name.
        """
        return playlist_name.lower() in [p.lower() for p in self.playlists.keys()]
    
    def video_details(self, v):
        """Return str version of a video for output
        
        Args:
            video: Video object to be output
        """
        if str(v.tags):
            all_tags = str(v.tags).replace("'", "").replace(",", "").replace("(", "").replace(")", "")
        return f" {v.title} ({v.video_id}) [{all_tags}]"

    def print_videos(self, videos):
        """Prints video titles line by line from a list of videos

        Args:
            videos: List of videos to be displayed.
        """

        for v in videos:
            print(self.video_details(v))

    def number_of_videos(self):
        """Returns the number of videos"""
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        vids = sorted(self._video_library.get_all_videos(), key=lambda x: x.title)
        print("Here's a list of all available videos:")
        self.print_videos(vids)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        #if video exists
        video = self.check_video_exists(video_id)
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

        if self.check_pl_exists(playlist_name):
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            #store playlist in their lowercase format
            self.playlists[playlist_name.lower()] = Playlist(playlist_name)
            print(f"Successfully created new playlist: {playlist_name} ")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        #if playlist doesn't exist, show warning
        if not self.check_pl_exists(playlist_name):
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
            return
        
        #if video doesn't exist, show warning
        if not self.check_video_exists(video_id):
            print(f"Cannot add video to {playlist_name}: Video does not exist")
            return
        
        #if video already in playlist don't add
        if self.playlists[playlist_name.lower()].get_video(video_id):
            print(f"Cannot add video to {playlist_name}: Video already added")
            return
        
        #add video to playlist
        selected_video = self._video_library.get_video(video_id)
        self.playlists[playlist_name.lower()].add_video(selected_video)
        print(f"Added video to {playlist_name}: {selected_video.title}")
        
    def show_all_playlists(self):
        """Display all playlists."""

        #if no playlists, show warning
        if not len(self.playlists):
            print("No playlists exist yet")
        
        #Otherwise, show all playlists
        else:
            print("Showing all playlists:")
            sorted_playlists = sorted(self.playlists.items())
            for (_, value) in sorted_playlists:
                print(value.get_orginal_name())

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        #Check if playlist exists, if doesn't shwo warning
        if not self.check_pl_exists(playlist_name):
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
            return
        
        #Playlist must exist
        else:
            #Get chosen playlist
            playlist = self.playlists[playlist_name.lower()]
            print(f"Showing playlist: {playlist_name}")

            videos = playlist.get_all_videos()
            #If there are no videos, show message
            if not len(videos):
                print(" No videos here yet")
            
            #otherwise, show all videos
            else:
                self.print_videos(videos)

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        #if playlist doesn't exist, show warning
        if not self.check_pl_exists(playlist_name):
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
            return
        
        #if video doesn't exist, show warning
        if not self.check_video_exists(video_id):
            print(f"Cannot remove video from {playlist_name}: Video does not exist")
            return
        
        #check if video in playlist, if not show warning
        playlist = self.playlists[playlist_name.lower()]
        if not playlist.get_video(video_id):
            print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
            return
        
        #Finally delete video from playlist
        deleted = playlist.delete_video(video_id)
        if deleted:
            print(f"Removed video from {playlist_name}: {deleted.title}")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        #if playlist doesn't exist, show warning
        if not self.check_pl_exists(playlist_name):
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
            return
        
        #Otherwise, find playlist and clear
        else:
            #Get Playlist
            playlist = self.playlists[playlist_name.lower()]
            playlist.delete_all_vids()
            print(f"Successfully removed all videos from {playlist_name}")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        #if playlist doesn't exist, show warning
        if not self.check_pl_exists(playlist_name):
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
            return
        
        #Otherwise, the playlist exists, delete it
        else:
            if self.playlists.pop(playlist_name.lower(), None):
                print(f"Deleted playlist: {playlist_name}")
   
    def search_videos(self, original_search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        search_term = original_search_term.lower()
        videos = self._video_library.get_all_videos()

        i = 0
        choice_of_vids = []
        #Go through all videos, searching for term, print choices
        for vid in videos:
            #If search term in title of video
            if search_term in vid.title.lower():
                i += 1
                if i == 1:
                    print(f"Here are the results for {original_search_term}:")
                
                #Keep a list of videos to choose from
                choice_of_vids.append(vid)
                v = self.video_details(vid)
                print(f"{i}){v}")
       
        #No matches, show warning
        if not i:
            print(f"No search results for {original_search_term}")
            return
        
        #Get input on what they would like to play
        try:
            print("Would you like to play any of the above? If yes, specify the number of the video. ")
            print("If your answer is not a valid number, we will assume it's a no.")
            choice = int(input(""))
        except ValueError:
            return
        #If choice is within parameters, play choice 
        if choice >0 and choice <= i:
            video = choice_of_vids[choice-1]
            self.play_video(video.video_id)

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        search_term = video_tag.lower()
        videos = self._video_library.get_all_videos()

        i = 0
        choice_of_vids = []
        #Go through all videos, searching for term in tag, print choices
        for vid in videos:
            #If search term in tags of video
            tags = [t.lower() for t in vid.tags]
            if search_term in tags:
                i += 1
                if i == 1:
                    print(f"Here are the results for {video_tag}:")
                
                #Keep a list of videos to choose from
                choice_of_vids.append(vid)
                v = self.video_details(vid)
                print(f"{i}){v}")
        
        #No matches, show warning
        if not i :
            print(f"No search results for {video_tag}")
            return
        
        #Get input on what they would like to play
        try:
            print("Would you like to play any of the above? If yes, specify the number of the video. ")
            print("If your answer is not a valid number, we will assume it's a no.")
            choice = int(input(""))
        except ValueError:
            return
        
        #If choice is within parameters, play choice 
        if choice >0 and choice <= i:
            video = choice_of_vids[choice-1]
            self.play_video(video.video_id)
    
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
