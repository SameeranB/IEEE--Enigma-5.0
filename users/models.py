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
    Achievements = models.DateTimeField(blank=True) # Stores the Time the user last answered
    Points = models.IntegerField(default=0)
    TimeLog = models.BooleanField(default=False, blank=True) # Stores the Hint Used Value


    def __str__(self):
        return self.email

# 3 - Bullseye
# 4 - Quick Skope