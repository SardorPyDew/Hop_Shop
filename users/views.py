import datetime
import random
import pytz

from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView

from conf import settings
from users.forms import RegisterForm, EmailVerificationForm, LoginForm
from users.models import VerificationCodeModel

UserModel = get_user_model()


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
        storage = messages.get_messages(self.request)
        storage.used = True
        messages.error(self.request, form.errors)
        print(self.get_context_data(form=form))
        return self.render_to_response(self.get_context_data(form=form))


def verify_email(request):
    if request.method == 'POST':
        form = EmailVerificationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            user_code = VerificationCodeModel.objects.filter(code=code).first()
            if user_code:
                now = datetime.now(pytz.timezone(settings.TIME_ZONE))
                sent_time = user_code.created_at.astimezone(pytz.timezone(settings.TIME_ZONE)) + datetime.timedelta(minutes=2)
                if sent_time > now:
                    UserModel.objects.filter(pk=user_code.user.pk).update(is_active=True)
                    return redirect(reverse_lazy('user:login'))
                else:
                    messages.error(request, 'Verification code expired.')

            else:
                messages.error(request, 'This code is invalid')


        else:
            messages.error(request, form.errors)
    return render(request, 'users/verify-email.html')


class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('pages:home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(self.success_url)
        else:
            messages.error(self.request, 'Invalid username or password')

    def form_invalid(self, form):
        storage = messages.get_messages(self.request)
        storage.used = True
        messages.error(self.request, 'Form is invalid')
        return self.render_to_response(self.get_context_data(form=form))


def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('pages:home')


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
