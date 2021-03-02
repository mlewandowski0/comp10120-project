from django.db import models
from django.contrib.auth.models import User 

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
class Playlist(models.Model):
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField()
    genre = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    description = models.CharField(max_length=256)
    rating = models.IntegerField()
    isPublic = models.BooleanField()

class Item(models.Model):
    whichPlaylist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    author = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
