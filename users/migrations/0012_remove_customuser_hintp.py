# Generated by Django 2.1.7 on 2019-02-23 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20190223_0525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='HintP',
        ),
    ]
