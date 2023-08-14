from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Note(models.Model):
    text = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


# class UserProfile(User):
#     pass
