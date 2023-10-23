from django.db import models

# Create your models here.

class Listing(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    num_bedroom = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.title