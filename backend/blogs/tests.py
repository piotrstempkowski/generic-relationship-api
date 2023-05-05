from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from accounts.factories import CustomUserFactory
from .factories import BlogFactory


class BlogViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = CustomUserFactory.create(no_blogs=True,
                                              no_comments=True,
                                              no_replies=True,
                                              no_likes=True)
        self.admin.is_staff = True
        self.admin.save()
        self.blogs = BlogFactory.create_batch(10)

        self.admin_token = Token.objects.create(user=self.admin)

        self.url = reverse("blog-list")

    def test_get_blogs_list_as_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.admin_token}")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(f"response data {response.data}")

