# Generated by Django 4.1.7 on 2023-03-24 06:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0006_alter_file_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('filename', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='files/')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'tbl_file_upload',
                'ordering': ['-createdAt'],
            },
        ),
    ]
