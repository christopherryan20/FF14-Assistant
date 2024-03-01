from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from core.models import World, BattleJob

class WorldTestCase(APITestCase):
    def setUp(self):
        World.objects.create(name='testWorld1', server='testServer1', datacenter='testDC1')
        World.objects.create(name='testWorld2', server='testServer2', datacenter='testDC2')
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.token1 = Token.objects.create(user=self.user1)

        self.headers = {
            "Authorization": "Token " + self.token1.key
        }

    def test_worlds_added_to_db(self):
        """2 Worlds in DB and world names are correct"""
        world_count = World.objects.count()
        world1 = World.objects.get(datacenter='testDC1')
        world2 = World.objects.get(datacenter='testDC2')
        self.assertEqual(world_count, 2)
        self.assertEqual(str(world1), 'testWorld1')
        self.assertEqual(str(world2), 'testWorld2')

    def test_get_worlds(self):
        """Get all worlds from API"""
        url = reverse('core:worlds')
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(url, format='json', **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class BattleJobTestCase(APITestCase):
    def setUp(self):
        BattleJob.objects.create(name='testJob1', baseClass='testClass1', role='testRole1')
        BattleJob.objects.create(name='testJob2', baseClass='testClass2', role='testRole2')
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.token1 = Token.objects.create(user=self.user1)

        self.headers = {
            "Authorization": "Token " + self.token1.key
        }

    def test_jobs_added_to_db(self):
        """2 Jobs in DB and job names are correct"""
        job_count = BattleJob.objects.count()
        job1 = BattleJob.objects.get(baseClass='testClass1')
        job2 = BattleJob.objects.get(baseClass='testClass2')
        self.assertEqual(job_count, 2)
        self.assertEqual(str(job1), 'testJob1')
        self.assertEqual(str(job2), 'testJob2')

    def test_get_jobs(self):
        """Get all jobs from API"""
        url = reverse('core:battle-jobs')
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(url, format='json', **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)