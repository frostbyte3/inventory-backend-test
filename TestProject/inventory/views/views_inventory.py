from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from ..models import Product, Inventory, Sale, StockUpdate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Inventory Views
class InventoryListView(ListView):
    model = Inventory
    template_name = 'inventory/inventory_list.html'
    context_object_name = 'inventory'

class InventoryDetailView(DetailView):
    model = Inventory
    template_name = 'inventory/inventory_detail.html'
    context_object_name = 'inventory'

class StockUpdateView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            product_id = kwargs['product_id']
            quantity_change = kwargs['quantity_change']
            reason = kwargs['reason']
    
            # Fetch the inventory object for the given product ID
            product = Product.objects.get(id=product_id)
            inventory = Inventory.objects.get(product_id=product_id)
            
            # Update the quantity based on the quantity change
            sum = inventory.quantity + quantity_change
            if(sum < 0):
                return Response({'error': 'Not enough inventory for this transaction'}, status=status.HTTP_400_BAD_REQUEST)
            su = StockUpdate(product = product, quantity_change=quantity_change, reason = reason)
            inventory.quantity = sum
            inventory.save()
            su.save()
            
            return Response({'message': 'Stock updated successfully'}, status=status.HTTP_200_OK)
        except KeyError:
            return Response({'error': 'Invalid data received from webhook'}, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response({'error': 'Specified product does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Inventory.DoesNotExist:
            su = StockUpdate(product = product, quantity_change=quantity_change, reason = reason)
            i = Inventory(product = product, quantity=quantity_change)
            i.save()
            su.save()
            return Response({'message': 'Stock created successfully'}, status=status.HTTP_200_OK)


