# Generated by Django 4.0.5 on 2022-07-11 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0002_stocks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='medicine_qty',
            field=models.IntegerField(),
        ),
    ]
