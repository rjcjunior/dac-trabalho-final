from django.shortcuts import render, redirect
from ..core.models import Company


def getCompany(user):
    try:
        company = Company.objects.get(user=user)
        if company:
            return company
    except:
        return False


def home(request):
    if request.user.is_authenticated:
        displayname = request.user.get_full_name()

        company = getCompany(request.user)
        if company:
            displayname = company.company_name

        context = {
            "displayname": displayname
        }
        return render(request, 'estagios/templates/home.html', context)
    else:
        return redirect('login')
