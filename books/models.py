from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Match(models.Model):

    STATUS_CHOICES = (
        ("Upcoming", 'Upcoming'),
        ("Completed", 'Completed'),
        ("Rewarded", 'Rewarded'),
    )

    match = models.TextField()
    slug = models.SlugField(unique=True)
    datetime = models.DateTimeField()
    description = models.TextField(blank=True)
    image_URL = models.CharField(max_length=200)
    video_URL = models.CharField(max_length=300, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="Upcoming")
    active = models.BooleanField(default=True)
    teamOne = models.ForeignKey(to="teams.Team", on_delete=models.CASCADE, related_name="Team_One")
    teamTwo = models.ForeignKey(to="teams.Team", on_delete=models.CASCADE, related_name="Team_Two")
    
    
    def snippet(self):
        return self.description[:20]+'...'

    def __str__(self):
        return self.match
    

class BetOption(models.Model):
    match = models.OneToOneField(to="books.Match", on_delete=models.CASCADE, related_name='bet_for_match', null=True)
    bet_one = models.CharField(max_length=300)
    bet_one_option_one = models.CharField(max_length=100)
    bet_one_option_one_odds = models.FloatField(default=1.0)
    bet_one_option_two = models.CharField(max_length=100)
    bet_one_option_two_odds = models.FloatField(default=1.0)
    bet_one_winner = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.match)



class Point(models.Model):
    user_current = models.OneToOneField(User, related_name='user_current', on_delete=models.CASCADE, null=True)
    points = models.IntegerField(default=250)
    pointLog = models.TextField(blank=True)
    xp_points = models.IntegerField(default=0)
    xp_level = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
       if self.xp_points >= 1000 and self.xp_points <= 4999:
            self.xp_level = 1
            super().save(*args, **kwargs)
       elif self.xp_points >= 5000 and self.xp_points <= 9999:
            self.xp_level = 2
            super().save(*args, **kwargs)
       elif self.xp_points >= 10000:
           self.xp_level = 3
           super().save(*args, **kwargs)
       else:
            self.xp_level = 0
            super().save(*args, **kwargs)        

    def __str__(self):
        return str(self.user_current)
    
class BetEntrie(models.Model):
    concerned = models.CharField(max_length=300)
    user_entered = models.ForeignKey(User, related_name='user_entry', on_delete=models.CASCADE, null=True)
    bet_id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    amount = models.IntegerField(default=0)
    entry = models.CharField(max_length=300, blank=True)
    bet_odds = models.FloatField(default=1.0)
    betted = models.BooleanField(default=False)
    rewarded = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user_entered} + {self.concerned} + {self.rewarded}'

    
