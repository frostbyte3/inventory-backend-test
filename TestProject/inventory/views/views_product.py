from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ..models import Product, Inventory, Sale

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
