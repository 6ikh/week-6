# your code here ...
import requests
import os
import pandas as pd

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
        first_hit = json_data['response']['hits'][0]['result']
        artist_id = first_hit['primary_artist']['id']
        artist_name = f"https://api.genius.com/artists/{artist_id}?access_token={self.access_token}"
        name = requests.get(artist_name)
        jsonn_data = name.json()
        return jsonn_data


    def get_artists(self, search_terms):
        artists =[]
        for i in search_terms:
            artist = self.get_artist(i)
            artists_details = {
                'search_term': i,
                'artist_name': artist['response']['artist']['name'],
                'artist_id': artist['response']['artist']['id'],
                'followers_count': artist['response']['artist'].get('followers_count')
            }
            artists.append(artists_details)
        return pd.DataFrame(artists,columns=['search_term', 'artist_name', 'artist_id', 'followers_count'])
