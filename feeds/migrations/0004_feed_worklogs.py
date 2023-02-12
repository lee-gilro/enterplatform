# Generated by Django 4.1.6 on 2023-02-03 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0003_alter_feed_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='worklogs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='feeds', to='feeds.worklog'),
        ),
    ]
