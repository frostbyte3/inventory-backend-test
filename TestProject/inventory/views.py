from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Inventory, Sale

# Product Views
class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'price']
    template_name = 'product/product_form.html'
    success_url = '/products/'

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'price']
    template_name = 'product/product_form.html'
    success_url = '/products/'

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product_confirm_delete.html'
    success_url = '/products/'


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
    fields = ['product', 'quantity_change', 'reason', 'update_time']
    template_name = 'inventory/stock_update_form.html'
    success_url = '/inventory/'

# Sale Views
class SaleListView(ListView):
    model = Sale
    template_name = 'sale/sale_list.html'
    context_object_name = 'sales'

class SaleDetailView(DetailView):
    model = Sale
    template_name = 'sale/sale_detail.html'
    context_object_name = 'sale'

class CreateSaleView(CreateView):
    model = Sale
    fields = ['product', 'quantity', 'transaction_time']
    template_name = 'sale/sale_form.html'
    success_url = '/sales/'

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

class UpdateSaleView(UpdateView):
    model = Sale
    fields = ['product', 'quantity', 'total_price', 'transaction_time']
    template_name = 'sale/sale_form.html'
    success_url = '/sales/'

class DeleteSaleView(DeleteView):
    model = Sale
    template_name = 'sale/sale_confirm_delete.html'
    success_url = '/sales/'
