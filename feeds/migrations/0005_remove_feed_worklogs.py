# Generated by Django 4.1.6 on 2023-02-03 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_feed_worklogs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='worklogs',
        ),
    ]
