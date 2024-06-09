# Generated by Django 4.2.7 on 2024-06-09 04:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('unlockk', '0006_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='friend',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friend',
            name='status',
            field=models.CharField(default='pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='friend',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
