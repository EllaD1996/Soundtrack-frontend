import streamlit as st
import streamlit.components.v1 as components
from interface_backend import create_album
import requests
from soundtrack.spotify.spotify_api import get_playlist

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


if uploaded_image is not None and "RAN" not in st.session_state.keys():
    print(uploaded_image)
    #Local
    #local_response = requests.post("http://0.0.0.0:8000/predict", files={"file":uploaded_image.getvalue()})
    #GCloud

    #response = requests.post("https://ss-2uwfe4q3ia-ew.a.run.app/predict",files={"file":uploaded_image.getvalue()})

    st.write(response.status_code)
    st.write(type(response.json()))
    st.write(response.json())
    print('Image sended to the server')
    index_result = response.json()

    print('---ALBUM CREATED---')
    album_dict = create_album(index_result)

    # Run spotypi api


    if "RAN" not in st.session_state.keys():
        print("First RAN CREATED")
        st.session_state["RAN"] = True
        print(st.session_state.keys())


if "RAN set playlist" not in st.session_state.keys() and "RAN" in st.session_state.keys():

    selected_genre = st.selectbox('pick a genre', album_dict.values())

    for album_name, genre in album_dict.items():

        print(f'Album: {album_name}')
        print(f'Genre: {genre}')
        if genre==selected_genre:
        # PROBLEM WHEN WE HAVE THE SAME GENRES
            playlist = get_playlist(album_name).replace('https://open.spotify.com','https://open.spotify.com/embed')
            st.session_state['playlist'] = playlist

    if 'RAN set playlist' not in st.session_state.keys():
        print("Second RAN")
        st.session_state["RAN set playlist"] = True
        print(st.session_state.keys())


    for i in album_dict:
        if album_dict[i]==selected_genre:
            pl = i

    # Run spotypi api
    playlist = get_playlist(pl).replace('https://open.spotify.com','https://open.spotify.com/embed')



if "RAN set playlist" in st.session_state.keys() and "RAN" in st.session_state.keys():
    print(f'PLAYLIST CRATED FOR YOUR CHOSEE : {st.session_state["playlist"]}')

    #get links from spotify
    pl_link = 'https://open.spotify.com/embed/album/5vdGNez4ZbeSUaeiFTPpcx'


    if st.button('gimme a playlist'):

        st.title('it looks like you are in *insert film title*')
        st.write('this is your original soundtrack lol:')


        components.iframe(st.session_state["playlist"], width=700, height=300)

