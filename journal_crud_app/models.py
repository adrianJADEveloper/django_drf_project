from django.db import models
from django.utils import timezone

# Create your Journal model here.


class Journal(models.Model):

    title = models.CharField(max_length=255, blank=False, unique=True)
    author = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    # for Grateful_for question
    q_one = models.CharField(max_length=1000, default=None)
    # for Actions_toward question
    q_two = models.CharField(max_length=1000, default=None)
    # for Tomorrow_plan question
    q_three = models.CharField(max_length=1000, default=None)

    def __str__(self):
        return self.title
