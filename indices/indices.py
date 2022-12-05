from google.cloud import storage
import numpy as np
import cv2
from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv("gs://image-storage-stills/dataset/final_dataframe.csv")

#####need to have indice from model MISSING

"""Returns bucket index and names for given indices"""

def return_index(indices):
    client = storage.Client()
    bucket_name = 'image-storage-stills'
    bucket = client.get_bucket(bucket_name)
    dirname = 'New_Image/'
    blobs = bucket.list_blobs(prefix=dirname)
    indx = []

    for blob in blobs:
        indx.append(blob.name)
    df = pd.DataFrame(indx, columns=["Image_Name"])

    return df

"""Runs through the movie data and builds list with:
                                    title, year, genre and image name"""

def find_info_in_data(indices):
    info = []
    image_names = []

    for i in range(len(indices[0])):
        index = indices[0][i]
        name = df._get_value(index, "Image_Name")
        nindex = data.index[data['Image_name'] == name]
        title = (data.loc[nindex, 'Title'].item()).capitalize()
        year = data.loc[nindex, 'Year'].item()
        genre = data.loc[nindex, 'Genre'].item()
        info.append([title, year, genre])
        image_names.append(name)

    return info, image_names

"""Given the image names, get image from bucket"""

def get_image(image_names):
    client =  storage.Client()
    bucket = client.get_bucket('image-storage-stills')
    images = []
    for name in image_names:
        dirname = 'New_Image/'
        blob = bucket.get_blob(name, prefix=dirname)
        image = blob.download_as_string()
        images.append(image)

    return images


"""Function to load the image"""

def load_data_new_image(image):
            return np.array(cv2.imdecode(
                        np.asarray(
                            bytearray(image), dtype=np.uint8), -1
                                    )
                                        )

"""Shows image.shocking"""


def show_image(indices):
    info, image_names = find_info_in_data(indices)
    images = get_image(image_names)
    for image in images:
        out = load_data_new_image(image)
        plt.imshow(out)
        plt.show();
