from django.db import models
from djongo import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class QuestionInfo(models.Model):
    QID = models.IntegerField(primary_key=True)
    QText = models.TextField()
    Image = models.URLField(blank= True)
    Answer = ArrayField(models.CharField(max_length=1000), size=10)
    CloseAnswer = ArrayField(models.CharField(max_length=1000), size=20)


class Achievements(models.Model):

    AID = models.IntegerField(primary_key=True)
    AText = models.TextField()
    Image = models.URLField(blank=True)

