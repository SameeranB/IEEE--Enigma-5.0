# Generated by Django 2.1.2 on 2018-12-20 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LoginSignup', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
