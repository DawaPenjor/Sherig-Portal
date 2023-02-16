from django.shortcuts import render, redirect
from . models import *
from . forms import *
from django.contrib import messages
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import os
from django.db.models import Sum
from .filters import StaffFilter, topperFilter

def schoolIndex(request):
    school_id = request.user.school
    #Staff stats
    total_male_adm = StaffDetail.objects.filter(School = school_id, category="Administration",gender="Male").count()
    total_female_adm = StaffDetail.objects.filter(School = school_id,category="Administration", gender="Female").count()
    total_adm = StaffDetail.objects.filter(School = school_id,category="Administration").count()

    total_male_teacher = StaffDetail.objects.filter(School = school_id,category="Teaching Staff",gender="Male").count()
    total_female_teacher = StaffDetail.objects.filter(School = school_id,category="Teaching Staff", gender="Female").count()
    total_teacher = StaffDetail.objects.filter(School = school_id,category="Teaching Staff").count()

    total_male_support = StaffDetail.objects.filter(School = school_id,category="Supporting Staff", gender="Male").count()
    total_female_support = StaffDetail.objects.filter(School = school_id,category="Supporting Staff",gender="Female").count()
    total_support = StaffDetail.objects.filter(School = school_id,category="Supporting Staff").count()

    total_male_non_teaching = StaffDetail.objects.filter(School = school_id,category="Non Teaching Staff",gender="Male").count()
    total_female_non_teaching = StaffDetail.objects.filter(School = school_id,category="Non Teaching Staff", gender="Female").count()
    total_non_teaching = StaffDetail.objects.filter(School = school_id,category="Non Teaching Staff").count()
    
    total_male_staff = StaffDetail.objects.filter(School = school_id,gender="Male").count()
    total_female_staff = StaffDetail.objects.filter(School = school_id, gender="Female").count()
    total_staff = StaffDetail.objects.filter(School = school_id).count()
   
    #Student stats
    total_standard = students.objects.filter(school = school_id).order_by('standard')
    total_male_std = students.objects.filter(school = school_id).aggregate(Sum('total_boys'))
    total_female_std = students.objects.filter(school = school_id).aggregate(Sum('total_girls'))
    total_students  = students.objects.filter(school = school_id).aggregate(Sum('total_students'))

    context = {
            "total_staff":total_staff,
            "total_male_staff":total_male_staff,
            "total_female_staff":total_female_staff,
            "total_male_adm": total_male_adm,"total_female_adm":total_female_adm,"total_adm":total_adm, 
            "total_male_teacher": total_male_teacher,"total_female_teacher":total_female_teacher,"total_teacher":total_teacher,
            "total_male_support": total_male_support,"total_female_support":total_female_support,"total_support": total_support, 
            "total_male_non_teaching": total_male_non_teaching,"total_female_non_teaching":total_female_non_teaching,"total_non_teaching":total_non_teaching,
            
            "total_standard":total_standard,
            "total_male_std":total_male_std['total_boys__sum'],
            "total_female_std":total_female_std['total_girls__sum'],
            "total_students":total_students['total_students__sum'],
    }
    return render(request, 'school/school_dashboard.html', context)

@login_required
def accounts(request, pk):
    user = Profile.objects.get(user_id=pk)
    user_pro = Profile.objects.get(user_id=pk)
    form = profileForm(instance=user)
    pform = SetPasswordForm(request.user)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if 'passwordUpdate' in request.POST:
                pform = SetPasswordForm(data=request.POST, user=request.user)
                if pform.is_valid():
                    pform.save()
                    messages.success(request, 'Password updated!')
                    request.session.flush()
                    update_session_auth_hash(request, pform.user)
                else:
                    messages.error(request,'Password Update failed!')
        if  request.method == 'POST':   
            if 'userUpdate' in request.POST:
                form = profileForm(request.POST, request.FILES, instance=user)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'User updated!')
                else:
                    messages.error(request, 'User update failed!')
                    form_user = profileForm(instance=user)
        
    context = {'user':request.user,
                'user_pro':user_pro,
                'form':form,
                'pform':pform,
                }

    return render(request, 'school/account.html', context)

