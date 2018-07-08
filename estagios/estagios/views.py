from django.shortcuts import render, redirect
from django.contrib import messages

from .helpers import get_company_jobs, get_company
from .forms import JobCreateForm
from ..core.models import Job, STATUS_PENDING


def home(request):
    if request.user.is_authenticated:
        displayname = request.user.get_full_name()
        jobs_list = None

        company = get_company(request.user)
        if company:
            displayname = company.company_name
            jobs_list = get_company_jobs(company)

        context = {
            "displayname": displayname,
            "jobs_list": jobs_list
        }
        return render(request, 'estagios/templates/home.html', context)
    else:
        return redirect('login')


def create_job(request):
    company = get_company(request.user)
    if company:
        form = JobCreateForm()
        if request.method == 'POST':
            form = JobCreateForm(request.POST)
            if form.is_valid():
                job = Job(**form.cleaned_data, company=company, status=STATUS_PENDING)
                job.save()
                messages.success(request, 'Estágio cadastrado com sucesso!')
                form = JobCreateForm()
        return render(request, 'estagios/templates/create_job.html', {'form': form})
    else:
        return redirect('login')
