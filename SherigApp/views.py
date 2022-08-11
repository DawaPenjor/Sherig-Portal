from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from . forms import registerSchoolForm, RegisterUserForm, LoginUserForm, updateUserForm
from django.contrib.auth import authenticate, login, logout 
from . models import CustomUser, School
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def contactUs(request):
    return render(request, 'contact_us.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admIndex')
        else:
            messages.error(request, 'Username or Password Incorrect!')           
    return render(request, 'LoginPage.html')

def logoutUser(request):
    logout(request)
    return redirect('index')

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