# Generated by Django 2.1.7 on 2019-02-23 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20190223_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='Achievements',
            field=models.DateTimeField(blank=True),
        ),
    ]
