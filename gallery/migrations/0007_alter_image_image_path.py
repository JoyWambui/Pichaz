# Generated by Django 3.2.9 on 2021-11-28 21:49

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_alter_image_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_path',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
