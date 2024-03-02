from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

from core.models import World
from character.models import Character

class CharacterTestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.user2 = User.objects.create_user(username='user2', password='password2')
        self.world1 = World.objects.create(name='testWorld1', server='testServer1', datacenter='testDC1')
        self.character1 = Character.objects.create(
            name="user1Character1", 
            home_world=self.world1, 
            appartment_location="",
            estate_location="",
            user=self.user1
        )
        Character.objects.create(
            name="user2Character1", 
            home_world=self.world1, 
            appartment_location="",
            estate_location="",
            user=self.user2
        )
        Character.objects.create(
            name="user2Character2", 
            home_world=self.world1, 
            appartment_location="",
            estate_location="",
            user=self.user2
        )


    def test_create_character(self):
        self.client.force_authenticate(self.user1)
        url = reverse('character:characterList')
        data = {
            "name":"user1Character1", 
            "home_world": self.world1.pk, 
            "appartment_location":"", 
            "estate_location":""
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Character.objects.count(),4)

    def test_get_character_list(self):
        self.client.force_authenticate(self.user2)
        url = reverse('character:characterList')
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data),2)

    def test_get_character_detail(self):
        self.client.force_authenticate(self.user1)
        url = reverse('character:characterList') + str(self.character1.pk)
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "user1Character1")

    def test_update_character_detail(self):
        self.client.force_authenticate(self.user1)
        url = reverse('character:characterList') + str(self.character1.pk)
        data = {
            "name":"user1Character1", 
            "home_world": self.world1.pk, 
            "appartment_location":"testLocation", 
            "estate_location":""
        }
        response = self.client.post(url,data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        char1 = Character.objects.get(name="user1Character1")
        self.assertEqual(char1.appartment_location, "testLocation")