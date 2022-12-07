import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from soundtrack.discogs.discogs_api import find_ost
import os
from dotenv import load_dotenv, find_dotenv

env_path = find_dotenv()
load_dotenv(env_path)

def spotify_access():

    consumer_key = os.getenv("SPOTIFY_CONSUMER_KEY")
    consumer_secret = os.getenv("SPOTIFY_CONSUMER_SECRET")

    client_credentials_manager = SpotifyClientCredentials(client_id=consumer_key,
                                                      client_secret=consumer_secret)

    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    return sp


def get_playlist(film):

    sp = spotify_access()

    #film_titles, years, genres = find_ost(films)
    playlists = []

    results = sp.search(q='album' + film, market='GB')
    for album_info in results['tracks']['items']:
        if album_info['album']['total_tracks'] > 3:
            if album_info['album']['external_urls']['spotify'] not in playlists:
                playlists.append((album_info['album']['external_urls']['spotify']))

    first_playlist = playlists[0]

    return first_playlist

def full_pl_dict(film_titles, playlists, genres):
    pl_dict = {}
    for title in range(len(film_titles)):
        pl_dict[film_titles[title]] = playlists[title], genres[title]
    return pl_dict
