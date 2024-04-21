from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import spotifyagent as sa
import json


def main():
    # Load environment variables
    load_dotenv('.\\secrets.env', override=True)
    
    # Define the playlist name and description
    playlist_name='Rampage Open Air 2024 - Discord'
    playlist_description='A playlist for the Rampage Open Air 2024 festival lineup'
        
    # Create a Spotify agent object
    agent = sa.SpotifyAgent()

    # Load the lineup from the JSON file
    artists = json.loads('.\\data\\lineup.json')

    # Loop through the artists and add their tracks to the playlist
    for artist in artists:
        # Get the Spotify ID of the artist
        artist_id = sa.get_artist_id(artist)

        # Skip the artist if the ID is not found
        if artist_id is None:
            continue
        else:
            # Get the top n tracks of the artist
            tracks = sa.get_tracks(artist_id, 2)

            playlist_id = sa.create_playlist(playlist_name, playlist_description)

            # Add the tracks to the playlist
            sa.add_tracks(tracks)


if __name__ == "__main__":
    main()