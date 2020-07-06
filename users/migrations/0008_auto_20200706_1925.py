# Generated by Django 3.0.7 on 2020-07-06 19:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200706_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followed_users',
            field=models.ManyToManyField(related_name='fans', to=settings.AUTH_USER_MODEL),
        ),
    ]
