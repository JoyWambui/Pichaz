# Generated by Django 3.2.9 on 2021-11-26 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_remove_image_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.location'),
        ),
    ]
