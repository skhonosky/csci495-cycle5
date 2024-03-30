from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlayerViewSet
from .views import FootballTeamViewSet
from .views import BasketballTeamViewSet

router = DefaultRouter()
router.register(r'player', PlayerViewSet)
router.register(r'footballteam', FootballTeamViewSet)
router.register(r'basketballteam', BasketballTeamViewSet)

urlpatterns = [
    path('', include(router.urls)),
]