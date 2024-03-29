# Generated by Django 4.0 on 2024-02-12 10:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0003_alter_agent_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('number_of_rooms', models.IntegerField()),
                ('number_of_bathrooms', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amenities', models.JSONField(blank=True, null=True)),
                ('availability_status', models.CharField(choices=[('available', 'Available'), ('pending', 'Pending'), ('rented', 'Rented')], default='pending', max_length=10)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartments', to='rental.mainuser')),
            ],
            options={
                'db_table': 'apartments',
            },
        ),
    ]
