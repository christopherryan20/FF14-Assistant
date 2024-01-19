from django.db import models
from utils.model_abstracts import Model
from django_extensions.db.models import (
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel
)
	
class World(ActivatorModel, Model):
	class Meta:
		verbose_name_plural = "Worlds"
	
	name = models.CharField(verbose_name="World Name", max_length=20)
	server = models.CharField(verbose_name="Server", max_length=20)
	datacenter = models.CharField(verbose_name="Data Center", max_length=20)

	def __str__(self):
		return f'{self.name}'

class BattleJob(ActivatorModel, Model):
	class Meta:
		verbose_name_plural = 'Battle Jobs'

	name = models.CharField(verbose_name="Job Name", max_length=20)
	baseClass = models.CharField(verbose_name="Base Class", max_length=20)
	role = models.CharField(verbose_name="Role", max_length=20)

	def __str__(self):
		return f'{self.name}'