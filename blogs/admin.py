from django.contrib import admin

from blogs.models import AuthorModel, BlogCategoryModel, BlogModel


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    search_fields = ('name',)
    list_filter = ('name', 'created_at',)


@admin.register(BlogCategoryModel)
class BlogCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    search_fields = ('name',)
    list_filter = ('name', 'created_at',)


@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at',)
    search_fields = ('title', 'content',)
    list_filter = ('created_at',)





