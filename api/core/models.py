from django.db import models
from datetime import datetime

# Create your models here.

## test model airport
class Airport(models.Model):
    name = models.CharField(max_length=255)
    airport_code = models.CharField(max_length=3)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)

    def __str__(self):
        return self.name
    
class Player(models.Model):
    name=models.CharField(max_length=255)
    sport=models.CharField(max_length=255)
    team=models.CharField(max_length=255)
    position=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class footballTeam(models.Model):
    name=models.CharField(max_length=255)
    conference=models.CharField(max_length=255)
    quarterback=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=2)
    
    def __str__(self):
        return self.name

class basketballTeam(models.Model):
    name=models.CharField(max_length=255)
    conference=models.CharField(max_length=255)
    legendary_player=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=2)
    
    def __str__(self):
        return self.name
