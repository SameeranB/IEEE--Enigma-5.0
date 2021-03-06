from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.



class CustomUser(AbstractUser):

    email = models.EmailField(unique=True)
    University = models.CharField(max_length=100)
    CurrentQuestion = models.IntegerField(default=1)
    Answer = models.TextField()
    Achievements = ArrayField(models.IntegerField(default=1), size=200)
    Points = models.IntegerField(default=0)
    TimeLog = ArrayField(models.DurationField())
    AttemptLog = ArrayField(models.IntegerField(default=0))

    def __str__(self):
        return self.email

# 3 - Bullseye
# 4 - Quick Skope