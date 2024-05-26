from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from products.models import ProductModel, ProductCategoriesModel


class ProductListView(ListView):
    template_name = 'products/product-list.html'
    model = ProductModel
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategoriesModel.objects.all()
        return context


class ProductDetailView(DetailView):
    template_name = 'products/product-detail.html'
    model = ProductModel
    context_object_name = 'product'
