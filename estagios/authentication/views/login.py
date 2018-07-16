from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login
from django.contrib import messages

from ..forms import LoginForm
from estagios.core.models import User


def get_user(django_user):
    try:
        return User.objects.get(user=django_user)
    except:
        return None


def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        django_user = authenticate(email=form.data.get('email'), password=form.data.get('password'))
        if django_user is not None:
            user = get_user(django_user)
            if (user and user.is_active) or django_user.is_superuser:
                django_login(request, django_user)
                if django_user.is_staff:
                    return redirect('/admin')
                else:
                    return redirect('home')
            else:
                messages.error(request, 'O login não está ativo!')
        else:
            messages.error(request, 'Login Inválido!')

    return render(request, '../templates/login.html')
