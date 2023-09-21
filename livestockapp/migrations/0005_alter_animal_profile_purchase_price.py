# Generated by Django 4.0.5 on 2023-09-20 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livestockapp', '0004_remove_animal_profile_purchased_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal_profile',
            name='purchase_price',
            field=models.DecimalField(decimal_places=2, max_digits=13, null=True),
        ),
    ]