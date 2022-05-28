# Generated by Django 3.2 on 2022-05-28 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empanelment',
            name='status',
            field=models.IntegerField(choices=[(1, 'contacted'), (2, 'inprocess'), (3, 'verified'), (4, 'refused')], default=2),
        ),
    ]
