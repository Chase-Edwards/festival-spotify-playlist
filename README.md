# festival-spotify-playlist
This application generates a spotify playlist from a list of artists. The intended use is for festival lineups.

# Environment Setup

Create a `.env` file and place it in the top level workspace folder. Add the following three ENV variables:

1) SPOTIPY_CLIENT_ID
2) SPOTIPY_CLIENT_SECRET
3) SPOTIPY_REDIRECT_URI

In `main`, when `load_dotenv` is called, it requires a path. Replace `.\\secrets.env` with the name of the .env file you created. 

# Note on playlist creation
The playlist created will be public and non-collaborative to start, as it will be used with the discord bot.