from django.contrib import admin
from django.urls import path, reverse
from django.template.response import TemplateResponse
from django.utils.html import format_html
from django.shortcuts import redirect
from django.contrib.auth.models import User as DjangoUser

from .models import Student, Company, User, Job
from .helpers import get_company_by_user
from .models import STATUS_PENDING
from .forms import JobForm

admin.site.site_header = 'Jober'
admin.site.site_title = 'Jober'
admin.site.site_url = 'http://jober.com/'
admin.site.index_title = 'Painel Administrativo'


class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'status', 'application_date', 'show_candidates_url', 'escolhido']
    ordering = ('status',)
    filter_horizontal = ('skills', 'candidatos')
    form = JobForm

    readonly_fields = ['show_candidates_url', ]

    def get_queryset(self, request):
        qs = super(JobAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        company = get_company_by_user(request.user)
        return qs.filter(company=company)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            company = get_company_by_user(request.user)
            obj.company = company
            obj.status = form.initial.get('status') or STATUS_PENDING
        super(JobAdmin, self).save_model(request, obj, form, change)

    def show_candidates_url(self, obj):
        if obj.id != None:
            return format_html(
                '<a class="button" href="{0}">Escolher Candidato</a>'.format(
                    reverse('admin:select_user_job', args=[obj.id]))
            )

    show_candidates_url.short_description = 'Escolher Candidato'
    show_candidates_url.allow_tags = True

    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            if obj:
                fields = super(JobAdmin, self).get_fields(request)
                return ['show_candidates_url', 'escolhido'] + fields
            else:
                fields = super(JobAdmin, self).get_fields(request)
                return  fields
        else:
            if obj:
                return 'title', 'period', 'application_date', 'response_date', 'description', 'skills', \
                       'candidatos', 'show_candidates_url'
            else:
                return 'title', 'period', 'application_date', 'response_date', 'description', 'skills'
                       

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('<int:job_id>/select-user-job/', self.select_user_job, name="select_user_job"),
        ]
        return my_urls + urls



    def select_user_job(self, request, job_id):
        job = Job.objects.get(id=job_id)
        student_list = job.candidatos.all()
        context = dict(
            self.admin_site.each_context(request),
            student_list=student_list,
        )

        if request.method == 'POST':
            escolhido_id = int(request.POST.get('escolhido'))
            escolhido = Student.objects.get(id=escolhido_id)
            job.escolhido = escolhido
            job.status = STATUS_PENDING
            job.save()

            return redirect('/admin/core/job/')

        return TemplateResponse(request, "core/templates/select_user_job.html", context)


class UserAdmin(admin.ModelAdmin):
    list_display = ['get_user_fullname', 'user', 'is_active']


admin.site.unregister(DjangoUser)
admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Company)
admin.site.register(Job, JobAdmin)
