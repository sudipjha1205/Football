"""ProTwo URL Configuration

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
from django.conf.urls import include
from django.urls import path
from AppTwo import views

urlpatterns = [
    path('',views.index,name='second_app'),
    path('messi/',views.goat,name="GOAT"),
    path('templates/',views.templates,name="templates"),
    path('espanyol/',views.intro,name="espanyol"),
    path('api/top5/players/attack/',views.top5leagueattacker,name="Top 5 League attacker"),
    path('api/top5/players/defense/',views.top5leaguedefender,name="Top 5 League defender"),
    path('api/top5/players/goalie/',views.top5leaguegoalie,name="Top 5 League Goal-Keeper"),
    path('api/bundesliga/players/attack/',views.bundesligaattack,name="Attackers Bundesliga"),
    path('api/bundesliga/players/defense/',views.bundesligadefense,name="Defenders Bundesliga"),
    path('api/bundesliga/players/goalie/',views.bundesligagoalie,name="Goalie Bundesliga"),
    path('api/bundesliga/players/goalie/adv/',views.bundesligagoalieadv,name="Goalie advance Bundesliga"),
    path('api/bundesliga/teams/attack/',views.bundeligateamattack,name="Bundesliga Team Attack"),
    path('api/bundesliga/teams/defense/',views.bundeligateamdefense,name="Bundesliga Team Defense"),
    path('api/bundesliga/teams/goalie/',views.bundeligateamgoalie,name="Bundesliga Team Goalie"),
    path('admin/', admin.site.urls),
]
