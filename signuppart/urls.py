from django.urls import path
from .views import *

urlpatterns = [
    path("home/", webPage, name='main_page'),
    path("signup/", signUpFunc, name="sign_up")
]