@login_required
def addStaff(request):
    profile = request.user.profile
    school = request.user.school
    cat = school.category
    form = StaffRegistrationForm()

    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST, request.FILES )
        if form.is_valid():
            staff = form.save(commit=False)
            staff.Owner = profile
            staff.School = school
            staff.school_category = cat
            print(cat)
            staff.save()
            messages.success(request, 'Staff Added!')
            return redirect('staffList')
        else:
            messages.error(request, 'Staff add failed!')

    context = {'form':form,
                }
    return render(request, 'school/reg_staff.html', context)

def staffList(request):
    staff_id = request.user.school
    staff = StaffDetail.objects.filter(School_id = staff_id).order_by('category')
    total_staff = StaffDetail.objects.filter(School_id = staff_id).count()

    filterStaff = StaffFilter(request.GET, queryset=staff)
    staff = filterStaff.qs

    paginator = Paginator(staff, 10)
    page_number = request.GET.get('page')
    page_obj  = paginator.get_page(page_number)

    context = {'staff': staff,
                   'total_staff': total_staff, 
                   'page_obj':page_obj,
                   'filterStaff':filterStaff,
                }

    return render(request, 'school/staff_list.html', context)

def staff_details(request, pk):
    staff = StaffDetail.objects.get(id=pk)

    context = {'staff': staff,}
    return render(request, 'school/staff_detail.html', context)

@login_required
def updateStaff(request, staff_id):
    user = StaffDetail.objects.get(id=staff_id)
    form = StaffRegistrationForm(instance=user)
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff updated!')
            return redirect('staffList')
        else:
            messages.error(request, 'Staff update failed!')
            form = StaffRegistrationForm(instance=user)
            
    context = {'form':form,}       
    return render(request, 'school/update_staff.html', context)

@login_required
def deleteStaff(request, staff_id):
    staff = StaffDetail.objects.get(id=staff_id)
    if len(staff.profile_pic) > 0:
        os.remove(staff.profile_pic.path)
    staff.delete()
    return redirect('staffList')

@login_required
def add_staff_on_leave(request):
    profile = request.user.profile
    school = request.user.school

    form = StaffLeaveForm()

    if request.method == 'POST':
        form = StaffLeaveForm(request.POST)
        if form.is_valid():
            staff = form.save(commit=False)
            staff.owner = profile
            staff.School = school
            staff.save()
            messages.success(request, 'Staff on leave Added!')
            return redirect('staffLeaveList')
        else:
            messages.error(request, 'Staff add failed!')

    context = {'form':form,
                }
    return render(request, 'school/add_staff_leave.html', context)

def list_of_staff_on_leave(request):
    leave_id = request.user.school
    staff_on_leave = StaffOnleave.objects.filter(School_id = leave_id)
    total_staff_on_leave = StaffOnleave.objects.filter(School_id = leave_id).count()

    context = {'staff_on_leave':staff_on_leave,
                'total_staff_on_leave':total_staff_on_leave,
                }
    return render(request, 'school/staff_list_leave.html', context)

@login_required
def update_staff_leave(request, staff_id):
    user = StaffOnleave.objects.get(id=staff_id)
    form = StaffLeaveForm(instance=user)
    if request.method == 'POST':
        form = StaffLeaveForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff leave detail updated!')
            return redirect('staffLeaveList')
        else:
            messages.error(request, 'Staff leave detail update failed!')
            form = StaffLeaveForm(instance=user)
            
    context = {'form':form,}       
    return render(request, 'school/update_staff_leave.html', context)

@login_required
def deleteStaffOnLeave(request, staff_id):
    staff = StaffOnleave.objects.get(id=staff_id)
    staff.delete()
    return redirect('staffLeaveList')

@login_required
def addStudents(request):
    profile = request.user.profile
    school = request.user.school
    cat = school.category
    form = studentRegistrationForm()

    if request.method == 'POST':
        form = studentRegistrationForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.owner = profile
            student.school = school
            student.category = cat
            student.total_students = student.total_boys + student.total_girls
            student.total_boarder_students = student.total_boarder_boys + student.total_boarder_girls
            student.total_dayscholar_students = student.total_dayscholar_boys + student.total_dayscholar_girls
            student.save()
            messages.success(request, 'Students stats Added!')
            return redirect('studentStats')
        else:
            messages.error(request, 'students stats update failed!')

    context = {'form':form,
                }
    return render(request, 'school/reg_student.html', context)

