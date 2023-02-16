import profile
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from . forms import registerSchoolForm, RegisterUserForm, LoginUserForm, updateUserForm, APAForm, FYPForm, profileForm
from django.contrib.auth import authenticate, login, logout 
from . models import CustomUser, School, APA, FYP, Profile, StaffDetail, StaffOnleave, students
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import update_session_auth_hash
import os
from django.db.models import Sum

def home(request):
    total_HSS = School.objects.filter(category="HSS").count()
    total_MSS = School.objects.filter(category="MSS").count()
    total_LSS = School.objects.filter(category="LSS").count()
    total_PS = School.objects.filter(category="PS").count()
    muenseling = School.objects.filter(category="Muenseling").count()
    total_school = School.objects.exclude(category="DZO").count()
    
    total_male_staff = StaffDetail.objects.filter(gender="Male").count()
    total_female_staff = StaffDetail.objects.filter(gender="Female").count()
    total_adm = StaffDetail.objects.filter(category="Administration").count()
    total_teacher = StaffDetail.objects.filter(category="Teaching Staff").count()
    total_support_staff = StaffDetail.objects.filter(category="Supporting Staff").count()
    total_non_teaching = StaffDetail.objects.filter(category="Non Teaching Staff").count()
    total_staff = StaffDetail.objects.count()

    total_male_std = students.objects.aggregate(Sum('total_boys'))
    total_female_std  = students.objects.aggregate(Sum('total_girls'))
    total_boarder_boys = students.objects.aggregate(Sum('total_boarder_boys'))
    total_boarder_girls  = students.objects.aggregate(Sum('total_boarder_girls'))
    total_dayscholar_boys = students.objects.aggregate(Sum('total_dayscholar_boys'))
    total_dayscholar_girls  = students.objects.aggregate(Sum('total_dayscholar_girls'))
    total_students  = students.objects.aggregate(Sum('total_students'))
    
    context = { 
        "total_HSS": total_HSS,"total_MSS" : total_MSS,"total_LSS": total_LSS,"total_PS": total_PS,"muenseling": muenseling,"total_school": total_school,
        "total_male_staff": total_male_staff,"total_female_staff":total_female_staff, "total_adm":total_adm, "total_teacher":total_teacher,
        "total_support_staff": total_support_staff, "total_non_teaching":total_non_teaching,"total_staff":total_staff,
        "total_male_std":total_male_std['total_boys__sum'],  "total_female_std":total_female_std['total_girls__sum'],      
        "total_boarder_boys":total_boarder_boys['total_boarder_boys__sum'], "total_boarder_girls":total_boarder_girls['total_boarder_girls__sum'],
        "total_dayscholar_boys":total_dayscholar_boys['total_dayscholar_boys__sum'],  "total_dayscholar_girls":total_dayscholar_girls['total_dayscholar_girls__sum'],
        "total_students":total_students['total_students__sum'], 
                }
    return render(request, 'home.html', context)

def contactUs(request):
    return render(request, 'contact_us.html')

def principalContact(request):
    detail = StaffDetail.objects.filter(category="Administration")
    paginator = Paginator(detail, 25)
    page_number = request.GET.get('page')
    page_obj  = paginator.get_page(page_number)
    context = {
        "page_obj":page_obj,
    }
    return render(request, "principal-contact.html", context)

def about(request):
    return render(request, 'about.html')

@login_required
def profiles(request, pk):
    pro = Profile.objects.get(user_id=pk)
    form = SetPasswordForm(request.user)
    form_user = profileForm(instance=pro)

    if request.user.is_authenticated:
        if request.method == 'POST':
            if 'passwordUpdate' in request.POST:
                form = SetPasswordForm(data=request.POST, user=request.user)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Password updated!')
                    request.session.flush()
                    update_session_auth_hash(request, form.user)
                else:
                    messages.error(request,'Password Update failed!')
            
            elif 'userUpdate' in request.POST:
                form_user = profileForm(request.POST, request.FILES, instance=pro)
                if form_user.is_valid():
                    form_user.save()
                    messages.success(request, 'User updated!')
                else:
                    messages.error(request, 'User update failed!')
                    form_user = profileForm(instance=pro)
    
        context = {
            'form':form, 
            'form_user':form_user,
            'pro':pro,
             }
        return render(request, 'administrator/profile.html', context )

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admIndex')
        elif user is not None and user.is_school:
            login(request, user)
            return redirect('schoolIndex')  
        else:
            messages.error(request, 'Username or Password Incorrect!')           
    return render(request, 'LoginPage.html')

