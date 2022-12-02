import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from Soundtrack-frontend.

client_credentials_manager = SpotifyClientCredentials(client_id=cid,
                                                      client_secret=secret)

sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def get_playlists(film_name):
    film = "pulp fiction"
    playlists = []
    keywords = ['OST', 'soundtrack', 'motion', 'score']

    for keyword in keywords:
        results = sp.search(q='album' + film + ' ' + keyword, market='GB')
        for i in results['tracks']['items']:
            if i['album']['total_tracks'] > 3:
                if i['album']['external_urls']['spotify'] not in playlists:
                    playlists.append((i['album']['external_urls']['spotify']))

    return playlists