def studentStats(request):
    id = request.user.school
    student = students.objects.filter(school_id = id).order_by('-standard')

    total_male_std = students.objects.filter(school_id = id).aggregate(Sum('total_boys'))
    total_female_std = students.objects.filter(school_id = id).aggregate(Sum('total_girls'))
    total_students  = students.objects.filter(school_id = id).aggregate(Sum('total_students'))

    total_boarder_boys = students.objects.filter(school_id = id).aggregate(Sum('total_boarder_boys'))
    total_boarder_girls  = students.objects.filter(school_id = id).aggregate(Sum('total_boarder_girls'))
    total_boarder_students  = students.objects.filter(school_id = id).aggregate(Sum('total_boarder_students'))

    total_dayscholar_boys = students.objects.filter(school_id = id).aggregate(Sum('total_dayscholar_boys'))
    total_dayscholar_girls  = students.objects.filter(school_id = id).aggregate(Sum('total_dayscholar_girls'))
    total_dayscholar_students  = students.objects.filter(school_id = id).aggregate(Sum('total_dayscholar_students')) 
    
    context = {
        'student': student,
        "total_male_std":total_male_std['total_boys__sum'],"total_female_std":total_female_std['total_girls__sum'],"total_students":total_students['total_students__sum'],
        "total_boarder_boys":total_boarder_boys['total_boarder_boys__sum'], "total_boarder_girls":total_boarder_girls['total_boarder_girls__sum'], "total_boarder_students":total_boarder_students['total_boarder_students__sum'],
        "total_dayscholar_boys":total_dayscholar_boys['total_dayscholar_boys__sum'],  "total_dayscholar_girls":total_dayscholar_girls['total_dayscholar_girls__sum'],"total_dayscholar_students":total_dayscholar_students['total_dayscholar_students__sum'],
    
    }

    return render(request, 'school/student_stats.html', context)

@login_required
def update_students_stats(request, std_id):
    user = students.objects.get(id=std_id)
    form = studentRegistrationForm(instance=user)
    if request.method == 'POST':
        form = studentRegistrationForm(request.POST, instance=user)
        if form.is_valid():
            user.total_students = user.total_boys + user.total_girls
            user.total_boarder_students = user.total_boarder_boys + user.total_boarder_girls
            user.total_dayscholar_students = user.total_dayscholar_boys + user.total_dayscholar_girls
            form.save()
            messages.success(request, 'student stats updated!')
            return redirect('studentStats')
        else:
            messages.error(request, 'student stats update failed!')
            form = studentRegistrationForm(instance=user)
            
    context = {'form':form,}       
    return render(request, 'school/update_std_stats.html', context)

@login_required
def deleteStdStats(request, std_id):
    student = students.objects.get(id=std_id)
    student.delete()
    return redirect('studentStats')


@login_required
def addTopper(request):
    profile = request.user.profile
    school = request.user.school
    form = topperRegistrationForm()

    if request.method == 'POST':
        form = topperRegistrationForm(request.POST)
        if form.is_valid():
            topper = form.save(commit=False)
            topper.owner = profile
            topper.school = school
            topper.save()
            messages.success(request, 'Topper Added!')
            return redirect('topperList')
        else:
            messages.error(request, 'Topper update failed!')

    context = {'form':form,}
    return render(request, 'school/reg_topper.html', context)

def topperList(request):
    school = request.user.school
    topper = TopperOfYear.objects.filter(school_id = school).order_by('-standard')

    filterTopper = topperFilter(request.GET, queryset=topper)
    topper = filterTopper.qs

    context = {'topper': topper, 
                'school':school,
                'filterTopper':filterTopper,
                 }

    return render(request, 'school/topper_list.html', context)

@login_required
def update_topper_list(request, topper_id):
    user = TopperOfYear.objects.get(id=topper_id)
    form = topperRegistrationForm(instance=user)
    if request.method == 'POST':
        form = topperRegistrationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'topper updated!')
            return redirect('topperList')
        else:
            messages.error(request, 'topper update failed!')
            form = topperRegistrationForm(instance=user)
            
    context = {'form':form,}       
    return render(request, 'school/update_topper.html', context)

@login_required
def deleteTopper(request, topper_id):
    topper = TopperOfYear.objects.get(id=topper_id)
    topper.delete()
    return redirect('topperList')

