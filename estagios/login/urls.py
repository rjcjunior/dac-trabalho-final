from django.urls import path
from estagios.login.views.register import register
from estagios.login.views.login import login

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]
