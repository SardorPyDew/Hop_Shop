from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class ContactTemplateView(TemplateView):
    template_name = 'contact.html'


