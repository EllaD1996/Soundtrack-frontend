import streamlit as st
import streamlit.components.v1 as components

st.markdown('# soundtrack selectah')

#st.camera_input('take a pic')

st.file_uploader('upload a pic',
                 type=['png','jpg','jpeg'],
                 accept_multiple_files=False,
                 label_visibility='collapsed'
                 )

st.selectbox('pick a genre',[1,2,3,4,5])

#get links from spotify
pl_link = 'https://open.spotify.com/embed/album/5vdGNez4ZbeSUaeiFTPpcx'


if st.button('gimme a playlist'):

    st.title('it looks like you are in *insert film title*')
    st.write('this is your original soundtrack lol:')

    components.iframe(pl_link, width=700, height=300)
