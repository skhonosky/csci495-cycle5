from django.shortcuts import render
from rest_framework import viewsets
from .models import footballPlayer
from .models import basketballPlayer
from .models import footballTeam
from .models import basketballTeam
from .serializers import footballPlayerSerializer
from .serializers import basketballPlayerSerializer
from .serializers import footballTeamSerializer
from .serializers import basketballTeamSerializer

# Create your views here.

class FootballPlayerViewSet(viewsets.ModelViewSet):
    queryset = footballPlayer.objects.all()
    serializer_class = footballPlayerSerializer

class BasketballPlayerViewSet(viewsets.ModelViewSet):
    queryset = basketballPlayer.objects.all()
    serializer_class = basketballPlayerSerializer

class FootballTeamViewSet(viewsets.ModelViewSet):
    queryset = footballTeam.objects.all()
    serializer_class = footballTeamSerializer

class BasketballTeamViewSet(viewsets.ModelViewSet):
    queryset = basketballTeam.objects.all()
    serializer_class = basketballTeamSerializer
