from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from blogs.models import BlogModel, BlogCategoryModel, BlogTagModel


class BlogListView(ListView):
    template_name = 'blogs/blog-list.html'
    context_object_name = 'blogs'
    model = BlogModel
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        blogs = BlogModel.objects.all()
        context = super().get_context_data(object_list=object_list, **kwargs)
        cat = self.request.GET.get('cat')
        if cat:
            blogs = blogs.filter(categories=cat)
        context.update({
            'blogs': blogs,
            'categories': BlogCategoryModel.objects.all(),
            'tags': BlogTagModel.objects.all(),
            'famous_blogs': BlogModel.objects.all().order_by('-created_at')[:2]
        })
        return context


class BlogDetailView(DetailView):
    template_name = 'blogs/blog-detail.html'
    context_object_name = 'blog'
    model = BlogModel

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context.update({
            'blogs': BlogModel.objects.get(pk=self.kwargs['pk']),
            'categories': BlogCategoryModel.objects.all(),
            'tags': BlogTagModel.objects.all(),
            'famous_blogs': BlogModel.objects.all().order_by('-created_at')[:2]
        })
        return context




