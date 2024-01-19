from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import WorldAPIView, BattleJobApiView

app_name = 'core'

urlpatterns = [
    path('worlds/', WorldAPIView.as_view(), name='worlds'),
    path('battle-jobs/', BattleJobApiView.as_view(), name='battle-jobs'),
    path('api-token-auth/', obtain_auth_token), #gives us access to token auth
]