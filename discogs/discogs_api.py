import discogs_client
import pandas as pd
import requests


"""Runs a query on the Discogs API for the film name to return full title,
year and genre of the same film"""

def find_ost(film):

    url = f'https://api.discogs.com/database/search?q={film/'

    params = {'key':consumer_key,
             'secret':consumer_secret,
             'type':'release',
             'style':'soundtrack',
             'format':'CD'
             }
    response = requests.get(url,params=params)

    if response.status_code != 200:
        return ''

    data = response.json()

    full_title = data['results'][0]['title']

    year = data['results'][0]['year']

    genre = data['results'][0]['genre']

    return full_title, year, genre
