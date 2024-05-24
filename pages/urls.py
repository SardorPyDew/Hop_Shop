
from django.urls import path

from pages.views import HomePageView, ContactTemplateView

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactTemplateView.as_view(), name='contact'),
]