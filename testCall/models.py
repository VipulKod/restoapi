from django.db import models

# Create your models here.
class Test(models.Model):
    data = models.CharField(max_length=100)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.data