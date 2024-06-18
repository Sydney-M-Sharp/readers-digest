from django.db import models
from django.contrib.auth.models import User

class BookCategory(models.Model):
    book = models.ForeignKey()
    category = models.ForeignKey()
    date_posted = models.DateField()