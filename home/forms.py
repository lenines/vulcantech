from django import forms

class LoginForm(forms.Form):
    login_username = forms.CharField(max_length=100)
    login_password = forms.CharField(label='Password')