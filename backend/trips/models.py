from django.db import models
from django.contrib.auth.models import User 

class Trip(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return self.title

class Destination(models.Model):
    trip = models.ForeignKey(Trip, related_name='destinations', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Note(models.Model):
    destination = models.ForeignKey(Destination, related_name='notes', on_delete=models.CASCADE)
    content = models.TextField()
    is_important = models.BooleanField(default=False)

    def __str__(self):
        return f"Note for {self.destination.name}"