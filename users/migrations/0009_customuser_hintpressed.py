# Generated by Django 2.1.7 on 2019-02-23 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_customuser_attempts'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='HintPressed',
            field=models.BooleanField(default=False),
        ),
    ]