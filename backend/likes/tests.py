from rest_framework.test import APITestCase, APIClient


class LikeViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
