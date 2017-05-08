from django import forms


class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=25, label="Ім'я")
    last_name = forms.CharField(max_length=25, label='Прізвище')
    username = forms.CharField(max_length=25, required=True)
    email = forms.CharField(max_length=35, widget=forms.EmailInput)
    password = forms.CharField(max_length=36, min_length=8, widget=forms.PasswordInput)


class LogInForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(min_length=8, max_length=36, widget=forms.PasswordInput)
