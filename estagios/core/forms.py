from django import forms

from .models import Job


class JobForm(forms.ModelForm):
    description = forms.CharField(required=True, max_length=1024, widget=forms.Textarea, label='Descrição')

    class Meta:
        model = Job
        fields = ['title', 'period', 'application_date', 'response_date', 'description', 'skills']
