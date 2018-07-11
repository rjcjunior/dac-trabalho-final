from django.urls import path

from .views import *

urlpatterns = [
    path('editStudent', editStudent, name='editStudent'),
    path('parabens', parabens, name='parabens'),
    path('vaga', vaga, name='vaga'),
    path('candidatura', candidatura, name='candidatura'),
    path('create-job', create_job, name='create-job'),
    path('', home, name='home'),
]