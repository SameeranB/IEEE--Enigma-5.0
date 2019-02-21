from django.db import models
from djongo import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class QuestionInfo(models.Model):
    QID = models.IntegerField(primary_key=True)
    QText = models.TextField(blank=True)
    Image = models.URLField(blank= True)
    QuesSolved = models.IntegerField(default=1)
    Answer = ArrayField(models.CharField(max_length=1000), size=10)
    CloseAnswer = ArrayField(models.CharField(max_length=1000), size=20)
    MediumAnswer = ArrayField(models.CharField(max_length=1000,default=''), size=20)



class Achievements(models.Model):

    AID = models.IntegerField(primary_key=True)
    AName = models.CharField(max_length=3000)
    AText = models.TextField()
    Image = models.URLField(blank=True)

class EasterEggs(models.Model):
    EID = models.IntegerField(primary_key=True)
    PWeight = models.IntegerField()
    AID = models.ForeignKey(Achievements, on_delete=models.CASCADE)
    Desc = models.CharField(max_length=1000)



