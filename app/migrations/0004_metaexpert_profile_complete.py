# Generated by Django 3.2 on 2022-06-06 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20220601_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='metaexpert',
            name='profile_complete',
            field=models.BooleanField(default=False),
        ),
    ]