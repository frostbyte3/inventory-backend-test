from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from inventory.models import Sale, Product, Inventory
from django.test import TestCase

class SaleAPITests(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Test Product', description='Test Description', price=10.0)
        self.sale = Sale.objects.create(product=self.product, quantity=2, total_price=20.0)
        Inventory.objects.create(product=self.product, quantity=40)
    
    def test_get_sale_list(self):
        url = reverse('sale-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_sale(self):
        url = reverse('sale-create')
        data = {'product': self.product.pk, 'quantity': 3}
        response = self.client.post(url, data)

        new_data = Sale.objects.filter(product=self.product, quantity=3)
        self.assertEqual(new_data.count(), 1)


    def test_get_sale_detail(self):
        url = reverse('sale-detail', kwargs={'pk': self.sale.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_sale(self):
        url = reverse('sale-update', kwargs={'pk': self.sale.pk})
        data = {'product':self.product.pk,'quantity': 4}
        response = self.client.post(url, data)

        self.sale.refresh_from_db()
        self.assertEqual(self.sale.quantity, 4)

    def test_delete_sale(self):
        url = reverse('sale-delete', kwargs={'pk': self.sale.pk})
        data={'product':self.product.pk ,'quantity':self.sale.quantity}
        response = self.client.post(url,data)

        new_data = Sale.objects.filter(product=self.product, quantity=2, total_price=20.0)
        self.assertFalse(new_data.exists())
