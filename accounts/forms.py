from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    occupation = forms.CharField(max_length=30, required=False, help_text='Optional.')
    short_biography = forms.CharField(max_length=1000, required=False, help_text='Optional.')
    location = forms.CharField(max_length=300, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'occupation',
            'short_biography',
            'location',
            'email',
            'password1',
            'password2',
        )
