from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.



class CustomUser(AbstractUser):



    CurrentQuestion = models.IntegerField(default=1)
    Answer = models.TextField()
    Achievements = ArrayField(models.CharField(max_length=1000), size=20)

    def __str__(self):
        return self.email

