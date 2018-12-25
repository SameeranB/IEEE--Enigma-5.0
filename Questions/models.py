from django.db import models
from djongo import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Achievement(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Achievements = ArrayField(models.CharField(max_length=1000), size=20)


class Question(models.Model):
    QID = models.IntegerField(primary_key=True)
    QText = models.TextField()
    Image = models.URLField(blank= True)
    Answer = ArrayField(models.CharField(max_length=1000), size=10)
    CloseAnswer = ArrayField(models.CharField(max_length=1000), size=20)
