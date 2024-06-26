# Generated by Django 5.0.6 on 2024-05-21 17:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_address_education_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='superset_url',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_address', to='accounts.address'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='education',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_education', to='accounts.education'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='media/profile_pictures', verbose_name='Profile Picture'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
