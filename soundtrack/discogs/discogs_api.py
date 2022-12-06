import requests
import os
from dotenv import load_dotenv, find_dotenv

env_path = find_dotenv()
load_dotenv(env_path)

def find_ost(films):
    """
    Summary: Runs a query on the Discogs API for the film name to return full title,
    year and genre of the same film
    Input: name of the film -> list of lists
    Return: Title, Year, Genre -> tuple
    """

    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")

    full_titles = []
    year_releases =[]
    genres = []
    for film in films:
        film_title = film[0]
        url = f'https://api.discogs.com/database/search?q={film_title}/'
        params = {'key':consumer_key,
                'secret':consumer_secret,
                'type':'release',
                'style':'soundtrack',
                'format':'CD'
                }
        response = requests.get(url,params=params)

        if response.status_code != 200:
            print(response.status_code)
            return 'Error'

        data = response.json()['results'][0]

        full_title = data['title']
        full_titles.append(full_title)
        year = data['year']
        year_releases.append(year)
        try:
            genre = data['genres']
            genres.append(genre)
        except KeyError:
            genre = data['genre']
            genres.append(genre)
        except:
            genres.append('OST')

    return full_titles, year_releases, genres


if __name__ == "__main__":
    films = [['The thing', 1982, 'Horror, Mystery, Science Fiction, Thriller'],
    ["Ain't them bodies saints", 2013, 'Crime, Drama, Romance, Western'],
    ['The bridge on the river kwai', 1957, 'Drama, History, War'],
    ["Jacob's ladder",1990,'Drama, Military, War, Vietnam War, Mystery, Horror'],
    ['Ambulance', 2022, 'Action, Crime, Thriller']]

    tuple_films  = find_ost(films)

    print(tuple_films)
