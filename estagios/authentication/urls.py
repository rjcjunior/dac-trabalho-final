from django.urls import path
from .views.register import register
from .views.login import login
from .views.logout import logout_view

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
]
