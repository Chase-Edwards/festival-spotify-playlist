from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import spotify_agent as agent


def main():
    
    
    load_dotenv('.\\secrets.env', override=True)

    # TODO: ADD READ OF LINEUP FILE + COMPREHENSION
    artist_name = "EPROM"
    playlist_name='Rampage Open Air 2024 - Discord'
    playlist_description='A playlist for the Rampage Open Air 2024 festival lineup'
        
    # Create a Spotify agent object
    agent = agent.SpotifyAgent()

    # Get the Spotify ID of the artist
    artist_id = agent.get_artist_id(artist_name)

    tracks = agent.get_tracks(artist_id, 2)

    playlist_id = agent.create_playlist(playlist_name, playlist_description)

    # Add the tracks to the playlist
    agent.add_tracks(tracks)

    pass

if __name__ == "__main__":
    main()