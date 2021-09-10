# Generated by Django 3.2.7 on 2021-09-10 07:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0006_alter_post_createdat'),
        ('author','0001_initial')
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 10, 12, 26, 14, 530255), verbose_name=datetime.datetime(2021, 9, 10, 12, 26, 14, 530255)),
        ),
    ]