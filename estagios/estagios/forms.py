from django import forms
from ..core.models import Job, Student
from django.forms import widgets


class JobCreateForm(forms.ModelForm):
    description = forms.CharField(required=True, max_length=1024, widget=forms.Textarea, label='Descrição')
    application_date = forms.DateField(required=True, widget=widgets.SelectDateWidget, label='Prazo de Inscrição')
    response_date = forms.DateField(required=True, widget=widgets.SelectDateWidget, label='Data de Resposta')

    class Meta:
        model = Job
        fields = ['title', 'description', 'period']


class StudentEditForm(forms.ModelForm):
    description = forms.CharField(required=True, max_length=1024, widget=forms.Textarea, label='Descrição')

    class Meta:
        model = Student
        fields = ('description', 'skills')
