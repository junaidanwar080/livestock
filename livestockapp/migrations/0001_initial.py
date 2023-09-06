# Generated by Django 4.0 on 2023-09-06 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal_profile',
            fields=[
                ('animal_id', models.AutoField(primary_key=True, serialize=False)),
                ('token_no', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('color', models.CharField(max_length=50, null=True)),
                ('weight', models.CharField(max_length=50, null=True)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('purchase_price', models.IntegerField(null=True)),
                ('purchased_by', models.CharField(blank=True, max_length=50, null=True)),
                ('purchased_on', models.DateField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('description', models.TextField(max_length=50, null=True)),
                ('gender', models.CharField(max_length=50, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('created_by', models.CharField(max_length=50, null=True)),
                ('created_on', models.DateField(blank=True, null=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_on', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=50, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateField(blank=True, null=True)),
                ('updated_on', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=30, null=True)),
                ('gender', models.TextField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('date_of_birth', models.DateField(blank=True, max_length=50, null=True)),
                ('created_on', models.DateField(blank=True, null=True)),
                ('updated_on', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='PregnancyDetails',
            fields=[
                ('pregnancy_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_pregnancy_confirmed', models.BooleanField(null=True)),
                ('pregnancy_checked_on', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_delivery_completed', models.BooleanField(null=True)),
                ('actual_delivery_date', models.DateField(blank=True, null=True)),
                ('is_miscarriage', models.BooleanField(blank=True, null=True)),
                ('miscarriage_date', models.DateField(blank=True, null=True)),
                ('infartility', models.BooleanField(null=True)),
                ('is_pregnant', models.IntegerField(null=True)),
                ('pregnancy_start_date', models.DateField(blank=True, null=True)),
                ('pregnancy_end_date', models.DateField(blank=True, null=True)),
                ('created_on', models.DateField(blank=True, null=True)),
                ('updated_on', models.DateField(blank=True, null=True)),
                ('animal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='animals_id', to='livestockapp.animal_profile')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='create_by', to='livestockapp.animal_profile')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_by', to='livestockapp.animal_profile')),
            ],
        ),
        migrations.AddField(
            model_name='animal_profile',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='token_no', to='livestockapp.category'),
        ),
        migrations.AddField(
            model_name='animal_profile',
            name='person_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
