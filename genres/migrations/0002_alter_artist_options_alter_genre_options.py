# Generated by Django 4.1.6 on 2023-03-02 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'verbose_name': '참조 아티스트 관리', 'verbose_name_plural': '참조 아티스트 목록 관리'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': '장르 관리', 'verbose_name_plural': '장르 목록 관리'},
        ),
    ]