from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from inventory.models import Sale, Product
from django.test import TestCase

class SaleAPITests(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Test Product', description='Test Description', price=10.0)
        self.sale = Sale.objects.create(product=self.product, quantity=2, total_price=20.0)

    def test_get_sale_list(self):
        url = reverse('sale-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_sale(self):
        url = reverse('sale-list')
        data = {'product': self.product.pk, 'quantity': 3, 'total_price': 30.0}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_sale_detail(self):
        url = reverse('sale-detail', kwargs={'pk': self.sale.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_sale(self):
        url = reverse('sale-detail', kwargs={'pk': self.sale.pk})
        data = {'quantity': 4, 'total_price': 40.0}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['quantity'], 4)

    def test_delete_sale(self):
        url = reverse('sale-detail', kwargs={'pk': self.sale.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class SaleIntegrationTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Test Product', description='Test Description', price=10.0)
        self.sale = Sale.objects.create(product=self.product, quantity=2, total_price=20.0)

    def test_sale_creation(self):
        initial_count = Sale.objects.count()
        data = {'product': self.product.pk, 'quantity': 3, 'total_price': 30.0}
        response = self.client.post(reverse('sale-list'), data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Sale.objects.count(), initial_count + 1)

    def test_sale_detail_view(self):
        url = reverse('sale-detail', kwargs={'pk': self.sale.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.sale.product.name)

    def test_sale_update(self):
        data = {'quantity': 4, 'total_price': 40.0}
        response = self.client.patch(reverse('sale-detail', kwargs={'pk': self.sale.pk}), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['quantity'], 4)

    def test_sale_deletion(self):
        initial_count = Sale.objects.count()
        response = self.client.delete(reverse('sale-detail', kwargs={'pk': self.sale.pk}))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Sale.objects.count(), initial_count - 1)