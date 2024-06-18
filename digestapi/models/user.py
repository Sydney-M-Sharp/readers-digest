from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.CharField()
    