# Generated by Django 5.0.6 on 2024-07-11 05:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_userprofile_course_userprofile_is_company_and_more'),
        ('jobs', '0005_rename_description_job_job_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Job_Company'),
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date Updated ')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_author_bookmarks', to='accounts.userprofile')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_bookmarks', to='jobs.job')),
            ],
            options={
                'verbose_name': 'Bookmark',
                'verbose_name_plural': 'Bookmarks',
                'ordering': ['-created_at'],
            },
        ),
    ]