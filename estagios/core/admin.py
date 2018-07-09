from django.contrib import admin
from .models import Student, Company, User, Job

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Company)
admin.site.register(Job)
