from django.db import models

from django.db import models
from django.contrib.auth.models import User
class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='songs/')
    

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    watch_later = models.ManyToManyField(Song)

    def __str__(self):
        return self.user.username + ' Profile'