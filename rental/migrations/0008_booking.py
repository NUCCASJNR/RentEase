# Generated by Django 4.0 on 2024-02-12 11:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0007_rename_agent_id_visitreport_agent_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('status', models.CharField(default='pending', max_length=10)),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='rental.apartment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='rental.mainuser')),
            ],
            options={
                'db_table': 'bookings',
            },
        ),
    ]
