from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from django.test import TestCase, tag

@tag('no_db')
class PostAPITestCase(APITestCase):
    def setUp(self):
        # Set up test data
        print("Set up initated!")

    def test_getAuthentication(self):
        # Test POST request to create a new Post
        post_data = {'email': 'abc@gmail.com', 'password': 'abcd@123'}
        response = self.client.post('/api/authenticate', post_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json().get("token")
        self.assertEqual(len(data.split(".")), 3)