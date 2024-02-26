from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import CharacterListAPIView, CharacterDetailAPIView

app_name = 'character'

urlpatterns = [
    path('', CharacterListAPIView.as_view(), name='characterList'),
    path('<str:id>', CharacterDetailAPIView.as_view(), name='characterDetail'),
]