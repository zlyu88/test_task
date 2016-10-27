from django import forms
from django.forms import ModelForm

from .models import Author


class SignUpForm(ModelForm):
    class Meta:
        model = Author
        fields = ['user_name', 'email', 'password', 'reg_date', 'picture']


class LogIn(forms.Form):
    user_name = forms.CharField(label='Your name', max_length=20)
    password = forms.CharField(max_length=32)