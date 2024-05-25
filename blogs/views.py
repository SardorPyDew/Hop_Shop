from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from blogs.models import BlogModel


class BlogListView(ListView):
    template_name = 'blogs/blog-list.html'
    context_object_name = 'blogs'
    model = BlogModel


