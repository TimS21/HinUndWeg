# Generated by Django 4.1.7 on 2023-02-28 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_vehicles_preisprotag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicles',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
