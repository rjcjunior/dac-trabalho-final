from django.contrib import admin
from django.urls import path, reverse
from django.template.response import TemplateResponse
from django.utils.html import format_html

from .models import Student, Company, User, Job
from .helpers import get_company_by_user
from .models import STATUS_PENDING
from .forms import JobForm


class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'status', 'application_date', 'show_candidates_url']
    ordering = ('status',)
    filter_horizontal = ('skills', 'candidatos')
    form = JobForm

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
        return format_html(
            '<a class="button" href="{0}">Escolher Candidato</a>'.format(
                reverse('admin:select_user_job', args=[obj.id]))
        )

    show_candidates_url.short_description = 'Escolher Candidato'
    show_candidates_url.allow_tags = True

    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            return super(JobAdmin, self).get_fields(request)
        else:
            return 'title', 'period', 'status', 'application_date', 'response_date', 'description', 'skills', \
                   'candidatos', 'show_candidates_url'

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
        return TemplateResponse(request, "core/templates/select_user_job.html", context)


admin.site.register(User)
admin.site.register(Student)
admin.site.register(Company)
admin.site.register(Job, JobAdmin)
