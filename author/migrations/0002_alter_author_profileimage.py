# Generated by Django 3.2.7 on 2021-09-10 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profileImage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]