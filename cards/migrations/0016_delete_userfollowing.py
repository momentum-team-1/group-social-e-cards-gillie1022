# Generated by Django 3.0.7 on 2020-07-02 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0015_auto_20200702_0025'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserFollowing',
        ),
    ]