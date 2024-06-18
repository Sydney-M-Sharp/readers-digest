from django.db import models
from django.contrib.auth.models import User


class BookReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books_created")
    book = models.ForeignKey()
    rating = models.IntegerField(max_length=10)
    comment = models.CharField()
    date_posted = models.DateField()
    