from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 500)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length= 200, null = True)
    price = models.FloatField()
    link = models.URLField()
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
# Create your models here.
