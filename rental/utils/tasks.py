#!/usr/bin/env python3

"""Celery task handler"""

import logging

from celery import shared_task

from rental.models.apartment import Apartment, ApartmentImage
from rental.utils.upload import upload_images_to_imgur

logger = logging.getLogger(__name__)


@shared_task
def upload_apartment_images_task(apartment_id, images):
    """
    Task to upload apartment images to imgur
    :param apartment_id: The id of the apartment
    :param images: The images to upload
    :return: None
    """
    uploaded_images_url = []
    try:
        uploaded_images_url = upload_images_to_imgur(images, apartment_id)
        for image_url in uploaded_images_url:
            ApartmentImage.custom_save(
                **{
                    "apartment": Apartment.objects.get(id=apartment_id),
                    "image_url": image_url,
                }
            )
    except Exception as e:
        logging.error(f"Error uploading apartment images due to: {str(e)}")
    return {
        "message": "Apartment images uploaded successfully",
        "uploaded_images_count": len(uploaded_images_url),
        "uploaded_image_urls": uploaded_images_url,
    }


# Path: rental/utils/tasks.py
