# Generated by Django 5.1.1 on 2024-11-11 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageupload',
            name='converted_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
