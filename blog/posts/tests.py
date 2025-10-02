from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from .views import PostAPIView
from django.contrib.auth.models import User
from rest_framework import status

# Create your tests here.

# class PostTest(APITestCase):
#     def setUp(self):
#         self.factory = APIRequestFactory()
#         self.view = PostAPIView.as_view({'get': 'list'})
#         self.url = 'api/posts/'
    
#     def test_list_post(self):
#         request = self.factory.get(self.url)
#         response = self.view(request)
#         response.render()
#         self.assertEqual(response.status_code, 200)

# - APIRequestFactory() is low-level and may require you to write more lines of code because there's no abstraction to it
# - Use the built-in self.client from APITestCase which provides more abstraction

class PostTestCase(APITestCase):
    def test_list_post(self):
        url = '/posts/test/posts/' # take a keen note on the trailing hashes
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

# How DRF knows about PostAPIView
# In Django/DRF, you expose your views in urls.py.
# Your test client (self.client) doesn’t directly call the view — it calls the URL endpoint.
# Django looks up the URL in your router/URLconf, finds PostAPIView, and routes the request to it.

# class UserTestCase(APITestCase):
#     def setUp(self):
#         self.url = "/users/"
    
#     def test_create_user(self):
#         data = {'username': 'waridi', 'password': '12345'}
#         response = self.client.post(self.url, data, format='json')
#         self.assertEqual(response.status_code, 201)
    

class PostCreateTest(APITestCase):
    def setUp(self):
        self.url = '/posts/test/posts/' # urls should be configured from the project-level to app-level
        self.william = User.objects.create_user(username="william", password="12345")
    
    def test_post_create(self):
        data = {
            'title': 'Testing post', 
            'author': self.william.id, # pass the object id not the object itself
            'content': 'Hoping to learn from this'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
