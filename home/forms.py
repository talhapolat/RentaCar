from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=40)
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

