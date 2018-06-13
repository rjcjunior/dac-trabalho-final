from django.db.utils import IntegrityError
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User as DjangoUser
from django.forms import ValidationError

from ..forms.register_form import RegisterForm
from estagios.core.models import Student


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                email = form.data.get('email')
                name = form.data.get('name')
                password = form.data.get('password')
                newuser = DjangoUser.objects.create_user(email, email, password, first_name=name)
                Student.objects.create(user=newuser)
                messages.success(request, 'Usuário registrado com sucesso!')
                form = RegisterForm()
            except IntegrityError as e:
                form.add_error('email', ValidationError('Usuário já existente ou inválido'))

    else:
        form = RegisterForm()
    return render(request, '../templates/register.html', {'form': form})
