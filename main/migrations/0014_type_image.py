# Generated by Django 4.1.7 on 2023-03-27 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_location_remove_vehicles_standort_vehicles_lid'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='image',
            field=models.ImageField(default='e-Bike.jpg', upload_to='static/images/'),
        ),
    ]
