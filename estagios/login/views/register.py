from django.shortcuts import render


def register(request):
    return render(request, 'login/templates/register.html')
