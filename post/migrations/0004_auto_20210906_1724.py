# Generated by Django 3.2.7 on 2021-09-06 12:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 6, 17, 24, 49, 130130), verbose_name=datetime.datetime(2021, 9, 6, 17, 24, 49, 130130)),
        ),
        migrations.AddField(
            model_name='post',
            name='isPublished',
            field=models.BooleanField(default=False),
        ),
    ]