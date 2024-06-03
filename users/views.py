import random

from django.core.checks import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from conf import settings
from users.forms import RegisterForm
from users.models import VerificationCodeModel


def send_email_verifivcation(user):
    random_code = random.randint(100000, 999999)

    if VerificationCodeModel.objects.filter(code=random_code).exists():
        send_email_verifivcation(user)
    else:
        VerificationCodeModel.objects.create(
            code=random_code,
            user=user
        )
        try:
            send_mail(
                'Verification code',
                f'Verification code for {random_code}',
                settings.EMAIL_HOST_USER,
                [user]
            )
            return True
        except Exception as e:
            print(e)
            return False


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('users:verify-email')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        send_email_verifivcation(user)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        print(self.get_context_data(form=form))
        return self.render_to_response(self.get_context_data(form=form))


def verify_email(request):
    return render(request, 'users/verify-email.html')


class LoginView(TemplateView):
    template_name = 'users/login.html'


class WishlistView(TemplateView):
    template_name = 'users/wishlist.html'


class CartView(TemplateView):
    template_name = 'users/cart.html'


class ChangePasswordView(TemplateView):
    template_name = 'users/reset-password.html'


class AccountView(TemplateView):
    template_name = 'users/account.html'


class CheckoutView(TemplateView):
    template_name = 'products/checkout.html'
