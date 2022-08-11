from django import forms
from django.db import models
from .models import CustomUser, School
from django.contrib.auth.forms import UserCreationForm


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (  'username',
                    'email',
                    'school',
                    'password1', 
                    'password2', 
                    'is_dzongkhag', 
                    'is_school' )

class updateUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'school','is_dzongkhag', 'is_school')

class LoginUserForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )

class registerSchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'

