# Generated by Django 4.1.6 on 2023-03-02 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': '투표 답변 관리', 'verbose_name_plural': '투표 답변 목록 관리'},
        ),
        migrations.AlterModelOptions(
            name='vote',
            options={'verbose_name': '투표 관리', 'verbose_name_plural': '투표 목록 관리'},
        ),
    ]
