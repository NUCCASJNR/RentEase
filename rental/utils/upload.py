#!/usr/bin/env python3

"""Contains image upload utilities"""

from os import getenv
from dotenv import load_dotenv
import requests
import base64

load_dotenv()

IMGUR_CLIENT_ID = getenv("IMGUR_CLIENT_ID")


def upload_images_to_imgur(images, apartment_id):
    """
    Uploads an image to imgur
    :param images: The images to upload
    :param apartment_id: The id of the image
    :return: The link to the uploaded image
    """
    uploaded_images_url = []
    url = "https://api.imgur.com/3/image"
    headers = {"Authorization": f"Client-ID {IMGUR_CLIENT_ID}"}
    for image in images:
        image_base64 = base64.b64encode(image).decode("utf-8")
        request_payload = {
            "image": image_base64,
            "type": "base64",
            "title": f"Apartment image: {apartment_id}",
        }
        try:
            response = requests.post(url, json=request_payload, headers=headers)
            if response.status_code == 200 and response.json()["success"]:
                uploaded_images_url.append(response.json()["data"]["link"])
            else:
                print(f"Error Uploading image: {response.text}")
        except Exception as e:
            print(f"Error uploading image due to: {str(e)}")
    return uploaded_images_url


# Path: Rental/utils/upload.py
