# Generated by Django 3.0.7 on 2020-07-02 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_followers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='followers',
            new_name='follows',
        ),
    ]
