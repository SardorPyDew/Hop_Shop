from django.urls import path

from blogs.views import BlogListView

app_name = 'blogs'

urlpatterns = [
    path('', BlogListView.as_view(), name='list')
]
