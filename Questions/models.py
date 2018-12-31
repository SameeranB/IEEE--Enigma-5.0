from django.db import models
from djongo import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

# Create your models here.


class Achievement(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='achievements')
    Achievements = ArrayField(models.CharField(max_length=1000), size=20)


class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='progress')
    CurrentQuestion = models.IntegerField(default=1)
    CurrentAnswer = models.TextField()


class QuestionInfo(models.Model):
    QID = models.IntegerField(primary_key=True)
    QText = models.TextField()
    Image = models.URLField(blank= True)
    Answer = ArrayField(models.CharField(max_length=1000), size=10)
    CloseAnswer = ArrayField(models.CharField(max_length=1000), size=20)
    Answer_Provided = models.TextField()