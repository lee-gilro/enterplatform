# Generated by Django 4.1.6 on 2023-02-05 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0006_remove_worklog_poster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worklog',
            name='photos',
        ),
        migrations.RemoveField(
            model_name='worklog',
            name='video',
        ),
    ]
