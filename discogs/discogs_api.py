import discogs_client
import requests
from soundtrack-frontend.indices import find_info_in_data

film, image_names = find_info_in_data(indices)


"""Runs a query on the Discogs API for the film name to return full title,
year and genre of the same film"""

def find_ost(film):
    full_titles = []
    year_releases =[]
    genres = []
    for i in range(len(indices)):
        film_title = film[i][0]
        year_release = film[i][1]
        url = f'https://api.discogs.com/database/search?q={film_title/'

        params = {'key':consumer_key,
                'secret':consumer_secret,
                'type':'release',
                'style':'soundtrack',
                'format':'CD',
                'year': year_release
                }
        response = requests.get(url,params=params)

        if response.status_code != 200:
            return ''

        data = response.json()

        full_title = data['results'][0]['title']
        full_titles.append(full_title)
        year = data['results'][0]['year']
        year_releases.append(year)
        genre = data['results'][0]['genre']
        genres.append(genre)
        
    return full_titles, year_releases, genres
