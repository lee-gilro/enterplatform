# Generated by Django 4.1.6 on 2023-03-15 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bankname', models.CharField(max_length=50)),
                ('bankcode', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '연결은행',
                'verbose_name_plural': '연결 은행 목록',
            },
        ),
    ]