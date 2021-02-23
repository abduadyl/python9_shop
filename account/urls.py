from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import RegistrationView, ActivationView, SigninView, SuccessfulRegistrationView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('activation/', ActivationView.as_view(), name='activation'),
    path('login/', SigninView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('successful_registration/', SuccessfulRegistrationView.as_view(), name='successful-registration'),
]