# Generated by Django 4.0 on 2023-09-06 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livestockapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal_profile',
            old_name='person_id',
            new_name='person',
        ),
    ]