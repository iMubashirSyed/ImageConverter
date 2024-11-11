# Generated by Django 5.1.3 on 2024-11-11 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_image', models.ImageField(upload_to='uploads/originals/')),
                ('converted_image', models.ImageField(blank=True, null=True, upload_to='uploads/converted/')),
                ('conversion_task_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
