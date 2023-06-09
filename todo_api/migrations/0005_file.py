# Generated by Django 4.1.7 on 2023-03-24 03:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0004_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('filename', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'tbl_file',
                'ordering': ['-createdAt'],
            },
        ),
    ]
