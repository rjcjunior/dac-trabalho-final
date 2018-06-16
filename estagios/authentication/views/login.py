from django.shortcuts import render, redirect
from ..forms import LoginForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib import messages


def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        user = authenticate(request, username=form.data.get('email'), password=form.data.get('password'))
        if user is not None:
            django_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Login Inválido!')

    return render(request, '../templates/login.html')
