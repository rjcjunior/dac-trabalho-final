from django.shortcuts import render, redirect
from ..forms import LoginForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib import messages


def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        django_user = authenticate(request, username=form.data.get('email'), password=form.data.get('password'))
        if django_user is not None and django_user.is_active:
            django_login(request, django_user)
            if django_user.is_staff:
                return redirect('/admin')
            else:
                return redirect('home')
        else:
            messages.error(request, 'Login Inválido!')

    return render(request, '../templates/login.html')
