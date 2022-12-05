import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id=cid,
                                                      client_secret=secret)

sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def get_playlists(ost_name):
    
    playlists = []
    keywords = ['OST', 'soundtrack', 'motion', 'score']

    for keyword in keywords:
        results = sp.search(q='album' + ost_name + ' ' + keyword, market='GB')
        for i in results['tracks']['items']:
            if i['album']['total_tracks'] > 3:
                if i['album']['external_urls']['spotify'] not in playlists:
                    playlists.append((i['album']['external_urls']['spotify']))

    return playlists
