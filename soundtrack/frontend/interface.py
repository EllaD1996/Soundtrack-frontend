import streamlit as st
import streamlit.components.v1 as components
from interface_backend import create_album, get_scene_image
import requests
from soundtrack.spotify.spotify_api import get_playlist
from css import get_css
from google.oauth2 import service_account
from google.cloud import storage

st.set_page_config(layout='wide')

st.markdown(get_css(), unsafe_allow_html=True)
st.sidebar.image("Picture2.png", use_column_width=True)


col1, col2 = st.columns([5, 1])

with col1:
    st.markdown(f'<h1 style="color:#FFB341;font-size:100px;font-family:cooper black">Soundtrack<br>Selector</h1>', unsafe_allow_html=True)

with col2:
    st.image("Picture2.png", width = 175, use_column_width=False)


st.sidebar.markdown("### Find your  ideal soundtrack for your surroundings")
st.sidebar.markdown("Welcome to our app! Here you can submit an image and get the perfect soundtrack to listen to for your environment")


col_1, col_2 = st.columns(2)

with col_1:
    st.markdown(f'<h1>          <br>              <br>           <br>              </h1>', unsafe_allow_html=True)
#-----------------------------------------------------------------------------------------------------------------------------------------




uploaded_image = st.file_uploader('upload a pic',
                 type=['png','jpg','jpeg'],
                 accept_multiple_files=False,
                 label_visibility='collapsed'
                 ) # take care about the format, tf suport others?



#st.session_state

#----------------------------------------------------------------------------------------------------
if uploaded_image is not None: # "STEP_1" not in st.session_state.keys():
    st.image(uploaded_image)
    #Local
    #response = requests.post("http://0.0.0.0:8000/predict", files={"file":uploaded_image.getvalue()})
    #GCloud

    response = requests.post("https://ss-2uwfe4q3ia-ew.a.run.app/predict",files={"file":uploaded_image.getvalue()})

    #st.write(response.status_code)
    #st.write(type(response.json()))
    #st.write(response.json())
    #print('Image sended to the server')
    index_result = response.json()

    album_dict = create_album(index_result)

    print(album_dict)
    print('---ALBUM CREATED---')

    st.session_state['album_names'] = album_dict

    # Run spotypi api
    if "STEP_1" not in st.session_state.keys():
        print("FIRST STEP COMPLETED")
        st.session_state["STEP_1"] = True
        print(st.session_state.keys())

#----------------------------------------------------------------------------------------------------
if "STEP_1" in st.session_state.keys():

    selected_genre = st.selectbox('Pick a genre', st.session_state['album_names'].values())

    print(st.session_state["album_names"])
    for album_name, genre in st.session_state['album_names'].items():
        if genre==selected_genre:
        # PROBLEM WHEN WE HAVE THE SAME GENRES
            playlist = get_playlist(album_name).replace('https://open.spotify.com',
                                                        'https://open.spotify.com/embed')
            st.session_state['playlist'] = playlist

    if 'STEP_2' not in st.session_state.keys():
        print("SECOND STEP COMPLETAED")
        st.session_state["STEP_2"] = True
        print(st.session_state.keys())

#----------------------------------------------------------------------------------------------------
#
#
#if "STEP_2" not in st.session_state.keys() and "STEP_1" in st.session_state.keys():
#
#    selected_genre = st.selectbox('Pick a genre', album_dict.values())
#
#    for album_name, genre in album_dict.items():
#        if genre==selected_genre:
#        # PROBLEM WHEN WE HAVE THE SAME GENRES
#            playlist = get_playlist(album_name).replace('https://open.spotify.com','https://open.spotify.com/embed')
#            st.session_state['playlist'] = playlist
#
#    if 'STEP_2' not in st.session_state.keys():
#        print("SECOND STEP COMPLETAED")
#        st.session_state["STEP_2"] = True
#        print(st.session_state.keys())
#
#----------------------------------------------------------------------------------------------------


if "playlist" in st.session_state.keys():# and "STEP_1" in st.session_state.keys():
    print(f'PLAYLIST CRATED FOR YOUR CHOSEE : {st.session_state["playlist"]}')

    #get links from spotify
    pl_link = 'https://open.spotify.com/embed/album/5vdGNez4ZbeSUaeiFTPpcx'


    if st.button('Give me a playlist'):

        st.write('This is your selected soundtrack')
        components.iframe(st.session_state["playlist"], width=700, height=300)


        movies_tuple = get_scene_image(index_result)
        for item in movies_tuple:
            film_title = item[0]
            image_names = item[1]
            image_url = f'https://storage.googleapis.com/image-storage-stills/New_Image/{image_names}'
            st.image(image_url)
            st.write(film_title)
