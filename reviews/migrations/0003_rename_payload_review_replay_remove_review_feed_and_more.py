# Generated by Django 4.1.6 on 2023-03-27 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0002_initial'),
        ('reviews', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='payload',
            new_name='replay',
        ),
        migrations.RemoveField(
            model_name='review',
            name='feed',
        ),
        migrations.AddField(
            model_name='review',
            name='worklog',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='feeds.worklog'),
            preserve_default=False,
        ),
    ]
