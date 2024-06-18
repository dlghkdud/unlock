# Generated by Django 3.2.25 on 2024-06-18 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unlockk', '0010_remove_profile_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_unlockk_userprofile_friends_+', to='unlockk.UserProfile'),
        ),
        migrations.AlterField(
            model_name='write',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
