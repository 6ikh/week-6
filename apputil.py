# your code here ...
import requests
import os

class Genius:
    def __init__(self, access_token):
        self.access_token = access_token
    def get_access_token(self):
        return self.access_token


    def get_artist(self, search_term):
        genius_search_url = f"https://api.genius.com/search?q={search_term}&access_token={self.access_token}"
        response = requests.get(genius_search_url)
        json_data = response.json()
        json_data

#if __name__ == "__main__":
    #load_dotenv()
    # constants
    #ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
    #genius = Genius(access_token=ACCESS_TOKEN)
