# your code here ...
import requests
import os
import pandas as pd

class Genius:
    """Class to interact with the Genius API."""

    def __init__(self, access_token):
        """intialize the access token for the Genius API"""
        self.access_token = access_token

    def get_access_token(self):
        """Return the stored Genius API access token"""
        return self.access_token

    def get_artist(self, search_term):
        """Return the artist details for a given search term"""
        # Make a request to the Genius API to search for the artist
        genius_search_url = f"https://api.genius.com/search?q={search_term}&access_token={self.access_token}"
        # Make a GET request to the Genius API search endpoint
        response = requests.get(genius_search_url)
        # Check if the request was successful
        json_data = response.json()
        # Return the JSON data from the response
        json_data
        # Get the first hit from the search results
        first_hit = json_data['response']['hits'][0]['result']
        # Get the artist ID from the first hit
        artist_id = first_hit['primary_artist']['id']
        # Request to the Genius API to get the artist details using artist ID
        artist_name = f"https://api.genius.com/artists/{artist_id}?access_token={self.access_token}"
        # Make a GET request to the Genius API artist endpoint
        name = requests.get(artist_name)
        # Check if the request was successful
        jsonn_data = name.json()
        # Return the JSON data from the response
        return jsonn_data

    def get_artists(self, search_terms):
        """ Return a DataFrame containing artist details for a list of search terms"""
        # Create an empty list to store artist details
        artists =[]
        # Loop through each search term and get the artist details
        for i in search_terms:
            # Get the artist details for the current search term
            artist = self.get_artist(i)
            # Create a dictionary to store the artist details
            artists_details = {
                'search_term': i,
                'artist_name': artist['response']['artist']['name'],
                'artist_id': artist['response']['artist']['id'],
                'followers_count': artist['response']['artist'].get('followers_count')
            }
            # Append the artist details to the list of artists
            artists.append(artists_details)
        # Return a DataFrame containing the artist details
        return pd.DataFrame(artists,columns=['search_term', 'artist_name', 'artist_id', 'followers_count'])
