#!/usr/bin/env python3

"""Contains image upload utilities"""

from os import getenv
from dotenv import load_dotenv
import requests

load_dotenv()

IMGUR_CLIENT_ID = getenv('IMGUR_CLIENT_ID')


def upload_image_to_imgur(image, image_id):
    """
    Uploads an image to imgur
    :param image: The image to upload
    :param image_id: The id of the image
    :return: The link to the uploaded image
    """
    url = "https://api.imgur.com/3/image"
    headers = {
        "Authorization": f"Client-ID {IMGUR_CLIENT_ID}"
    }
    request_payload = {
        "image": image,
        "type": "file",
        "title": f"Apartment image {image_id}"
    }
    try:
        response = requests.post(url, headers=headers, data=request_payload)
        if response.status_code == 200 and response.json()['success']:
            return response.json()['data']['link']
        else:
            print('Error Uploading image')
    except Exception as e:
        print(f'Error uploading image due to: {str(e)}')
