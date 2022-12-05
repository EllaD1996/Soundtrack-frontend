import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from soundtrack-frontend.discogs import find_ost
from soundtrack-frontend.indices import find_info_in_data

client_credentials_manager = SpotifyClientCredentials(client_id=cid,
                                                      client_secret=secret)

sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

film, image_names = find_info_in_data(indices)


film_titles, years, genres = find_ost(film)

def get_playlists(film_titles, years):

    playlists = []
    #keywords = ['OST', 'soundtrack', 'motion', 'score']
    for title in range(len(film_titles):
        #for keyword in keywords:
        results = sp.search(q='album' + film_titles[title]
                            + ' ' + years[title] + keyword, market='GB')
        for i in results['tracks']['items']:
            if i['album']['total_tracks'] > 3:
                if i['album']['external_urls']['spotify'] not in playlists:
                    playlists.append((i['album']['external_urls']['spotify']))

    return playlists

def full_pl_dict(film_titles, playlists, genres)
    pl_dict = {}
    for title in range(len(film_titles):
        pl_dict[film_title[title]] = playlists[title], genres[title]

    return pl_dict
