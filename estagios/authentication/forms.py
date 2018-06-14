from django import forms

accountTypes = (
    ('student', 'Estudante'),
    ('company', 'Empresa'),
)


class RegisterForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    type = forms.ChoiceField(choices=accountTypes)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if not password or not confirm_password or password != confirm_password:
            error = forms.ValidationError('As senhas precisam ser iguais!')
            self.add_error('password', error)
            self.add_error('confirm_password', error)
        return cleaned_data


class StudentForm(RegisterForm):
    pass


class CompanyForm(RegisterForm):
    pass