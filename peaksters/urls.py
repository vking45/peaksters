"""peaksters URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from books import views as books_view
from teams import views as teams_view

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^home/$', books_view.home),
    url('previous-matches/$', books_view.previous_matches),
    url('detail/(?P<slug>[\w-]+)/$', books_view.details, name="detail"),
    url('detail/previous/(?P<slug>[\w-]+)/$', books_view.details_previous, name="detail_previous"),
    url('login/$',books_view.login_view),
    url('congratulations/$', books_view.congrats),
    url('profile/$', books_view.profile),
    url('logout/$', books_view.logout_view),
    url('rewards/handout/$' , books_view.entry_rewards),
    url('rewards/handout/(?P<bet_id>\w{0,50})/$', books_view.entry_detail, name="entry_detail"),

    # Teams Views
   # url('tournaments/$', teams_view.tournament),
   # url('tournaments/(?P<index>\w{0,50})/$', teams_view.tournament_detail, name="tournament_detail"),
    url('teams/$', teams_view.team),
    url('teams/(?P<index1>\w{0,50})/$', teams_view.team_detail, name="team_detail"),
    #url('blinders/codm/pointstable/$', teams_view.points_table , name="points_table_codm"),
]
