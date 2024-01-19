from django.contrib import admin
from .models import World, BattleJob

@admin.register(World)
class WorldAdmin(admin.ModelAdmin):
    list_display = ('name', 'server', 'datacenter', 'id')

@admin.register(BattleJob)
class BattleJobAdmin(admin.ModelAdmin):
    list_display = ('name', 'baseClass', 'role', 'id')