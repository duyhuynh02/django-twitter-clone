# Generated by Django 3.0.3 on 2020-09-29 00:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0008_auto_20200925_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='likes',
            field=models.ManyToManyField(related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='PostLikes',
        ),
    ]
