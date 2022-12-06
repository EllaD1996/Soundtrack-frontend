import streamlit as st
import streamlit.components.v1 as components
from interface_backend import create_playlist
import requests

st.title('Soundtrack Selector')

# def add_logo():
#     st.markdown(
#         """
#         <style>
#             [data-testid="stSidebarNav"] {
#                 background-image: url(http://placekitten.com/200/200);
#                 background-repeat: no-repeat;
#                 padding-top: 120px;
#                 background-position: 20px 20px;
#             }
#             [data-testid="stSidebarNav"]::before {
#                 content: "My Company Name";
#                 margin-left: 20px;
#                 margin-top: 20px;
#                 font-size: 30px;
#                 position: relative;
#                 top: 100px;
#             }
#         </style>
#         """,
#         unsafe_allow_html=True,
    # )

# add_logo()
# #st.camera_input('take a pic')
# st.markdown(f'<h1 style="color:#33ff33;font-size:24px;font-family:arial">Soundtrack Selector</h1>', unsafe_allow_html=True)

uploaded_image = st.file_uploader('upload a pic',
                 type=['png','jpg','jpeg'],
                 accept_multiple_files=False,
                 label_visibility='collapsed'
                 ) # take care about the format, tf suport others?


if uploaded_image is not None:
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


    playlist_link = create_playlist(index_result)


#get links from spotify
#pl_link = 'https://open.spotify.com/embed/album/5vdGNez4ZbeSUaeiFTPpcx'

if st.button('gimme a playlist'):

    st.title('it looks like you are in *insert film title*')
    st.write('this is your original soundtrack lol:')

    components.iframe(playlist_link, width=700, height=300)
