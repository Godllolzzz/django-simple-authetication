from django.urls import path
from .views import *

urlpatterns = [
    path('homepage/', HomePage, name="homepage"),
    path('loginpage/', LoginPage, name="loginpage"),
    path('', SignupPage, name="signuppage"),
    path('logoutPage/', LogoutPage, name="logoutpage"),
]