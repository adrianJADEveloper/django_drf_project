from django.db import models

# Create your Book model here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallAutoField()

    def __str__(self):
        return self.title
