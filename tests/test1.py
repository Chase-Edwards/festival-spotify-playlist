import unittest
import os
import sys
import json
import logging
from dotenv import load_dotenv

# Get the project path dynamically to avoid hardcoded path
project_path = os.path.abspath(os.path.join('.'))

# Check the path is not already in sys.path, to avoid duplicates
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from src.spotifyagent import agent as sa

# Load environment variables
load_dotenv('.\\secrets.env', override=True)

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='data.log',
                    encoding='utf-8',
                    filemode='w',
                    level=logging.DEBUG)


class TestSpotifyAgent(unittest.TestCase):

    def test_agent_creation(self):
        agent = sa.SpotifyAgent()

    def test_get_artist_id(self):
        # Load the lineup from the JSON file
        
        f = open('.\\data\\lineup.json')
        artists = json.load(f)
        f.close()

        agent = sa.SpotifyAgent()
        
        artist_name = artists[0]
        print(artist_name)
        artist_id = agent.get_artist_id(artist_name)
        print("ARTIST NAME = " + artist_name)
        print("ARTIST ID = " + artist_id)


if __name__ == '__main__':
    unittest.main()