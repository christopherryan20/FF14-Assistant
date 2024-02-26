from json import JSONDecodeError
from django.http import JsonResponse
from .serializers import CharacterSerializer
from .models import Character
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class CharacterListAPIView(views.APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CharacterSerializer
    def get(self, request, format=None):
        queryset = Character.objects.filter(user=request.user)
        serializer = CharacterSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = CharacterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CharacterDetailAPIView(views.APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CharacterSerializer
    def get(self, request, id, format=None):
        try:
            instance = Character.objects.get(id=id,user=request.user)
            seriaizer = CharacterSerializer(instance)
            return Response(seriaizer.data, status=status.HTTP_200_OK)
        except:
            return Response({"error":"Character not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request, id):
        try:
            instance = Character.objects.get(id=id,user=request.user)
            data = JSONParser().parse(request)
            serializer = CharacterSerializer(instance, data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error":"Character not found"}, status=status.HTTP_404_NOT_FOUND)


