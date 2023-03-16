# Generated by Django 4.1.6 on 2023-03-15 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payloads', models.TextField(max_length=300)),
                ('backgroundimage', models.ImageField(blank=True, null=True, upload_to='images')),
                ('on_public', models.BooleanField(default=True)),
                ('feed_name', models.CharField(default='', max_length=150)),
            ],
            options={
                'verbose_name': '피드 관리',
                'verbose_name_plural': '피드 목록 관리',
            },
        ),
        migrations.CreateModel(
            name='WorkLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payload', models.TextField(max_length=250)),
                ('is_shop', models.BooleanField(default=False)),
                ('on_public', models.BooleanField(default=False)),
                ('posted_feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worklogs', to='feeds.feed')),
            ],
            options={
                'verbose_name': '워크로그 관리',
                'verbose_name_plural': '워크로그 목록 관리',
            },
        ),
    ]
