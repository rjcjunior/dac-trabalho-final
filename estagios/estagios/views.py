from django.shortcuts import render, redirect


def home(request):
    if request.user.is_authenticated:
        return render(request, 'estagios/templates/home.html')
    else:
        return redirect('login')
