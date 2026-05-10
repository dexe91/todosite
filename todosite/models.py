from django.db import models
from django.utils import timezone


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    deadline = models.DateTimeField(default=timezone.now)

    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_last_update = models.DateTimeField(auto_now=True)
