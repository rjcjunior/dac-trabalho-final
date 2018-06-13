from django.urls import path
from .views.register import register
from .views.login import login

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]
