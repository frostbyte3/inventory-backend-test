from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from inventory.models import Product
from django.test import TestCase

class ProductAPITests(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Test Product', description='Test Description', price=10.0)

    def test_get_product_list(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        url = reverse('product-create')
        data = {'name': 'New Product', 'description': 'New Description', 'price': 20.0}
        response = self.client.post(url, data)

        new_data = Product.objects.get(name='New Product', description='New Description', price=20.0)
        self.assertNotEqual(new_data, Product.objects.none())

    def test_get_product_detail(self):
        url = reverse('product-detail', kwargs={'pk': self.product.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product(self):
        url = reverse('product-update', kwargs={'pk': self.product.pk})
        data = {'name': 'Updated Product', 'description': 'Updated Description', 'price': 15.0}
        response = self.client.post(url, data)
        
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Updated Product')

    def test_delete_product(self):
        url = reverse('product-delete', kwargs={'pk': self.product.pk})
        response = self.client.delete(url)

        new_data = Product.objects.filter(name='Test Product', description='Test Description', price=10.0)
        self.assertEqual(new_data.exists(), False)
        
