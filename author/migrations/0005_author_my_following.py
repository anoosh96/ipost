# Generated by Django 3.2.7 on 2021-09-10 17:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0004_author_my_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='my_following',
            field=models.ManyToManyField(related_name='_author_author_my_following_+', through='author.AuthorFollowing', to=settings.AUTH_USER_MODEL),
        ),
    ]
