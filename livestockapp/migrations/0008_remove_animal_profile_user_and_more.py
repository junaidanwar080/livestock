# Generated by Django 4.0.5 on 2023-10-02 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livestockapp', '0007_alter_animal_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal_profile',
            name='user',
        ),
        migrations.AddField(
            model_name='animal_profile',
            name='animal_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='animal_profile',
            name='purchased_party_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchased_animal', to='livestockapp.refpartyprofile'),
        ),
        migrations.AddField(
            model_name='animal_profile',
            name='shared_party_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shared_animal', to='livestockapp.refpartyprofile'),
        ),
    ]
