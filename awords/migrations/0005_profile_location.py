# Generated by Django 3.1.2 on 2020-10-28 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awords', '0004_auto_20201028_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
