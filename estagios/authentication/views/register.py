from django.db.utils import IntegrityError
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User as DjangoUser
from django.forms import ValidationError

from ..forms import RegisterForm, CompanyForm, StudentForm
from estagios.core.models import Student, Company


def create_django_user(name, email, password):
    return DjangoUser.objects.create_user(email, email, password, first_name=name)


def student_create(post_data):
    form = StudentForm(post_data)
    if form.is_valid():
        email = form.data.get('email')
        name = form.data.get('name')
        password = form.data.get('password')
        newuser = create_django_user(name, email, password)

        Student.objects.create(user=newuser)


def company_create(post_data):
    form = CompanyForm(post_data)
    if form.is_valid():
        email = form.data.get('email')
        name = form.data.get('name')
        password = form.data.get('password')

        newuser = create_django_user(name, email, password)

        company_name = form.data.get('company_name')
        cnpj = form.data.get('cnpj')
        Company.objects.create(user=newuser, company_name=company_name, cnpj=cnpj)


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        register_type = request.POST.get('type')
        try:
            if register_type == 'student':
                student_create(request.POST)
            elif register_type == 'company':
                company_create(request.POST)
            form = RegisterForm()
        except IntegrityError:
            form.add_error('email', ValidationError('Usuário já existente ou inválido'))

        messages.success(request, 'Usuário registrado com sucesso!')

    return render(request, '../templates/register.html', {'form': form})
