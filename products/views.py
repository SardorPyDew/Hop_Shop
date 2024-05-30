from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from products.models import ProductModel, ProductCategoriesModel, ProductManufactureModel, ProductTagModel, \
    ProductColorModel


class ProductListView(ListView):
    template_name = 'products/product-list.html'
    model = ProductModel
    context_object_name = 'products'

    @staticmethod
    def chang_colors_structure():
        colors = ProductColorModel.objects.all()
        colors_list = []
        temp_colors = []
        for color in colors:
            if len(temp_colors) == 2:
                colors_list.append(temp_colors)
                temp_colors.clear()
            else:
                temp_colors.append(color)
        colors_list.append(temp_colors)
        return colors_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategoriesModel.objects.all()
        context['manufactures'] = ProductManufactureModel.objects.all()
        context['tags'] = ProductTagModel.objects.all()
        context['colors'] = ProductColorModel.objects.all()
        context['products'] = ProductModel.objects.all()
        return context


class ProductDetailView(DetailView):
    template_name = 'products/product-detail.html'
    model = ProductModel
    context_object_name = 'product'
