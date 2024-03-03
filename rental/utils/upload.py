#!/usr/bin/env python3

"""Contains image upload utilities"""

from os import getenv
from dotenv import load_dotenv
import requests
import base64
from PIL import Image
import io

load_dotenv()

IMGUR_CLIENT_ID = getenv('IMGUR_CLIENT_ID')


def resize_image(image, max_width=800, max_height=600):
    img = Image.open(image)
    img.thumbnail((max_width, max_height), Image.ANTIALIAS)
    output = io.BytesIO()
    img.save(output, format='JPEG')  # You can choose the desired format here
    output.seek(0)
    return output


def upload_images_to_imgur(images, apartment_id):
    uploaded_images_url = []
    url = "https://api.imgur.com/3/image"
    headers = {
        "Authorization": f"Client-ID {IMGUR_CLIENT_ID}"
    }
    for image in images:
        resized_image = resize_image(image)
        image_base64 = base64.b64encode(resized_image.read()).decode('utf-8')
        request_payload = {
            "image": image_base64,
            "type": "base64",
            "title": f"Apartment image: {apartment_id}"
        }
        try:
            response = requests.post(url, json=request_payload, headers=headers)
            if response.status_code == 200 and response.json()['success']:
                uploaded_images_url.append(response.json()['data']['link'])
            else:
                print(f'Error Uploading image: {response.text}')
        except Exception as e:
            print(f'Error uploading image due to: {str(e)}')
    return uploaded_images_url

# Path: Rental/utils/upload.py
