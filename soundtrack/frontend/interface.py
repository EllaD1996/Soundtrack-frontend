import streamlit as st
import streamlit.components.v1 as components
from interface_backend import create_album
import requests
from soundtrack.spotify.spotify_api import get_playlist
from css import get_css

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


if uploaded_image is not None and "RAN" not in st.session_state.keys():
    print(uploaded_image)
    #Local
    #local_response = requests.post("http://0.0.0.0:8000/predict", files={"file":uploaded_image.getvalue()})
    #GCloud

    response = requests.post("https://ss-2uwfe4q3ia-ew.a.run.app/predict",files={"file":uploaded_image.getvalue()})

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
