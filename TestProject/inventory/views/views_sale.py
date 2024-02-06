from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from ..models import Product, Inventory, Sale
from decimal import Decimal
from .views_inventory import StockUpdateView
# Sale Views
class SaleListView(ListView):
    model = Sale
    template_name = 'sale/sale_list.html'
    context_object_name = 'sales'

class SaleDetailView(DetailView):
    model = Sale
    template_name = 'sale/sale_detail.html'
    context_object_name = 'sale'

class CreateSaleView(View):
    template_name = 'sale/sale_form.html'

    def get(self, request, *args, **kwargs):
        products = Inventory.objects.values('product__id', 'product__name', 'product__description', 'product__price', 'quantity')
        products_with_renamed_keys = [
            {
                'id': product['product__id'],
                'name': product['product__name'],
                'description': product['product__description'],
                'price': product['product__price'],
                'quantity': product['quantity']
            }
            for product in products
        ]
        context = {'products': products_with_renamed_keys}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product')
        quantity = Decimal(request.POST.get('quantity'))

        # Create Sale instance
        sale = Sale(
            product_id=product_id,
            quantity=quantity,
            total_price=Product.objects.get(id=product_id).price * quantity
        )

        # Call StockUpdateView webhook internally
        stock_update_view = StockUpdateView()
        stock_update_view.request = request
        response = stock_update_view.post(request, product_id=product_id, quantity_change=-quantity, reason="Sale")

        if(response.status_code>=200 and response.status_code < 300):
            sale.save()
            return redirect('/sales')
            
        return redirect('.') 


class UpdateSaleView(UpdateView):
    model = Sale
    fields = ['product', 'quantity', 'total_price', 'transaction_time']
    template_name = 'sale/sale_form.html'
    success_url = '/sales/'

class DeleteSaleView(DeleteView):
    model = Sale
    template_name = 'sale/sale_confirm_delete.html'
    success_url = '/sales/'
