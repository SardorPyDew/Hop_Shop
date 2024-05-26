from django.contrib import admin
from products.models import *


@admin.register(ProductManufactureModel)
class ProductManufactureAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    search_fields = ('name',)
    list_filter = ('name', 'created_at',)


@admin.register(ProductColorModel)
class ProductColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'created_at',)
    search_fields = ('name',)
    list_filter = ('name', 'created_at',)


@admin.register(ProductTagModel)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    search_fields = ('name',)
    list_filter = ('name', 'created_at',)


@admin.register(ProductSizeModel)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    search_fields = ('name',)
    list_filter = ('name', 'created_at',)


@admin.register(ProductCategoriesModel)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    search_fields = ('name',)
    list_filter = ('name', 'created_at',)


class ProductImageModelAdmin(admin.StackedInline):
    model = ProductImagesModel


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount', 'created_at',)
    search_fields = ('name', 'short_description', 'long_description')
    list_filter = ('created_at', 'updated_at',)
    inlines = [ProductImageModelAdmin]

