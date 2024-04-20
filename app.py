from dotenv import load_dotenv
import os
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth


load_dotenv('.\\secrets.env')

spotipy_client_id = os.getenv("SPOTIPY_CLIENT_ID")
spotipy_client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
spotipy_redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")


print("SPOTIPY_CLIENT_ID: ", spotipy_client_id)
print("SPOTIPY_CLIENT_SECRET: ", spotipy_client_secret)


scope = "playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotipy_client_id,
                                               client_secret=spotipy_client_secret,
                                               redirect_uri=spotipy_redirect_uri,
                                               scope=scope))


# TODO: ADD READ OF LINEUP FILE + COMPREHENSION
artist = "EPROM"

search_query = 'q=' + 'artist%3A' + artist


def get_artist_id(query):
    """
    Get the Spotify ID of an artist based on the search query.

    Args:
        query (str): The search query for the artist.

    Returns:
        str: The Spotify ID of the artist.
    """
    response = sp.search(search_query, limit=1, type='artist')
    artist_uri = response['artists']['items'][0]['id']
    return artist_uri


current_user_id = sp.current_user()['id']

playlist = sp.user_playlist_create(user=current_user_id,
                                   name='Rampage Open Air 2024 - Discord',
                                   description='A playlist for the Rampage Open Air 2024 festival lineup')

created_playlist_id = playlist['id']


def delete_playlist(playlist_id):
    """
    Delete a playlist with the given playlist ID.

    Args:
        playlist_id (str): The ID of the playlist to be deleted.
    """
    sp.current_user_unfollow_playlist(playlist_id)


delete_playlist(created_playlist_id)

print("test")