from django.urls import path

from .views import candidatar, edit_student, parabens, vaga, candidatura, create_job, home

urlpatterns = [
    path('candidatar/<int:idJob>', candidatar, name='candidatar'),
    path('edit-student', edit_student, name='edit-student'),
    path('parabens', parabens, name='parabens'),
    path('vaga/<int:id>', vaga, name='vaga'),
    path('candidatura', candidatura, name='candidatura'),
    path('create-job', create_job, name='create-job'),
    path('', home, name='home'),
]
