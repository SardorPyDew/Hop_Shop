from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from products.models import ProductModel


class ProductListView(ListView):
    template_name = 'products/product-list.html'
    model = ProductModel
    context_object_name = 'products'
