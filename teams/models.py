from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=300)
    index1 = models.IntegerField(primary_key=True, unique=True, default=0)
    logo_URL = models.CharField(max_length=400)
    description = models.TextField(blank=True)
    members = models.TextField(blank=True)
    matches_played = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
  #  team_matches = models.ManyToManyField(to="books.Match", blank=True)

    def __str__(self):
        return self.name

    def snippet(self):
        return self.description[:20]+'...'