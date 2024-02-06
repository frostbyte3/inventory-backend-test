from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ..models import Product, Inventory, Sale

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
