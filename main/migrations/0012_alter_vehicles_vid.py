# Generated by Django 4.1.7 on 2023-03-13 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rename_email_user_emailadresse_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicles',
            name='vid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
