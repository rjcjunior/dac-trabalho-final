from django.shortcuts import render, redirect
from django.contrib import messages

from ..core.helpers import get_available_jobs, get_students_by_user, get_company_by_user, get_company_jobs, \
    get_job_by_id
from .forms import JobCreateForm, StudentEditForm
from ..core.models import Job, STATUS_PENDING


def home(request):
    if request.user.is_authenticated:
        displayname = request.user.get_full_name()
        jobs_list = get_available_jobs()
        isCompany = False
        student = get_students_by_user(request.user)
        company = get_company_by_user(request.user)
        skills = []
        if company:
            displayname = company.company_name
            jobs_list = get_company_jobs(company)
            isCompany = True
            description = company.description
        elif student:
            description = student.description
            skills = student.skills.all()
            aux = []
            for i in jobs_list.all():
                if not (student in i.candidatos.all()):
                    aux.append(i)
            jobs_list = aux

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


def edit_student(request):
    student = get_students_by_user(request.user)
    if student:
        form = StudentEditForm(request.POST or None, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'estagios/templates/edit_student.html', {'form': form})
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


# TODO Colocar um notice avisando que a candidatura foi um sucesso
def candidatar(request, idJob):
    if request.user.is_authenticated:
        student = get_students_by_user(request.user)
        job = get_job_by_id(idJob)
        if not job.skills.all:  # Se lista de skills do job for vazia
            job.candidatos.add(student)
            job.save()
            return redirect('home')
        else:
            confirm = True
            for i in job.skills.all():
                if not (i in student.skills.all()):
                    confirm = False
            if confirm:
                job.candidatos.add(student)
                job.save()
                messages.success('Candidatura feita com sucesso!')
                return redirect('home')
            else:
                return redirect('/vaga/' + str(idJob))
    else:
        return redirect('/vaga/' + str(idJob))


def vaga(request, id):
    if request.user.is_authenticated:
        job = get_job_by_id(id)
        context = {
            "job": job[0]
        }
        return render(request, 'estagios/templates/vaga.html', context)
    else:
        return redirect('login')


def parabens(request):
    if request.user.is_authenticated:
        return render(request, 'estagios/templates/parabens.html')
    else:
        return redirect('login')
