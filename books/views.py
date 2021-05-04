from django.shortcuts import render
from .models import Bet, Point
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# Create your views here.

def home(request):
    teambets = Bet.objects.filter(active=True)
    return render(request, 'Index.html', {'teambets' : teambets})

def previous_matches(request):
    teambets = Bet.objects.filter(active=False)
    return render(request, 'IndexTwo.html', {'teambets' : teambets})

@login_required(login_url="/login/")
def details(request, match):
     point = Point.objects.get(user_current=request.user)
     teambets = Bet.objects.get(match=match)
     if request.method == 'POST':
        selected_option = request.POST['team']
        if selected_option == 'One':
         teambets.teamOne_count = teambets.teamOne_count + 1
         teambets.teamOne_users = teambets.teamOne_users + str(point.user_current) + ', '
         point.points = point.points-100
         point.save()
         teambets.save()
         return redirect('/congratulations/')
        elif selected_option == 'Two':
         teambets.teamTwo_count = teambets.teamTwo_count + 1 
         teambets.teamTwo_users = teambets.teamTwo_users + str(point.user_current) + ', '
         point.points = point.points-100
         point.save()
         teambets.save()
         return redirect('/congratulations/')
        else:
         return HttpResponse(400, 'Invalid form option')

        teambets.save()

     return render(request,'details.html',{'teambets' : teambets, 'point' : point })

@login_required(login_url="/login/")
def details_previous(request, match):
     point = Point.objects.get(user_current=request.user)
     teambets = Bet.objects.get(match=match)
     return render(request, 'detailsTwo.html', {'teambets' : teambets, 'point' : point })
    
@receiver(post_save, sender=get_user_model())
def create_user_cart(sender, instance, created, **kwargs):
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