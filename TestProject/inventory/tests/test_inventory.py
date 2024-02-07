from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from inventory.models import Product,Inventory
from django.test import TestCase

class InventoryAPITests(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Test Product', description='Test Description', price=10.0)

    def test_get_inventory_list(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_inventory(self):
        url = reverse('product-list')
        data = {'name': 'New Product', 'description': 'New Description', 'price': 20.0}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_inventory_detail(self):
        url = reverse('product-detail', kwargs={'pk': self.product.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
