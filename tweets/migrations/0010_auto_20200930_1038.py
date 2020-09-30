# Generated by Django 3.0.3 on 2020-09-30 03:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0009_auto_20200929_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='likes',
            field=models.ManyToManyField(related_name='tweet_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
