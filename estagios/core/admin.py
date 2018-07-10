from django.contrib import admin

from .models import Student, Company, User, Job
from .helpers import get_company_by_user
from .models import STATUS_PENDING
from .forms import JobForm


class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'application_date']
    filter_horizontal = ('skills',)
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

    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            return super(JobAdmin, self).get_fields(request)
        else:
            return 'title', 'period', 'application_date', 'response_date', 'description', 'skills'


admin.site.register(User)
admin.site.register(Student)
admin.site.register(Company)
admin.site.register(Job, JobAdmin)
