# Generated by Django 4.1.6 on 2023-03-28 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likelists', '0001_initial'),
        ('feeds', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worklog',
            name='likelists',
            field=models.ManyToManyField(blank=True, related_name='liked_worklogs', to='likelists.likelist'),
        ),
    ]
