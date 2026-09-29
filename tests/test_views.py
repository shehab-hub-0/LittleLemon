from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass12345')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pasta", price=12, inventory=50)
        Menu.objects.create(title="Greek salad", price=9, inventory=30)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/items/')
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)