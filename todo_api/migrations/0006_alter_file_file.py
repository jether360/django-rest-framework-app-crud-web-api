# Generated by Django 4.1.7 on 2023-03-24 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0005_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='files/'),
        ),
    ]
