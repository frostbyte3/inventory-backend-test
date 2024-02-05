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
        url = reverse('product-list')
        data = {'name': 'New Product', 'description': 'New Description', 'price': 20.0}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_product_detail(self):
        url = reverse('product-detail', kwargs={'pk': self.product.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product(self):
        url = reverse('product-detail', kwargs={'pk': self.product.pk})
        data = {'name': 'Updated Product', 'description': 'Updated Description', 'price': 15.0}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Product')

    def test_delete_product(self):
        url = reverse('product-detail', kwargs={'pk': self.product.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ProductIntegrationTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Test Product', description='Test Description', price=10.0)

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