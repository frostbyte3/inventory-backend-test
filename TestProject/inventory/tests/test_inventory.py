from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from inventory.models import Product,Inventory
from django.test import TestCase

class InventoryAPITests(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Test Product', description='Test Description', price=10.0)

    def test_get_product_list(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        url = reverse('product-list')
        data = {'name': 'New Product', 'description': 'New Description', 'price': 20.0}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_product_detail(self):
        url = reverse('product-detail', kwargs={'pk': self.product.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class InventoryIntegrationTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Test Product', description='Test Description', price=10.0)
        self.stock_update = Inventory.objects.create(product=self.product, quantity=5)

    def test_product_detail_view(self):
        url = reverse('product-detail', kwargs={'pk': self.product.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)

    def test_product_creation(self):
        initial_count = Product.objects.count()
        data = {'name': 'New Product', 'description': 'New Description', 'price': 20.0}
        response = self.client.post(reverse('product-list'), data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Product.objects.count(), initial_count + 1)

    def test_stock_update_creation(self):
        initial_quantity = self.stock_update.quantity
        data = {'product': self.product.pk, 'quantity': 10}
        response = self.client.post(reverse('stock-update-list'), data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.stock_update.quantity, initial_quantity + 10)
