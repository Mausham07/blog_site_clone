# Generated by Django 4.1 on 2023-02-18 05:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 18, 5, 59, 2, 727621, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 18, 5, 59, 2, 727175, tzinfo=datetime.timezone.utc)),
        ),
    ]