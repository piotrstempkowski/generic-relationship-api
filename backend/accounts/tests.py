from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from .factories import CustomUserFactory
from .serializers import UserSerializer


class UserViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.admin = CustomUserFactory.create()
        self.admin.is_staff = True
        self.admin.save()

        self.admin_token = Token.objects.create(user=self.admin)

        self.url = reverse("user-list")

    def test_get_users_with_data_as_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.admin_token}")
        users_with_data = CustomUserFactory.create_batch(10)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = UserSerializer(User.objects.all(), many=True)
        self.assertEqual(response.data, serializer.data)

    def test_get_user_without_data_as_admin(self):
        self.client.force_authenticate(self.admin)
        users_with_out_data = CustomUserFactory.create_batch(10, no_blogs=True,
                                                             no_comments=True,
                                                             no_replies=True,
                                                             no_likes=True)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = UserSerializer(User.objects.all(), many=True)
        self.assertEqual(response.data, serializer.data)
