# Generated by Django 4.1.6 on 2023-03-02 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '유저 관리', 'verbose_name_plural': '유저 목록 관리'},
        ),
    ]
