from django.urls import path

from .views import home, create_job

urlpatterns = [
    path('create-job', create_job, name='create-job'),
    path('', home, name='home'),
]