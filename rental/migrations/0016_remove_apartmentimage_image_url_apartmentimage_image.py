# Generated by Django 4.0 on 2024-03-07 11:23

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0015_alter_apartment_assigned_agent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartmentimage',
            name='image_url',
        ),
        migrations.AddField(
            model_name='apartmentimage',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]