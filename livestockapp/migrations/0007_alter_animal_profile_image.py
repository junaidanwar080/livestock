# Generated by Django 4.0.5 on 2023-09-23 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livestockapp', '0006_animal_profile_is_shared'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal_profile',
            name='image',
            field=models.FileField(null=True, upload_to='images/'),
        ),
    ]
