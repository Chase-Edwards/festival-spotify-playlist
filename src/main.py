from dotenv import load_dotenv
from spotifyagent import agent as sa
import json
import logging
import sys
import os


def main():
    
    # Load environment variables
    load_dotenv('.\\secrets.env', override=True)

    # Set up logging
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='data.log',
                        encoding='utf-8',
                        filemode='w',
                        level=logging.DEBUG)

    
    # Define the playlist name and description
    playlist_name='Rampage Open Air 2024 - Discord'
    playlist_description='A playlist for the Rampage Open Air 2024 festival lineup'
        
    # Create a Spotify agent object
    agent = sa.SpotifyAgent()

    # Load the lineup from the JSON file
    f = open('.\\data\\lineup.json')
    artists = json.load(f)
    f.close()

    # Create the playlist
    if agent.playlist_id is None:
        agent.create_playlist(playlist_name, playlist_description)

    # Loop through the artists and add their tracks to the playlist
    for artist in artists:
        # Get the Spotify ID of the artist
        artist_id = agent.get_artist_id(artist)

        # Skip the artist if the ID is not found
        if artist_id is None:
            continue
        else:
            # Get the top tracks of the artist
            tracks = agent.get_tracks(artist_id, 5)
            if len(tracks) == 0:
                continue
            else:        
                # Add the tracks to the playlist
                agent.add_tracks(tracks)


if __name__ == "__main__":
    main()