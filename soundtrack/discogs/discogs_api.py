import requests
import os
from dotenv import load_dotenv, find_dotenv

env_path = find_dotenv()
load_dotenv(".env")

def find_ost(films):
    """
    Summary: Runs a query on the Discogs API for the film name to return full title,
    year and genre of the same film
    Input: name of the film -> list of film titles
    Return: {Title: Genre} -> dict
    """

    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    ost_with_genres = {}
    for film in films:
        url = f'https://api.discogs.com/database/search?q={film}/'
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


        if len(response.json()['results']) == 0:
            ost_with_genres[film] = "OST"
            return ost_with_genres
        data = response.json()['results'][0]
        try:
            genre = data['genres']
        except KeyError:
            genre = data['genre']
        except:
            genre = 'OST'

        ost_with_genres[data['title']] = ', '.join(genre)
    return ost_with_genres


if __name__ == "__main__":
    films = [['The thing', 1982, 'Horror, Mystery, Science Fiction, Thriller'],
    ["Ain't them bodies saints", 2013, 'Crime, Drama, Romance, Western'],
    ['The bridge on the river kwai', 1957, 'Drama, History, War'],
    ["Jacob's ladder",1990,'Drama, Military, War, Vietnam War, Mystery, Horror'],
    ['Ambulance', 2022, 'Action, Crime, Thriller']]

    tuple_films  = find_ost(films)

    print(tuple_films)
