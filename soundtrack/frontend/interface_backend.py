from soundtrack.discogs.discogs_api import find_ost
from soundtrack.spotify.spotify_api import get_playlists
from soundtrack.indices.indices import find_info_in_data

def create_playlist(index_result):
    print('Process Complete finding your playlist...')
    list_index = index_result['idx']
    print(list_index)

    # Searching for the movie title
    movies_info, images = find_info_in_data(list_index)
    movies_titles = [movie[0] for movie in movies_info]

    # Run dicogs api
    album_dict = find_ost(movies_titles)

    # Run spotypi api
    #playlists = get_playlists(album_dict.keys())

    # show result

    #Return input to put the playlist in streamlit




#playlist = get_playlists(films)
#
selected_genre = st.selectbox('pick a genre',album_dict.values())

for i in album_dict:
    if album_dict[i]==selected_genre:
        pl = i