from django.db import models
from datetime import datetime

# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=200)
    price = models.IntegerField()
    vegetarian = models.BooleanField(default=True)
    typeOfFood = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name