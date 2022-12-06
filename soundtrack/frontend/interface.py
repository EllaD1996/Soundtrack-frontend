import streamlit as st
import streamlit.components.v1 as components
from interface_backend import create_playlist
import requests



st.markdown('# soundtrack selectah')

#st.camera_input('take a pic')

uploaded_image = st.file_uploader('upload a pic',
                 type=['png','jpg','jpeg'],
                 accept_multiple_files=False,
                 label_visibility='collapsed'
                 ) # take care about the format, tf suport others?


if uploaded_image is not None:
    print(uploaded_image)
    #Local
    response = requests.post("http://0.0.0.0:8000/predict", files={"file":uploaded_image.getvalue()})
    #GCloud
    #response = requests.post("http://127.0.0.1:8000/image",files={"file":uploaded_image.getvalue()})
    st.write(response.status_code)
    st.write(type(response.json()))
    st.write(response.json())
    print('Image sended to the server')
    index_result = response.json()


    entire_playlist = create_playlist(index_result)










#get links from spotify
pl_link = 'https://open.spotify.com/embed/album/5vdGNez4ZbeSUaeiFTPpcx'


if st.button('gimme a playlist'):

    st.title('it looks like you are in *insert film title*')
    st.write('this is your original soundtrack lol:')

    components.iframe(pl_link, width=700, height=300)