def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required
def registerSchool(request):
    if request.method == 'POST':
        form = registerSchoolForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            messages.success(request, 'School Added Successfully!')
            form = registerSchoolForm()
        else:
            messages.error(request, 'School Update Failed!')
    else:
        form = registerSchoolForm()
    context = {'form':form,}
    return render(request, 'administrator/add_school.html', context)

@login_required
def admIndex(request):
    user = CustomUser.objects.all()
    apa_file = APA.objects.all()
    fyp_file = FYP.objects.all()
    tot_user = CustomUser.objects.all()
    paginator = Paginator(user, 5)
    page_number = request.GET.get('userpage')
    page_obj  = paginator.get_page(page_number)

    school = School.objects.all()
    paginator = Paginator(school, 5)
    page_number = request.GET.get('schoolpage')
    page_obj_school  = paginator.get_page(page_number)

    context = {
        'user':request.user,
        'tot_user':tot_user,
        'page_obj':page_obj,
        'school':school,
        'page_obj_school': page_obj_school,
        'apa_file':apa_file,
        'fyp_file':fyp_file,
         }
    return render(request, 'administrator/dashboard.html', context)

@login_required
def registerUser(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.save()
            messages.success(request, 'User Added!')
            form = RegisterUserForm()
        else:
            messages.error(request, 'User Update Failed!')
    else:
        form = RegisterUserForm()
    context = {'form':form,}
    return render(request, 'administrator/reg_user.html', context)

@login_required
def updateUser(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    form = updateUserForm(instance=user)
    if request.method == 'POST':
        form = updateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated!')
            return redirect('admIndex')
        else:
            messages.error(request, 'User update failed!')
            form = updateUserForm(instance=user)
    context = {'form':form,}       
    return render(request, 'administrator/update_user.html', context)

@login_required
def deleteUser(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    user.delete()
    return redirect('admIndex')

@login_required       
def updateSchool(request, school_id):
    school = School.objects.get(id=school_id)
    form = registerSchoolForm(instance=school)
    if request.method == 'POST':
        form = registerSchoolForm(request.POST, instance=school)
        if form.is_valid():
            form.save()
            messages.success(request, 'School updated!')
            return redirect('admIndex')
        else:
            messages.error(request, 'School update failed!')
            form = registerSchoolForm(instance=school)
    context = {'form':form,}       
    return render(request, 'administrator/add_school.html', context)

@login_required
def deleteSchool(request, school_id):
    school = School.objects.get(id=school_id)
    school.delete()
    return redirect('admIndex')

@login_required
def uploadAPA(request):
    if request.method == 'POST':
        form = APAForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.save()
            messages.success(request, 'File Uploaded!')
        else:
            messages.error(request, 'Upload Failed!')
    else:
        form = APAForm()
    context = {'form':form}
    return render(request, 'administrator/uploadAPA.html', context)

def viewAPA(request):
    file = APA.objects.all()
    context = {'file':file,}
    return render(request, 'APA.html', context)

@login_required
def deleteAPAFile(request, pk):
    file = APA.objects.get(id=pk)
    if len(file.APA_file) > 0:
        os.remove(file.APA_file.path)
    file.delete()
    messages.success(request, 'File deleted!')
    return redirect('admIndex')

@login_required
def uploadFYP(request):
    if request.method == 'POST':
        form = FYPForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.save()
            messages.success(request, 'File Uploaded!')
        else:
            messages.error(request, 'Upload Failed!')
    else:
        form = FYPForm()
    context = {'form':form}
    return render(request, 'administrator/uploadFYP.html', context)

def viewFYP(request):
    file = FYP.objects.all()
    context = {'file':file,}
    return render(request, 'FYP.html', context)

@login_required
def deleteFYPFile(request, pk):
    file = FYP.objects.get(id=pk)
    if len(file.FYP_file) > 0:
        os.remove(file.FYP_file.path)
    file.delete()
    messages.success(request, 'File deleted!')
    return redirect('admIndex')
