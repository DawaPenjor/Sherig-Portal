from dataclasses import field
from pyexpat import model
from django import forms
from django.db import models
from .models import *
from django.contrib.auth.forms import UserCreationForm,SetPasswordForm


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (  'username',
                    'email',
                    'school',
                    'password1', 
                    'password2', 
                    'is_superuser',
                    'is_dzongkhag', 
                    'is_school' )


class updateUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'school','is_superuser','is_dzongkhag', 'is_school')

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

class APAForm(forms.ModelForm):
    class Meta:
        model = APA
        fields = ('APA_file',)
    
class FYPForm(forms.ModelForm):
    class Meta:
        model = FYP
        fields = ('FYP_file',)

class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user',]

class StaffRegistrationForm(forms.ModelForm):
    class Meta:
        model = StaffDetail
        fields = [
            'Employee_ID', 'name', 'gender', 'date_of_birth', 'CID',
            'category', 'position_title', 'position_level', 'grade', 'appointment_date',
            'joining_date_of_present_school', 'transfered_from', 'Employment_type',
            'nationality', 'subject', 'qualification', 'contact_number', 'email',
            'permanent_address','profile_pic',
        ]
        exclude = ['Owner','School']
        widgets = {
            'Employee_ID': forms.NumberInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Enter Employee Id'}),
            'name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter full name'
                       }),
            'gender': forms.Select(
                attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}),
            'CID': forms.NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter CID number'
                       }),
            'category': forms.Select(
                attrs={'class': 'form-control'}),
            'position_title': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter Position Title'
                       }),
            'position_level': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter position level'}),
            'grade': forms.NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter grade in number'}),
            'appointment_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date',
                       'placeholder': 'Pick appointment date'
                       }),
            'joining_date_of_present_school': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date',
                       'placeholder': 'When did he/she joined to this school?'
                       }),
            'transfered_from': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Previous school'
                       }),
            'Employment_type': forms.Select(
                attrs={'class': 'form-control'}),
            'nationality': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter nationality'
                       }),
            'subject': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter subject/Role of the support staff'
                       }),
            'qualification': forms.Textarea(
                attrs={'rows': 3, 'cols': 80, 'class': 'form-control',
                       'placeholder': 'Enter all qualification'
                       }),
            'contact_number': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter 8 digit mobile number'
                       }),
            'email': forms.EmailInput(
                attrs={'class': 'form-control',
                       'placeholder': '.....@education.gov.bt'
                       }),
            'permanent_address': forms.Textarea(
                attrs={'rows': 3, 'cols': 80, 'class': 'form-control',
                       'placeholder': 'Enter permanent address: village, Gewog, Dzongkhag'
                       }),
            'profile_pic': forms.FileInput(
                attrs={'class': 'form-control'})
        }
    def clean_CID(self):
        cid = self.cleaned_data.get('CID')
        if len(cid) != 11:
            raise forms.ValidationError(
                "CID number should be UNIQUE 11 digits.")
        return cid

    def clean_contact_number(self):
        phone = self.cleaned_data.get('contact_number')
        if len(phone) != 8:
            raise forms.ValidationError("Mobile number should have 8 digits.")
        return phone

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if "@education.gov.bt" not in email:
            raise forms.ValidationError(
                "We accept only education mail address.")
        return email
    
class StaffLeaveForm(forms.ModelForm):
    #def __init__(self, user, *args, **kwargs):
    #    super(StaffLeaveForm, self).__init__(*args, **kwargs)
    #    self.fields['name'].queryset = StaffDetail.objects.filter(Owner=user)

    class Meta:
        model = StaffOnleave
        exclude = ['owner','School',]

        widgets = {
            'Start_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}),
            'End_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}),
            'office_order': forms.Textarea(
                attrs={'rows': 2, 'cols': 80, 'class': 'form-control',
                       'placeholder': 'Approval office order Ref. No & date'
                       }),
            'remark': forms.Textarea(
                attrs={'rows': 2, 'cols': 80, 'class': 'form-control',
                       }),
        }
        
class studentRegistrationForm(forms.ModelForm):
    class Meta:
        model = students
        exclude = ['owner','school', 'category','total_students', 'total_boarder_students', 'total_dayscholar_students',]

class topperRegistrationForm(forms.ModelForm):
    class Meta:
        model = TopperOfYear
        exclude = ['owner','school',]
    
class tozayRegistrationForm(forms.ModelForm):
    class Meta:
        model = Tozay
        exclude = ['owner','school',]

        widgets = {
            'DoB': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}),
            'reason': forms.Textarea(
                attrs={'rows': 2, 'cols': 80, 'class': 'form-control',
                       }),
        }
    def clean_CID(self):
        cid = self.cleaned_data.get('CID')
        if len(cid) != 11:
            raise forms.ValidationError(
                "CID number should be UNIQUE 11 digits.")
        return cid

    def clean_father_CID(self):
        cid = self.cleaned_data.get('father_CID')
        if len(cid) != 11:
            raise forms.ValidationError(
                "CID number should be UNIQUE 11 digits.")
        return cid
        
    def clean_mother_CID(self):
        cid = self.cleaned_data.get('mother_CID')
        if len(cid) != 11:
            raise forms.ValidationError(
                "CID number should be UNIQUE 11 digits.")
        return cid
    
class capitalActivityForm(forms.ModelForm):
    class Meta:
        model = CapitalActivites
        exclude = ['owner','school',]

        widgets = {
            'start_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}),
            'remark': forms.Textarea(
                attrs={'rows': 2, 'cols': 80, 'class': 'form-control',
                       }),
        }
class schoolInfrastructureForm(forms.ModelForm):
    class Meta:
        model = SchoolInfrastructure
        exclude = ['owner','school',]
        