from . import models
from rest_framework import serializers

class WorldSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.World
		fields = ('id', 'name', 'server', 'datacenter')

class BattleJobSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.BattleJob
		fields = ('id', 'name', 'baseClass', 'role')