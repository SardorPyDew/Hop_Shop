from django.shortcuts import render
from django.views.generic import TemplateView


class RegisterView(TemplateView):
    template_name = 'users/register.html'


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
