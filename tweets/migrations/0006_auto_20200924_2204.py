# Generated by Django 3.0.3 on 2020-09-24 15:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_auto_20200923_1524'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={},
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
