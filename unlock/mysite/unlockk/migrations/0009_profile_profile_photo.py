# Generated by Django 5.0.3 on 2024-06-11 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unlockk', '0008_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
