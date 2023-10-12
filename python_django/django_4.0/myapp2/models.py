from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length= 1000)
    event_date = models.DateTimeField()
    venue = models.CharField(max_length= 1000)

    def __str__(self):
        return self.name


