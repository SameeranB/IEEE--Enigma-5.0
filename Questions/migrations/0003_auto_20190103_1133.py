# Generated by Django 2.1.2 on 2019-01-03 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0002_auto_20181230_1051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprogress',
            old_name='CurrentAnswer',
            new_name='Answer',
        ),
    ]
