# Generated by Django 4.0 on 2024-02-24 09:20

from django.db import migrations, models


class Migration(migrations.Migration):
    """ """

    dependencies = [
        ("rental", "0010_alter_mainuser_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="apartmentimage",
            name="image",
        ),
        migrations.AddField(
            model_name="apartmentimage",
            name="image_url",
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
