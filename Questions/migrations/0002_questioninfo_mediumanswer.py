# Generated by Django 2.1.7 on 2019-02-18 15:47

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questioninfo',
            name='MediumAnswer',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='', max_length=1000), default='', size=20),
        ),
    ]
