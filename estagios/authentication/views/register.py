from django.db.utils import IntegrityError
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User as DjangoUser, Group
from django.forms import ValidationError

from ..forms import RegisterForm, CompanyForm, StudentForm
from estagios.core.models import Student, Company


def create_django_user(name, email, password, is_staff=False):
    return DjangoUser.objects.create_user(email, email, password, first_name=name, is_staff=is_staff)


def student_create(form):
    if form.is_valid():
        email = form.data.get('email')
        name = form.data.get('name')
        password = form.data.get('password')
        newuser = create_django_user(name, email, password)

        return Student.objects.create(user=newuser)


def company_create(form):
    if form.is_valid():
        email = form.data.get('email')
        name = form.data.get('name')
        password = form.data.get('password')

        newuser = create_django_user(name, email, password, True)
        company_group = Group.objects.get(name='Company')
        company_group.user_set.add(newuser)

        company_name = form.data.get('company_name')
        cnpj = form.data.get('cnpj')
        return Company.objects.create(user=newuser, company_name=company_name, cnpj=cnpj)


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        register_type = request.POST.get('type')
        try:
            if register_type == 'student':
                form = StudentForm(request.POST)
                student_create(form)
            elif register_type == 'company':
                form = CompanyForm(request.POST)
                company_create(form)
        except IntegrityError:
            form.add_error('email', ValidationError('Usuário já existente ou inválido'))

        messages.success(request, 'Usuário registrado com sucesso!')
        form = RegisterForm()

    return render(request, '../templates/register.html', {'form': form})
