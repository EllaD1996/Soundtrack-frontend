import streamlit as st
import numpy as np
import streamlit.components.v1 as components
from soundtrack.discogs.discogs_api import find_ost
from soundtrack.spotify.spotify_api import get_playlists
import requests
import json
from PIL import Image



st.markdown('# soundtrack selectah')

#st.camera_input('take a pic')

raw_image = st.file_uploader('upload a pic',
                 type=['png','jpg','jpeg'],
                 accept_multiple_files=False,
                 label_visibility='collapsed'
                 )

if raw_image is not None:
    arrayed_img = np.array(Image.open(raw_image))

    st.write(arrayed_img.shape)


    # Request and response
    response = requests.post("http://0.0.0.0:8000/predict", json=json.dumps(arrayed_img.tolist()))
    #response = requests.post("https://ss-2uwfe4q3ia-ew.a.run.app/predict", json=json.dumps(arrayed_img.tolist()))
    print(response.json())




playlist = get_playlists(films)

st.selectbox('pick a genre',[1,2,3,4,5])





#get links from spotify
pl_link = 'https://open.spotify.com/embed/album/5vdGNez4ZbeSUaeiFTPpcx'


if st.button('gimme a playlist'):

    st.title('it looks like you are in *insert film title*')
    st.write('this is your original soundtrack lol:')

    components.iframe(pl_link, width=700, height=300)
