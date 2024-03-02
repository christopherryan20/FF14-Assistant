from json import JSONDecodeError
from django.http import JsonResponse
from .serializers import WorldSerializer, BattleJobSerializer
from .models import World, BattleJob
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class WorldAPIView(views.APIView):
    """
        An api view to see a list of valid servers
    """
    permission_classes = [IsAuthenticated]
    serializer_class = WorldSerializer
    def get(self, request, format=None):
        queryset = World.objects.all()
        serializer = WorldSerializer(queryset, many=True)
        
        return Response(serializer.data,status=status.HTTP_200_OK)


class BattleJobApiView(views.APIView):
    """
        An Api view to get a list of combat jobs
    """
    permission_classes = [IsAuthenticated]
    serializer_class = BattleJobSerializer
    def get(self, request, format=None):
        queryset = BattleJob.objects.all()
        serializer = BattleJobSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
