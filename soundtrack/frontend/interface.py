import streamlit as st
import streamlit.components.v1 as components
from interface_backend import create_album
import requests
from soundtrack.spotify.spotify_api import get_playlist
from google.oauth2 import service_account
from google.cloud import storage



st.title('Soundtrack Selector')

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(http://placekitten.com/200/200);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "My Company Name";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
 )


add_logo()
st.camera_input('take a pic')
st.markdown(f'<h1 style="color:#33ff33;font-size:24px;font-family:arial">Soundtrack Selector</h1>', unsafe_allow_html=True)



#-----------------------------------------------------------------------------------------------------------------------------------------




uploaded_image = st.file_uploader('upload a pic',
                 type=['png','jpg','jpeg'],
                 accept_multiple_files=False,
                 label_visibility='collapsed'
                 ) # take care about the format, tf suport others?



#st.session_state

#----------------------------------------------------------------------------------------------------
if uploaded_image is not None: # "STEP_1" not in st.session_state.keys():
    print(uploaded_image)
    #Local
    response = requests.post("http://0.0.0.0:8000/predict", files={"file":uploaded_image.getvalue()})
    #GCloud
    #response = requests.post("https://ss-2uwfe4q3ia-ew.a.run.app/predict",files={"file":uploaded_image.getvalue()})

    #st.write(response.status_code)
    #st.write(type(response.json()))
    #st.write(response.json())
    #print('Image sended to the server')
    index_result = response.json()

    print('---ALBUM CREATED---')
    album_dict = create_album(index_result)
    st.session_state['album_names'] = album_dict

    # Run spotypi api
    if "STEP_1" not in st.session_state.keys():
        print("FIRST STEP COMPLETED")
        st.session_state["STEP_1"] = True
        print(st.session_state.keys())

#----------------------------------------------------------------------------------------------------
if "STEP_1" in st.session_state.keys():

    selected_genre = st.selectbox('Pick a genre', st.session_state['album_names'].values())

    for album_name, genre in st.session_state['album_names'].items():
        if genre==selected_genre:
        # PROBLEM WHEN WE HAVE THE SAME GENRES
            playlist = get_playlist(album_name).replace('https://open.spotify.com','https://open.spotify.com/embed')
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


    if st.button('gimme a playlist'):

        st.title('It looks like you are in *insert film title*')
        st.write('This is your original soundtrack lol:')
        components.iframe(st.session_state["playlist"], width=700, height=300)
