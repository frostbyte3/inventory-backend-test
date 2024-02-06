from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ..models import Product, Inventory, Sale


# Inventory Views
class InventoryListView(ListView):
    model = Inventory
    template_name = 'inventory/inventory_list.html'
    context_object_name = 'inventory'

class InventoryDetailView(DetailView):
    model = Inventory
    template_name = 'inventory/inventory_detail.html'
    context_object_name = 'inventory'

class StockUpdateView(CreateView):
    model = Inventory
    fields = ['product', 'quantity']
    template_name = 'inventory/stock_update_form.html'
    success_url = '/inventory/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context
