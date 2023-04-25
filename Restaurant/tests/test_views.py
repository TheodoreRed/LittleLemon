from django.test import TestCase
from Restaurant.serializers import MenuSerializer
from Restaurant.models import Menu
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.item2 = Menu.objects.create(title="Nuts", price=99, inventory=129)
        self.item3 = Menu.objects.create(title="Cherries", price=250, inventory=45)
    
    def test_retrieve_all_menu_items(self):
        url = reverse('menu-list')
        response = self.client.get(url)

        queryset = Menu.objects.all()
        serialized_data = MenuSerializer(queryset, many=True)

        self.assertEqual(response.data, serialized_data.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)