from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class BookCategory(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='book_categories')
    category = models.ForeignKey('Category', on_delete=models.CASCADE,  related_name='book_categories')
    date = models.DateField(default=timezone.now)