# Generated by Django 4.1.6 on 2023-03-02 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': '댓글관리 관리', 'verbose_name_plural': '댓글 목록 관리'},
        ),
    ]
