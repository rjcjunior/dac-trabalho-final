from django.shortcuts import render, redirect
from django.contrib import messages

from .core.helpers import get_company_jobs_avaliables, get_students_by_user, get_company_by_user, get_company_jobs
from .forms import JobCreateForm, StudentEditForm
from .core.models import Job, STATUS_PENDING


def home(request):
    if request.user.is_authenticated:
        displayname = request.user.get_full_name()
        jobs_list = get_company_jobs_avaliables()
        isCompany = False
        student = get_students_by_user(request.user)
        company = get_company_by_user(request.user)
        skills = []
        description = ''
        if company:
            displayname = company.company_name
            jobs_list = get_company_jobs(company)
            isCompany = True
            description = company.description
        elif student:
            description = student.description
            skills = student.skills.all()
        context = {
            "displayname": displayname,
            "jobs_list": jobs_list,
            "isCompany": isCompany,
            "description": description,
            "skills": skills
        }
        return render(request, 'estagios/templates/home.html', context)
    else:
        return redirect('login')


def editStudent(request):
    student = get_students_by_user(request.user)
    if student:
        form = StudentEditForm(request.POST or None, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'estagios/templates/editStudent.html', {'form': form})
    else:
        return redirect('login')


def create_job(request):
    company = get_company_by_user(request.user)
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


def candidatura(request):
    if request.user.is_authenticated:
        return render(request, 'estagios/templates/candidatura.html')
    else:
        return redirect('login')


def vaga(request):
    if request.user.is_authenticated:
        return render(request, 'estagios/templates/vaga.html')
    else:
        return redirect('login')


def parabens(request):
    if request.user.is_authenticated:
        return render(request, 'estagios/templates/parabens.html')
    else:
        return redirect('login')
