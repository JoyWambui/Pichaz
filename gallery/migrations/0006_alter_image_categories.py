# Generated by Django 3.2.9 on 2021-11-28 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_image_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='categories',
            field=models.ManyToManyField(related_query_name='images', to='gallery.Category'),
        ),
    ]
