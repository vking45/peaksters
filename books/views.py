from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Match, Point, BetEntrie, BetOption
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import math

# Create your views here.

def home(request):
    teambets = Match.objects.filter(active=True).order_by('-datetime')
    return render(request, 'Index.html', {'teambets' : teambets})

def previous_matches(request):
    teambets = Match.objects.filter(active=False).order_by('-datetime')
    return render(request, 'IndexTwo.html', {'teambets' : teambets})

@login_required(login_url="/login/")
def details(request, slug):
     point = Point.objects.get(user_current=request.user)
     teambets = Match.objects.get(slug=slug)
     option = BetOption.objects.get(match=teambets.id)

     try:
        betentry = BetEntrie.objects.get(concerned=teambets.match, user_entered=request.user)
     except BetEntrie.DoesNotExist:
        betentry = BetEntrie.objects.create(concerned=teambets.match, user_entered=request.user)

     if request.method == 'POST':
        selected_option = request.POST['team']
        selected_points = int(request.POST['pointoptions'])
        if selected_option == 'One':
         betentry.amount = selected_points
         betentry.betted = True
         betentry.entry = option.bet_one_option_one
         betentry.bet_odds = option.bet_one_option_one_odds
         point.pointLog = point.pointLog + '\n'  + 'You placed a bet of ' + str(selected_points) + ' on '+ teambets.match + ' on ' + option.bet_one_option_one + '\n'
         point.points = point.points - selected_points
         betentry.save()
         point.save()
         return redirect('/congratulations/')
        elif selected_option == 'Two':
         betentry.amount = selected_points
         betentry.betted = True
         betentry.entry = option.bet_one_option_two
         betentry.bet_odds = option.bet_one_option_two_odds
         point.pointLog = point.pointLog + '\n'  + 'You placed a bet of ' + str(selected_points) + ' on '+ teambets.match + ' on ' + option.bet_one_option_two + '\n'
         point.points = point.points - selected_points
         point.save()
         betentry.save()
         return redirect('/congratulations/')
        else:
         return HttpResponse(400, 'Invalid form option')

     return render(request,'details.html',{'teambets' : teambets, 'point' : point , 'betentry' : betentry , 'option' : option})

@login_required(login_url="/login/")
def details_previous(request, slug):
     point = Point.objects.get(user_current=request.user)
     teambets = Match.objects.get(slug=slug)
     option = BetOption.objects.get(match=teambets.id)
     return render(request, 'detailsTwo.html', {'teambets' : teambets, 'point' : point , 'option' : option })
    
@receiver(post_save, sender=get_user_model())
def create_user_points(sender, instance, created, **kwargs):
    if created:
        Point.objects.create(user_current=instance)


def login_view(request):
    if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      if form.is_valid():
        # log the user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/home/')

    else:
      form = AuthenticationForm()
    return render(request,'loginpage.html', {'form':form}) 

@login_required(login_url="/login/")
def congrats(request):
    return render(request, 'congrats.html')

@login_required(login_url="/login/")
def profile(request):
    point = Point.objects.get(user_current=request.user)
    return render(request, 'profile.html', {'point' : point})

@login_required(login_url="/login/")
def logout_view(request):
    logout(request)
    return redirect('/home/')

@login_required(login_url="/login/")
def entry_rewards(request):
    betentry = BetEntrie.objects.filter(rewarded=False)
    return render(request, 'rewards.html', {'betentry' : betentry})

@login_required(login_url="/login/")
def entry_detail(request, bet_id):
    betentry = BetEntrie.objects.get(bet_id=bet_id)
    point = Point.objects.get(user_current=betentry.user_entered)
    if request.method == 'POST':
        selected_option = request.POST['option']
        if selected_option == 'One':
            winnings = math.floor(betentry.amount * betentry.bet_odds)
            point.points += winnings
            point.pointLog = point.pointLog + '\n'  + 'Your winnings for ' + betentry.concerned + ' is ' + str(winnings) + '\n'
            betentry.rewarded = True
            betentry.save()
            point.save()
            return redirect('/rewards/handout/')
        if selected_option == 'Two':
            winnings = 0
            point.pointLog = point.pointLog + '\n'  + 'Your winnings for ' + betentry.concerned + ' is ' + str(winnings) + '\n'
            betentry.rewarded = True
            betentry.save()
            point.save()
            return redirect('/rewards/handout/')
    return render(request, 'reward_detail.html', {'betentry' : betentry})