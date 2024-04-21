import unittest
import os
import sys
import json
from dotenv import load_dotenv

# get the project path dynamically to avoid hardcoded path
project_path = os.path.abspath(os.path.join('.'))

# check the path is not already in sys.path, to avoid duplicates
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from src.spotifyagent import agent as a

# Load environment variables
load_dotenv('.\\secrets.env', override=True)

class TestSpotifyAgent(unittest.TestCase):

    def test_agent_creation(self):
        agent = a.SpotifyAgent()

    def test_get_artist_id(self):
        # Load the lineup from the JSON file
        
        f = open('.\\data\\lineup.json')
        artists = json.load(f)

        agent = a.SpotifyAgent()
        
        artist_name = artists[0]
        print(artist_name)
        artist_id = agent.get_artist_id(artist_name)
        print("ARTIST NAME = " + artist_name)
        print("ARTIST ID = " + artist_id)
        # assert artist_id is not None


if __name__ == '__main__':
    unittest.main()