from django.shortcuts import render
from rest_framework import status
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .models import Top5LeagueAttack,Top5LeagueDefense,Top5LeagueGoalie
from .serializers import *
import requests
import json

from .models import BundesligaAttackers,BundesligaDefenders,BundesligaGoalie,BundesligaGoalieAdv,BundesligaTeamAttack,BundesligaTeamDefense,BundesligaTeamKeeper

# Create your views here.
def index(request):
    return HttpResponse("<em>My Second App</em>")

def intro(request):
    return HttpResponse("Hola!! Yo soy Sudip :) ")

def templates(request):
    my_dict = {"name":"Sudip Kumar Jha"}
    return render(request,'Apptwo/index.html',context=my_dict)

def goat(request):
    my_dict = {"name":"Lionel Messi","pos":"Greatest Of All Time"}
    return render(request,'Apptwo/messi.html',context=my_dict)


@api_view(['GET'])
def top5leagueattacker(request):
    if request.method == 'GET':
        data = Top5LeagueAttack.objects.all().order_by('-ga')
        serializer = Top5leagueattackSerializer(data, context={'request':request},many=True)

        return Response(serializer.data)
    else:
        pass


@api_view(['GET'])
def top5leaguedefender(request):
    if request.method == 'GET':
        data = Top5LeagueDefense.objects.all().order_by('-intplustkl')
        serializer = Top5leaguedefenseSerializer(data, context={'request':request},many=True)

        return Response(serializer.data)
    else:
        pass


@api_view(['GET'])
def top5leaguegoalie(request):
    if request.method == 'GET':
        data = Top5LeagueGoalie.objects.all().order_by('-cs')
        serializer = Top5leaguegoalieSerializer(data, context={'request':request},many=True)

        return Response(serializer.data)
    else:
        pass


@api_view(['GET'])
def bundesligaattack(request):
    if request.method == 'GET':
        data = BundesligaAttackers.objects.all().order_by('-ga')
        serializer = BundesligaAttackersSerializer(data, context={'request':request},many=True)

        return Response(serializer.data)
    else:
        pass


@api_view(['GET'])
def bundesligadefense(request):
    if request.method == 'GET':
        data = BundesligaDefenders.objects.all().order_by('-intplustkl')
        serializer = BundesligaDefendersSerializer(data, context={'request':request},many=True)

        return Response(serializer.data)
    else:
        pass


@api_view(['GET'])
def bundesligagoalie(request):
    if request.method == 'GET':
        data = BundesligaGoalie.objects.all().order_by('-cs')
        serializer = BundesligaGoalieSerializer(data, context={'request':request},many=True)

        return Response(serializer.data)
    else:
        pass


@api_view(['GET'])
def bundesligagoalieadv(request):
    if request.method == 'GET':
        data = BundesligaGoalieAdv.objects.all().order_by('ga')
        serializer = BundesligaGoalieAdvSerializer(data, context={'request':request},many=True)

        return Response(serializer.data)
    else:
        pass


@api_view(['GET'])
def bundeligateamattack(request):
    if request.method == 'GET':
        data = BundesligaTeamAttack.objects.all().order_by('ga')
        serializer = BundesligaTeamAttackSerializer(data, context={'request':request},many=True)

        return Response(serializer.data)
    else:
        pass


@api_view(['GET'])
def bundeligateamdefense(request):
    if request.method == 'GET':
        data = BundesligaTeamDefense.objects.all().order_by('tklint')
        serializer = BundesligaTeamDefenseSerializer(data, context={'request':request},many=True)

        return Response(serializer.data)
    else:
        pass

@api_view(['GET'])
def bundeligateamgoalie(request):
    if request.method == 'GET':
        data = BundesligaTeamKeeper.objects.all().order_by('cs')
        serializer = BundesligaTeamKeeperSerializer(data, context={'request':request},many=True)

        return Response(serializer.data)
    else:
        pass

