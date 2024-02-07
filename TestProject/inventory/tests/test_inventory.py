from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from inventory.models import Product,Inventory,StockUpdate
from django.test import TestCase

class InventoryAPITests(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Test Product', description='Test Description', price=10.0)
        self.inventory = Inventory.objects.create(product=self.product, quantity=10)

    def test_get_inventory_list(self):
        url = reverse('inventory-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_inventory_detail(self):
        url = reverse('inventory-detail', kwargs={'pk': self.inventory.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_stock_update_success(self):
        data = {'product_id': self.product.id, 'quantity_change': -5, 'reason': 'Test Reason'}
        url = reverse('stock-update')
        response = self.client.post(url, data, format='json')
        self.assertEqual(Inventory.objects.get(product=self.product).quantity, 5)
        self.assertTrue(StockUpdate.objects.filter(product=self.product, quantity_change=-5, reason='Test Reason').exists())

    def test_stock_update_insufficient(self):
        data = {'product_id': self.product.id, 'quantity_change': -15, 'reason': 'Test Reason'}
        url = reverse('stock-update')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Not enough inventory for this transaction')

    def test_stock_update_invalid_data(self):
        data = {'quantity_change': -5, 'reason': 'Test Reason'}
        url = reverse('stock-update')  # Missing product_id
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Invalid data received from webhook')

    
    def test_stock_update_nonexistant_product(self):
        data = {'product_id': 999, 'quantity_change': -5, 'reason': 'Test Reason'}
        url = reverse('stock-update')  # Nonexistent product_id
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Specified product does not exist')
    
