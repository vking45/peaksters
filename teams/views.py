from django.shortcuts import render
from .models import Team
# Create your views here.

def team(request):
    teams = Team.objects.all().order_by('name')
    return render(request, 'teams.html', {'teams' : teams})

def team_detail(request, index1):
    teams = Team.objects.get(index1=index1)
    return render(request, 'team_details.html', {'teams' : teams})

def points_table(request):
    teams = Team.objects.all().order_by('-wins')
    return render(request, 'points_table.html', {'teams' : teams})