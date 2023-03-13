# Generated by Django 4.1.7 on 2023-03-13 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_type_type_alter_user_uid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='eMail',
            new_name='EMailAdresse',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='nName',
            new_name='Nachname',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='vName',
            new_name='Vorname',
        ),
        migrations.AddField(
            model_name='vehicles',
            name='standort',
            field=models.CharField(choices=[('DHBW-Mannheim', 'DHBW-Mannheim'), ('Hauptbahnhof Mannheim', 'Hauptbahnhof Mannheim'), ('Wasserturm Mannheim', 'Wasserturm Mannheim')], default='DHBW-Mannheim', max_length=21),
        ),
    ]