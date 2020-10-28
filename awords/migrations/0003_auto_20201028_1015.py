# Generated by Django 3.1.2 on 2020-10-28 07:15

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awords', '0002_auto_20201025_2223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='screen1',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='screen2',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
    ]
