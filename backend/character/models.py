from django.db import models
from utils.model_abstracts import Model
from django_extensions.db.models import (
	ActivatorModel
)
from django.contrib.auth.models import User

from core.models import World

class Character(ActivatorModel, Model):
    class Meta:
        verbose_name_plural = "Characters"
	
    name = models.CharField(verbose_name="Character Name", max_length=25)
    home_world = models.ForeignKey(World, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appartment_location = models.CharField(max_length=30, blank=True)
    estate_location = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.name}'