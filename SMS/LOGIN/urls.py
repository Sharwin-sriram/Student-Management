from django.urls import path
from .views import *

urlpatterns = [
  path('', login_page,name="login"),
  path('register',register,name="register"),
  path('reset',reset_password,name="reset"),
]