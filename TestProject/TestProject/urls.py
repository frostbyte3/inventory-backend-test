"""
URL configuration for TestProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from inventory.views import (
    # Product Views
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    # Inventory Views
    InventoryListView,
    InventoryDetailView,
    StockUpdateView,
    # Sale Views
    SaleListView,
    SaleDetailView,
    CreateSaleView,
    UpdateSaleView,
    DeleteSaleView,
)

urlpatterns = [
    # Product URLs
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/new/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),

    # Inventory URLs
    path('inventory/', InventoryListView.as_view(), name='inventory-list'),
    path('inventory/<int:pk>/', InventoryDetailView.as_view(), name='inventory-detail'),
    path('inventory/stock-update/', StockUpdateView.as_view(), name='stock-update'),

    # Sale URLs
    path('sales/', SaleListView.as_view(), name='sale-list'),
    path('sales/<int:pk>/', SaleDetailView.as_view(), name='sale-detail'),
    path('sales/new/', CreateSaleView.as_view(), name='sale-create'),
    path('sales/<int:pk>/update/', UpdateSaleView.as_view(), name='sale-update'),
    path('sales/<int:pk>/delete/', DeleteSaleView.as_view(), name='sale-delete'),
]
