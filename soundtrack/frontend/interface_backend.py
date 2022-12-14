from soundtrack.discogs.discogs_api import find_ost

from soundtrack.indices.indices import find_info_in_data, get_image

def create_album(index_result):
    print('Process Complete finding your playlist...')
    list_index = index_result['idx']
    print(list_index)

    # Searching for the movie title
    movies_info, images = find_info_in_data(list_index)
    movies_titles = [movie[0] for movie in movies_info]

    # Run discogs api
    album_dict = find_ost(movies_titles)
    print(album_dict)

    return album_dict

    # Run spotypi api
    #playlist = get_playlists(pl).replace('https://open.spotify.com','https://open.spotify.com/embed')

    #Return input to put the playlist in streamlit

def get_scene_image(indeces):
    info = []
    print('################################')
    print(f"INDEX : {indeces['idx']}")
    print(f"TYPE INDEX : {type(indeces['idx'])}")

    info_films, images_names = find_info_in_data(indeces['idx'])
    for index in range(len(info_films)):
        info.append((info_films[index][0], images_names[index]))
    return info
