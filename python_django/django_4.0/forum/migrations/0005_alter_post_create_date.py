# Generated by Django 4.0 on 2023-10-12 10:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_alter_post_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 12, 10, 25, 30, 581502, tzinfo=utc)),
        ),
    ]
