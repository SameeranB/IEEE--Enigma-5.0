# Generated by Django 2.1.2 on 2018-12-30 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LoginSignup', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='achievement',
            name='user',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Achievement',
        ),
    ]