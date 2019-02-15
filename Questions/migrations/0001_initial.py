# Generated by Django 2.1.7 on 2019-02-15 18:01

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('AID', models.IntegerField(primary_key=True, serialize=False)),
                ('AName', models.CharField(max_length=3000)),
                ('AText', models.TextField()),
                ('Image', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EasterEggs',
            fields=[
                ('EID', models.IntegerField(primary_key=True, serialize=False)),
                ('PWeight', models.IntegerField()),
                ('Desc', models.CharField(max_length=1000)),
                ('AID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Questions.Achievements')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionInfo',
            fields=[
                ('QID', models.IntegerField(primary_key=True, serialize=False)),
                ('QText', models.TextField()),
                ('Image', models.URLField(blank=True)),
                ('Answer', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1000), size=10)),
                ('CloseAnswer', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1000), size=20)),
            ],
        ),
    ]
