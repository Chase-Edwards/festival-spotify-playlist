import os
import spotipy
import logging


class SpotifyAgent:
    def __init__(self):
        """
        Initialize the SpotifyAgent class.

        Args:
            client_id (str): The client ID for the Spotify API.
            client_secret (str): The client secret for the Spotify API.
        """
        self.client_id = os.getenv("SPOTIPY_CLIENT_ID")
        self.client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
        self.redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")
        self.scope = "playlist-modify-public"
        self.playlist_id = None
        self.oauth_manager = spotipy.SpotifyOAuth(client_id=self.client_id,
                                                  client_secret=self.client_secret,
                                                  redirect_uri=self.redirect_uri,
                                                  scope=self.scope)
        self.client = spotipy.Spotify(auth_manager=self.oauth_manager)
        self.current_user_id = self.client.current_user()['id']


    def get_artist_id(self, artist_name):
        """
        Get the Spotify ID of an artist.

        Args:
            artist_name (str): The artist name.

        Returns:
            str: The Spotify ID of the artist.
        """
        search_query = 'artist:' + artist_name
        artist_id = None

        response = self.client.search(search_query, limit=3, type='artist')
        artists_by_popularity = sorted(response['artists']['items'],
                                       key = lambda x: x['popularity'],
                                       reverse=True)

        for artist in artists_by_popularity:
            if artist['name'].lower() == artist_name.lower():
                artist_id = artist['id']
                break
        
        if artist_id is None:
            logging.warning(f"The agent couldn't find a suitable Artist ID for {artist_name}")
            return None
        else:    
            logging.info(f"Artist ID: {artist_id}")
        
        return artist_id


    def create_playlist(self, name, description):
        """
        Create a public playlist for the current user.

        Args:
            name (str): The new playlist name.
            description (str): The new playlist description.
        """
        playlist = self.client.user_playlist_create(user=self.current_user_id, name=name, description=description)
        self.playlist_id = playlist['id']


    def get_tracks(self, artist_id, amount):
        """
        Gets a given amount of tracks from an artist.

        Args:
            artist_id (str): The ID of the artist whose songs will be searched for.
            amount    (int): The number of songs to add.

        Returns:
            tracks (dict): A dictionary of tracks.
        """
        if amount > 10:
            raise ValueError("amount must be 10 or less.")
        
        return self.client.artist_top_tracks(artist_id)['tracks'][:amount]


    def add_tracks(self, tracks):
        """
        Add an amount of songs to a playlist with the given playlist ID.

        Args:
            playlist_id (str): The ID of the playlist to be deleted.
            tracks (dict): A dictionary of tracks.
        """
        self.client.playlist_add_items(self.playlist_id, [track['id'] for track in tracks])
        

    def delete_playlist(self):
        """
        Delete a playlist with the given playlist ID.
        """
        if self.playlist_id:
            self.client.playlist_unfollow(self.playlist_id)
        
        else:
            print("No playlist id set.")