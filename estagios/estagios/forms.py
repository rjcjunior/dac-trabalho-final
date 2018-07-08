from django import forms
from ..core.models import Job


class JobCreateForm(forms.ModelForm):
    description = forms.CharField(required=True, max_length=1024, widget=forms.Textarea)

    class Meta:
        model = Job
        fields = ['title', 'description', 'period']
