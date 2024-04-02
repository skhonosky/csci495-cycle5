from rest_framework import serializers
from core.models import footballPlayer, basketballPlayer, footballTeam, basketballTeam

class footballPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = footballPlayer
        fields = ['name', 'sport', 'team', 'position']
        read_only_fields = ['id']

class basketballPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = basketballPlayer
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