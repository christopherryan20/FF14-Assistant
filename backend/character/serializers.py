from . import models
from rest_framework import serializers

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Character
        fields = ('id', 'name', 'home_world', 'appartment_location', 'estate_location')