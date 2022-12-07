from google.cloud import storage
import numpy as np
import cv2
from matplotlib import pyplot as plt
import pandas as pd
from google.oauth2 import service_account

#####need to have indice from model MISSING



#def return_index(credencials):
#    """
#    Summary:Returns bucket index and names for given indices
#    Input: None
#    Return: bucket items -> DataFrame
#    """
#    client = storage.Client(credentials=credencials)
#    bucket_name = 'image-storage-stills'
#    bucket = client.get_bucket(bucket_name)
#    dirname = 'New_Image/'
#    blobs = bucket.list_blobs(prefix=dirname)
#    indx = []
#
#    for blob in blobs:
#        indx.append(blob.name)
#    df = pd.DataFrame(indx, columns=["Image_Name"])
#
#    return df

def find_info_in_data(indices, data='local'):
    """
    Summary: Runs through the movie data and builds list with: title, year, genre and image name
    Input:
    indices -> list [1,2,3, 4,5]
    data -> local: read data local, web: read data in gcloud (not working)
    Return: film_info and images names-> tuple
    """
    if data == 'web':
        data = pd.read_csv("gs://image-storage-stills/dataset/new_data_13k.csv")
    if data == 'local':
        data = pd.read_csv("soundtrack/data/new_data_13k.csv")

    info = []
    image_names = []
    for index in indices:
        name = data.loc[index, 'Image_name']
        title = (data.loc[index, 'Title']).capitalize()
        year = data.loc[index, 'Year']
        genre = data.loc[index, 'Genre']
        info.append([title, year, genre])
        image_names.append(name)

    return info, image_names

def get_image(image_names,credencials):
    """
    Summary: Given the image names, get image from bucket
    Input: images names -> list
    Return: actual images -> string?
    """
    client =  storage.Client(credentials=credencials)
    bucket = client.get_bucket('image-storage-stills')
    images = []
    for name in image_names:
        dirname = 'New_Image/'
        blob = bucket.get_blob(name, prefix=dirname)
        image = blob.download_as_string()
        images.append(image)
    return images


def load_data_new_image(image):
    """
    Summary: Function to load the image
    Input: image -> string
    Return: readable image -> np.array
    """
    return np.array(cv2.imdecode(
                np.asarray(
                    bytearray(image), dtype=np.uint8), -1)
                                )

def show_image(indices,credentials):
    """
    Summary: Shows image.shocking
    Input: indices -> np.array
    Return: original image -> .png
    """
    info, image_names = find_info_in_data(indices)
    images = get_image(image_names,credentials)
    for image in images:
        out = load_data_new_image(image)
        plt.imshow(out)
        plt.show();
