# Generated by Django 3.0.3 on 2020-09-25 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0007_tweet_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='likes',
        ),
        migrations.CreateModel(
            name='PostLikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.Tweet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]