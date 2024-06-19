from django.db import models
from django.contrib.auth.models import User


class BookReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books_reviewed")
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name='book_reviews')
    rating = models.IntegerField()
    comment = models.CharField(max_length=255)
    date_posted = models.DateField()
    