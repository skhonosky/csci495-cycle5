from django.shortcuts import render
from rest_framework import viewsets
from .models import Player
from .models import footballTeam
from .models import basketballTeam
from .serializers import playerSerializer
from .serializers import footballTeamSerializer
from .serializers import basketballTeamSerializer

# Create your views here.

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = playerSerializer

class FootballTeamViewSet(viewsets.ModelViewSet):
    queryset = footballTeam.objects.all()
    serializer_class = footballTeamSerializer

class BasketballTeamViewSet(viewsets.ModelViewSet):
    queryset = basketballTeam.objects.all()
    serializer_class = basketballTeamSerializer
