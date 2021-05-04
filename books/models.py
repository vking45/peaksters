from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bet(models.Model):
    match = models.TextField()
    datetime = models.CharField(max_length=100)
    description = models.TextField(default="Hell")
    image_URL = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    rewarded = models.BooleanField(default=False)
    teamOne = models.CharField(max_length=100)
    teamTwo = models.CharField(max_length=100)
    teamOne_count = models.IntegerField(default=0)
    teamTwo_count = models.IntegerField(default=0)
    teamOne_users = models.TextField(blank=True)
    teamTwo_users = models.TextField(blank=True)
    winner = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.match
    

class Point(models.Model):
    user_current = models.OneToOneField(User, related_name='user_current', on_delete=models.CASCADE, null=True)
    points = models.IntegerField(default=100)


    def __str__(self):
        return str(self.user_current)
    