@login_required
def addTozay(request):
    profile = request.user.profile
    school = request.user.school
    form = tozayRegistrationForm()

    if request.method == 'POST':
        form = tozayRegistrationForm(request.POST)
        if form.is_valid():
            tozay = form.save(commit=False)
            tozay.owner = profile
            tozay.school = school
            tozay.save()
            messages.success(request, 'Tozay Added!')
            return redirect('tozayList')
        else:
            messages.error(request, 'Tozay update failed! Check ther errors below.')

    context = {'form':form,}
    return render(request, 'school/reg_tozay.html', context)

def tozayList(request):
    id = request.user.school
    tozay_std = Tozay.objects.filter(school_id = id).order_by('-standard')

    context = {'tozay_std': tozay_std,}

    return render(request, 'school/tozay_list.html', context)

@login_required
def update_tozay_list(request, tozay_id):
    user = Tozay.objects.get(id=tozay_id)
    form = tozayRegistrationForm(instance=user)
    if request.method == 'POST':
        form = tozayRegistrationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'tozay updated!')
            return redirect('tozayList')
        else:
            messages.error(request, 'tozay update failed!')
            form = tozayRegistrationForm(instance=user)
            
    context = {'form':form,}       
    return render(request, 'school/update_tozay.html', context)

@login_required
def deleteTozay(request, tozay_id):
    tozay_std = Tozay.objects.get(id=tozay_id)
    tozay_std.delete()
    return redirect('tozayList')


@login_required
def addCapitalActivity(request):
    owner_id = request.user.profile
    school_id = request.user.school
    form = capitalActivityForm()

    if request.method == 'POST':
        form = capitalActivityForm(request.POST)
        if form.is_valid():
            cap_activity = form.save(commit=False)
            cap_activity.owner = owner_id
            cap_activity.school = school_id
            cap_activity.save()
            messages.success(request, 'Capital Activity Added!')
            return redirect('capActivityList')
        else:
            messages.error(request, 'Capital Activity update failed! Check ther errors below.')

    context = {'form':form,}
    return render(request, 'school/add_cap_activities.html', context)

def capActivityList(request):
    cap_id = request.user.school
    cap_activity = CapitalActivites.objects.filter(school_id = cap_id)

    context = {'cap_activity': cap_activity,}

    return render(request, 'school/cap_activities.html', context)

@login_required
def update_cap_activity(request, activity_id):
    user = CapitalActivites.objects.get(id=activity_id)
    form = capitalActivityForm(instance=user)
    if request.method == 'POST':
        form = capitalActivityForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Activity updated!')
            return redirect('capActivityList')
        else:
            messages.error(request, 'Activity update failed!')
            form = capitalActivityForm(instance=user)
            
    context = {'form':form,}       
    return render(request, 'school/update_cap_activity.html', context)

@login_required
def deleteActivity(request, activity_id):
    activity = CapitalActivites.objects.get(id=activity_id)
    activity.delete()
    return redirect('capActivityList')

@login_required
def addSchoolInfrastructure(request):
    owner_id = request.user.profile
    school_id = request.user.school
    form = schoolInfrastructureForm()

    if request.method == 'POST':
        form = schoolInfrastructureForm(request.POST)
        if form.is_valid():
            items = form.save(commit=False)
            items.owner = owner_id
            items.school = school_id
            items.save()
            messages.success(request, 'Item Added!')
            return redirect('schoolInsfrastructureList')
        else:
            messages.error(request, 'Item update failed! Check ther errors below.')

    context = {'form':form,}
    return render(request, 'school/add_school_item.html', context)


def schoolInsfrastructureList(request):
    inf_id = request.user.school
    items = SchoolInfrastructure.objects.filter(school_id = inf_id)

    context = {'items': items,}

    return render(request, 'school/school_infrastructure.html', context)

@login_required
def update_school_insfrastructure(request, item_id):
    user = SchoolInfrastructure.objects.get(id=item_id)
    form = schoolInfrastructureForm(instance=user)
    if request.method == 'POST':
        form = schoolInfrastructureForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item updated!')
            return redirect('schoolInsfrastructureList')
        else:
            messages.error(request, 'Item update failed!')
            form = schoolInfrastructureForm(instance=user)
            
    context = {'form':form,}       
    return render(request, 'school/update_school_insfrastructure.html', context)

@login_required
def deleteItem(request, item_id):
    items = SchoolInfrastructure.objects.get(id=item_id)
    items.delete()
    return redirect('schoolInsfrastructureList')