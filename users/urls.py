from django.urls import path
from users.views import *

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('account/', AccountView.as_view(), name='account'),
    path('register/', RegisterView.as_view(), name='register'),
    path('change/password/', ChangePasswordView.as_view(), name='change-password'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('verify/email/', verify_email, name='verify-email'),
    
]
