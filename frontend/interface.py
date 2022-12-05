import streamlit as st
import numpy as np
import streamlit.components.v1 as components
from soundtrack-frontend.discogs import find_ost
from soundtrack-frontend.spotify import get_playlists



st.markdown('# soundtrack selectah')

#st.camera_input('take a pic')

raw_image = st.file_uploader('upload a pic',
                 type=['png','jpg','jpeg'],
                 accept_multiple_files=False,
                 label_visibility='collapsed'
                 )

arrayed_img = np.array(raw_image)

""" NEED MODELS RUNNING HERE AND RETURNING FILMS"""

find_ost(film)


get_playlists(ost_name)

st.selectbox('pick a genre',[1,2,3,4,5])





#get links from spotify
pl_link = 'https://open.spotify.com/embed/album/5vdGNez4ZbeSUaeiFTPpcx'


if st.button('gimme a playlist'):

    st.title('it looks like you are in *insert film title*')
    st.write('this is your original soundtrack lol:')

    components.iframe(pl_link, width=700, height=300)
