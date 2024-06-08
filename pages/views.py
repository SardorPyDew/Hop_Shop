from django.views.generic import TemplateView, CreateView

from pages.form import ContactModelForm
from pages.models import FeedbackModel


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['feedbacks'] = FeedbackModel.objects.all()
        return context


class ContactTemplateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm
    success_url = '/'

