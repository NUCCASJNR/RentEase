#!/usr/bin/env python3
"""Celery task handler"""
import logging

from celery import shared_task

from rental.models.apartment import Apartment
from rental.models.apartment import ApartmentImage
from rental.utils.email_utils import EmailUtils
from rental.utils.upload import upload_images_to_imgur

logger = logging.getLogger(__name__)


@shared_task
def upload_apartment_images_task(apartment_id, images):
    """Task to upload apartment images to imgur

    :param apartment_id: The id of the apartment
    :param images: The images to upload
    :returns: None

    """
    try:
        uploaded_images_urls = upload_images_to_imgur(images, apartment_id)
        # Batch save uploaded images
        apartment = Apartment.objects.get(id=apartment_id)
        apartment_images = []
        for image_url in uploaded_images_urls:
            apartment_images.append(
                ApartmentImage(apartment=apartment, image_url=image_url)
            )
        ApartmentImage.objects.bulk_create(apartment_images)
        return {
            "message": "Apartment images uploaded successfully",
            "uploaded_images_count": len(uploaded_images_urls),
            "uploaded_image_urls": uploaded_images_urls,
        }
    except Exception as e:
        logging.error(f"Error uploading apartment images due to: {str(e)}")
        return {"error": f"Error uploading apartment images: {str(e)}"}


@shared_task
def send_verification_email_async(user, verification_code):
    """

    :param user: 
    :param verification_code: 

    """
    EmailUtils.send_verification_email(user, verification_code)


# Path: rental/utils/tasks.py
