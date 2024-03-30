from rest_framework import serializers
from core.models import Player, footballTeam, basketballTeam

class playerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['name', 'sport', 'team', 'position']
        read_only_fields = ['id']

class footballTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = footballTeam
        fields = ['name', 'conference', 'quarterback', 'city', 'state']
        read_only_fields = ['id']

class basketballTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = basketballTeam
        fields = ['name', 'conference', 'legendary_player', 'city', 'state']
        read_only_fields = ['id']