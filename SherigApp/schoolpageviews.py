import profile
from django.shortcuts import render
from . models import School,StaffDetail,students
from django.db.models import Sum

def hss_home(request):
    hss = School.objects.filter(category="HSS")
    
    #students stats
    total_male_std = students.objects.filter(category="HSS").aggregate(Sum('total_boys'))
    total_female_std = students.objects.filter(category="HSS").aggregate(Sum('total_girls'))
    total_students  = students.objects.filter(category="HSS").aggregate(Sum('total_students'))

    total_boarder_boys = students.objects.filter(category="HSS").aggregate(Sum('total_boarder_boys'))
    total_boarder_girls  = students.objects.filter(category="HSS").aggregate(Sum('total_boarder_girls'))
    total_boarder_students  = students.objects.filter(category="HSS").aggregate(Sum('total_boarder_students'))

    total_dayscholar_boys = students.objects.filter(category="HSS").aggregate(Sum('total_dayscholar_boys'))
    total_dayscholar_girls  = students.objects.filter(category="HSS").aggregate(Sum('total_dayscholar_girls'))
    total_dayscholar_students  = students.objects.filter(category="HSS").aggregate(Sum('total_dayscholar_students'))

    #Staff stats
    total_male_staff = StaffDetail.objects.filter(school_category="HSS",gender="Male").count()
    total_female_staff = StaffDetail.objects.filter(school_category="HSS", gender="Female").count()
    total_staff = StaffDetail.objects.filter(school_category="HSS").count()

    total_male_adm = StaffDetail.objects.filter(school_category="HSS",category="Administration",gender="Male").count()
    total_female_adm = StaffDetail.objects.filter(school_category="HSS",category="Administration", gender="Female").count()
    total_adm = StaffDetail.objects.filter(school_category="HSS",category="Administration").count()

    total_male_teacher = StaffDetail.objects.filter(school_category="HSS",category="Teaching Staff",gender="Male").count()
    total_female_teacher = StaffDetail.objects.filter(school_category="HSS",category="Teaching Staff", gender="Female").count()
    total_teacher = StaffDetail.objects.filter(school_category="HSS",category="Teaching Staff").count()

    total_male_support = StaffDetail.objects.filter(school_category="HSS",category="Supporting Staff", gender="Male").count()
    total_female_support = StaffDetail.objects.filter(school_category="HSS",category="Supporting Staff",gender="Female").count()
    total_support = StaffDetail.objects.filter(school_category="HSS",category="Supporting Staff").count()

    total_male_non_teaching = StaffDetail.objects.filter(school_category="HSS",category="Non Teaching Staff",gender="Male").count()
    total_female_non_teaching = StaffDetail.objects.filter(school_category="HSS",category="Non Teaching Staff", gender="Female").count()
    total_non_teaching = StaffDetail.objects.filter(school_category="HSS",category="Non Teaching Staff").count()
    
    context = {
        "hss":hss,
        "total_male_std":total_male_std['total_boys__sum'],"total_female_std":total_female_std['total_girls__sum'],"total_students":total_students['total_students__sum'],
        "total_boarder_boys":total_boarder_boys['total_boarder_boys__sum'], "total_boarder_girls":total_boarder_girls['total_boarder_girls__sum'], "total_boarder_students":total_boarder_students['total_boarder_students__sum'],
        "total_dayscholar_boys":total_dayscholar_boys['total_dayscholar_boys__sum'],  "total_dayscholar_girls":total_dayscholar_girls['total_dayscholar_girls__sum'],"total_dayscholar_students":total_dayscholar_students['total_dayscholar_students__sum'],

        "total_male_staff": total_male_staff,"total_female_staff":total_female_staff, "total_staff":total_staff,
        "total_male_adm": total_male_adm,"total_female_adm":total_female_adm,"total_adm":total_adm, 
        "total_male_teacher": total_male_teacher,"total_female_teacher":total_female_teacher,"total_teacher":total_teacher,
        "total_male_support": total_male_support,"total_female_support":total_female_support,"total_support": total_support, 
        "total_male_non_teaching": total_male_non_teaching,"total_female_non_teaching":total_female_non_teaching,"total_non_teaching":total_non_teaching,
        
    }
    return render(request, "hss.html", context)

def mss_home(request):
    mss = School.objects.filter(category="MSS")
    #students stats
    total_male_std = students.objects.filter(category="MSS").aggregate(Sum('total_boys'))
    total_female_std = students.objects.filter(category="MSS").aggregate(Sum('total_girls'))
    total_students  = students.objects.filter(category="MSS").aggregate(Sum('total_students'))

    total_boarder_boys = students.objects.filter(category="MSS").aggregate(Sum('total_boarder_boys'))
    total_boarder_girls  = students.objects.filter(category="MSS").aggregate(Sum('total_boarder_girls'))
    total_boarder_students  = students.objects.filter(category="MSS").aggregate(Sum('total_boarder_students'))

    total_dayscholar_boys = students.objects.filter(category="MSS").aggregate(Sum('total_dayscholar_boys'))
    total_dayscholar_girls  = students.objects.filter(category="MSS").aggregate(Sum('total_dayscholar_girls'))
    total_dayscholar_students  = students.objects.filter(category="MSS").aggregate(Sum('total_dayscholar_students'))

    #Staff stats
    total_male_staff = StaffDetail.objects.filter(school_category="MSS",gender="Male").count()
    total_female_staff = StaffDetail.objects.filter(school_category="MSS", gender="Female").count()
    total_staff = StaffDetail.objects.filter(school_category="MSS").count()

    total_male_adm = StaffDetail.objects.filter(school_category="MSS",category="Administration",gender="Male").count()
    total_female_adm = StaffDetail.objects.filter(school_category="MSS",category="Administration", gender="Female").count()
    total_adm = StaffDetail.objects.filter(school_category="MSS",category="Administration").count()

    total_male_teacher = StaffDetail.objects.filter(school_category="MSS",category="Teaching Staff",gender="Male").count()
    total_female_teacher = StaffDetail.objects.filter(school_category="MSS",category="Teaching Staff", gender="Female").count()
    total_teacher = StaffDetail.objects.filter(school_category="MSS",category="Teaching Staff").count()

    total_male_support = StaffDetail.objects.filter(school_category="MSS",category="Supporting Staff", gender="Male").count()
    total_female_support = StaffDetail.objects.filter(school_category="MSS",category="Supporting Staff",gender="Female").count()
    total_support = StaffDetail.objects.filter(school_category="MSS",category="Supporting Staff").count()

    total_male_non_teaching = StaffDetail.objects.filter(school_category="MSS",category="Non Teaching Staff",gender="Male").count()
    total_female_non_teaching = StaffDetail.objects.filter(school_category="MSS",category="Non Teaching Staff", gender="Female").count()
    total_non_teaching = StaffDetail.objects.filter(school_category="MSS",category="Non Teaching Staff").count()
    
    context = {
        "mss":mss,
        "total_male_std":total_male_std['total_boys__sum'],"total_female_std":total_female_std['total_girls__sum'],"total_students":total_students['total_students__sum'],
        "total_boarder_boys":total_boarder_boys['total_boarder_boys__sum'], "total_boarder_girls":total_boarder_girls['total_boarder_girls__sum'], "total_boarder_students":total_boarder_students['total_boarder_students__sum'],
        "total_dayscholar_boys":total_dayscholar_boys['total_dayscholar_boys__sum'],  "total_dayscholar_girls":total_dayscholar_girls['total_dayscholar_girls__sum'],"total_dayscholar_students":total_dayscholar_students['total_dayscholar_students__sum'],

        "total_male_staff": total_male_staff,"total_female_staff":total_female_staff, "total_staff":total_staff,
        "total_male_adm": total_male_adm,"total_female_adm":total_female_adm,"total_adm":total_adm, 
        "total_male_teacher": total_male_teacher,"total_female_teacher":total_female_teacher,"total_teacher":total_teacher,
        "total_male_support": total_male_support,"total_female_support":total_female_support,"total_support": total_support, 
        "total_male_non_teaching": total_male_non_teaching,"total_female_non_teaching":total_female_non_teaching,"total_non_teaching":total_non_teaching,
        
    }
    return render(request, "mss.html", context)

def lss_home(request):
    lss = School.objects.filter(category="LSS")
    #students stats
    total_male_std = students.objects.filter(category="LSS").aggregate(Sum('total_boys'))
    total_female_std = students.objects.filter(category="LSS").aggregate(Sum('total_girls'))
    total_students  = students.objects.filter(category="LSS").aggregate(Sum('total_students'))

    total_boarder_boys = students.objects.filter(category="LSS").aggregate(Sum('total_boarder_boys'))
    total_boarder_girls  = students.objects.filter(category="LSS").aggregate(Sum('total_boarder_girls'))
    total_boarder_students  = students.objects.filter(category="LSS").aggregate(Sum('total_boarder_students'))

    total_dayscholar_boys = students.objects.filter(category="LSS").aggregate(Sum('total_dayscholar_boys'))
    total_dayscholar_girls  = students.objects.filter(category="LSS").aggregate(Sum('total_dayscholar_girls'))
    total_dayscholar_students  = students.objects.filter(category="LSS").aggregate(Sum('total_dayscholar_students'))

    #Staff stats
    total_male_staff = StaffDetail.objects.filter(school_category="LSS",gender="Male").count()
    total_female_staff = StaffDetail.objects.filter(school_category="LSS", gender="Female").count()
    total_staff = StaffDetail.objects.filter(school_category="LSS").count()

    total_male_adm = StaffDetail.objects.filter(school_category="LSS",category="Administration",gender="Male").count()
    total_female_adm = StaffDetail.objects.filter(school_category="LSS",category="Administration", gender="Female").count()
    total_adm = StaffDetail.objects.filter(school_category="LSS",category="Administration").count()

    total_male_teacher = StaffDetail.objects.filter(school_category="LSS",category="Teaching Staff",gender="Male").count()
    total_female_teacher = StaffDetail.objects.filter(school_category="LSS",category="Teaching Staff", gender="Female").count()
    total_teacher = StaffDetail.objects.filter(school_category="LSS",category="Teaching Staff").count()

    total_male_support = StaffDetail.objects.filter(school_category="LSS",category="Supporting Staff", gender="Male").count()
    total_female_support = StaffDetail.objects.filter(school_category="LSS",category="Supporting Staff",gender="Female").count()
    total_support = StaffDetail.objects.filter(school_category="LSS",category="Supporting Staff").count()

    total_male_non_teaching = StaffDetail.objects.filter(school_category="LSS",category="Non Teaching Staff",gender="Male").count()
    total_female_non_teaching = StaffDetail.objects.filter(school_category="LSS",category="Non Teaching Staff", gender="Female").count()
    total_non_teaching = StaffDetail.objects.filter(school_category="LSS",category="Non Teaching Staff").count()
    
    context = {
        "lss": lss,
        "total_male_std":total_male_std['total_boys__sum'],"total_female_std":total_female_std['total_girls__sum'],"total_students":total_students['total_students__sum'],
        "total_boarder_boys":total_boarder_boys['total_boarder_boys__sum'], "total_boarder_girls":total_boarder_girls['total_boarder_girls__sum'], "total_boarder_students":total_boarder_students['total_boarder_students__sum'],
        "total_dayscholar_boys":total_dayscholar_boys['total_dayscholar_boys__sum'],  "total_dayscholar_girls":total_dayscholar_girls['total_dayscholar_girls__sum'],"total_dayscholar_students":total_dayscholar_students['total_dayscholar_students__sum'],

        "total_male_staff": total_male_staff,"total_female_staff":total_female_staff, "total_staff":total_staff,
        "total_male_adm": total_male_adm,"total_female_adm":total_female_adm,"total_adm":total_adm, 
        "total_male_teacher": total_male_teacher,"total_female_teacher":total_female_teacher,"total_teacher":total_teacher,
        "total_male_support": total_male_support,"total_female_support":total_female_support,"total_support": total_support, 
        "total_male_non_teaching": total_male_non_teaching,"total_female_non_teaching":total_female_non_teaching,"total_non_teaching":total_non_teaching,
        
    }
    return render(request, "lss.html", context)

def ps_home(request):
    ps = School.objects.filter(category="PS")
    #students stats
    total_male_std = students.objects.filter(category="PS").aggregate(Sum('total_boys'))
    total_female_std = students.objects.filter(category="PS").aggregate(Sum('total_girls'))
    total_students  = students.objects.filter(category="PS").aggregate(Sum('total_students'))

    total_boarder_boys = students.objects.filter(category="PS").aggregate(Sum('total_boarder_boys'))
    total_boarder_girls  = students.objects.filter(category="PS").aggregate(Sum('total_boarder_girls'))
    total_boarder_students  = students.objects.filter(category="PS").aggregate(Sum('total_boarder_students'))

    total_dayscholar_boys = students.objects.filter(category="PS").aggregate(Sum('total_dayscholar_boys'))
    total_dayscholar_girls  = students.objects.filter(category="PS").aggregate(Sum('total_dayscholar_girls'))
    total_dayscholar_students  = students.objects.filter(category="PS").aggregate(Sum('total_dayscholar_students'))

    #Staff stats
    total_male_staff = StaffDetail.objects.filter(school_category="PS",gender="Male").count()
    total_female_staff = StaffDetail.objects.filter(school_category="PS", gender="Female").count()
    total_staff = StaffDetail.objects.filter(school_category="PS").count()

    total_male_adm = StaffDetail.objects.filter(school_category="PS",category="Administration",gender="Male").count()
    total_female_adm = StaffDetail.objects.filter(school_category="PS",category="Administration", gender="Female").count()
    total_adm = StaffDetail.objects.filter(school_category="PS",category="Administration").count()

    total_male_teacher = StaffDetail.objects.filter(school_category="PS",category="Teaching Staff",gender="Male").count()
    total_female_teacher = StaffDetail.objects.filter(school_category="PS",category="Teaching Staff", gender="Female").count()
    total_teacher = StaffDetail.objects.filter(school_category="PS",category="Teaching Staff").count()

    total_male_support = StaffDetail.objects.filter(school_category="PS",category="Supporting Staff", gender="Male").count()
    total_female_support = StaffDetail.objects.filter(school_category="PS",category="Supporting Staff",gender="Female").count()
    total_support = StaffDetail.objects.filter(school_category="PS",category="Supporting Staff").count()

    total_male_non_teaching = StaffDetail.objects.filter(school_category="PS",category="Non Teaching Staff",gender="Male").count()
    total_female_non_teaching = StaffDetail.objects.filter(school_category="PS",category="Non Teaching Staff", gender="Female").count()
    total_non_teaching = StaffDetail.objects.filter(school_category="PS",category="Non Teaching Staff").count()
    
    context = {
        "ps":ps,
        "total_male_std":total_male_std['total_boys__sum'],"total_female_std":total_female_std['total_girls__sum'],"total_students":total_students['total_students__sum'],
        "total_boarder_boys":total_boarder_boys['total_boarder_boys__sum'], "total_boarder_girls":total_boarder_girls['total_boarder_girls__sum'], "total_boarder_students":total_boarder_students['total_boarder_students__sum'],
        "total_dayscholar_boys":total_dayscholar_boys['total_dayscholar_boys__sum'],  "total_dayscholar_girls":total_dayscholar_girls['total_dayscholar_girls__sum'],"total_dayscholar_students":total_dayscholar_students['total_dayscholar_students__sum'],

        "total_male_staff": total_male_staff,"total_female_staff":total_female_staff, "total_staff":total_staff,
        "total_male_adm": total_male_adm,"total_female_adm":total_female_adm,"total_adm":total_adm, 
        "total_male_teacher": total_male_teacher,"total_female_teacher":total_female_teacher,"total_teacher":total_teacher,
        "total_male_support": total_male_support,"total_female_support":total_female_support,"total_support": total_support, 
        "total_male_non_teaching": total_male_non_teaching,"total_female_non_teaching":total_female_non_teaching,"total_non_teaching":total_non_teaching,
        
    }
    return render(request, "ps.html", context)

def msi_home(request):
    muenseling = School.objects.filter(category="Muenseling")
    #students stats
    total_male_std = students.objects.filter(category="Muenseling").aggregate(Sum('total_boys'))
    total_female_std = students.objects.filter(category="Muenseling").aggregate(Sum('total_girls'))
    total_students  = students.objects.filter(category="Muenseling").aggregate(Sum('total_students'))

    total_boarder_boys = students.objects.filter(category="Muenseling").aggregate(Sum('total_boarder_boys'))
    total_boarder_girls  = students.objects.filter(category="Muenseling").aggregate(Sum('total_boarder_girls'))
    total_boarder_students  = students.objects.filter(category="Muenseling").aggregate(Sum('total_boarder_students'))

    total_dayscholar_boys = students.objects.filter(category="Muenseling").aggregate(Sum('total_dayscholar_boys'))
    total_dayscholar_girls  = students.objects.filter(category="Muenseling").aggregate(Sum('total_dayscholar_girls'))
    total_dayscholar_students  = students.objects.filter(category="Muenseling").aggregate(Sum('total_dayscholar_students'))

    #Staff stats
    total_male_staff = StaffDetail.objects.filter(school_category="Muenseling",gender="Male").count()
    total_female_staff = StaffDetail.objects.filter(school_category="Muenseling", gender="Female").count()
    total_staff = StaffDetail.objects.filter(school_category="Muenseling").count()

    total_male_adm = StaffDetail.objects.filter(school_category="Muenseling",category="Administration",gender="Male").count()
    total_female_adm = StaffDetail.objects.filter(school_category="Muenseling",category="Administration", gender="Female").count()
    total_adm = StaffDetail.objects.filter(school_category="Muenseling",category="Administration").count()

    total_male_teacher = StaffDetail.objects.filter(school_category="Muenseling",category="Teaching Staff",gender="Male").count()
    total_female_teacher = StaffDetail.objects.filter(school_category="Muenseling",category="Teaching Staff", gender="Female").count()
    total_teacher = StaffDetail.objects.filter(school_category="Muenseling",category="Teaching Staff").count()

    total_male_support = StaffDetail.objects.filter(school_category="Muenseling",category="Supporting Staff", gender="Male").count()
    total_female_support = StaffDetail.objects.filter(school_category="Muenseling",category="Supporting Staff",gender="Female").count()
    total_support = StaffDetail.objects.filter(school_category="Muenseling",category="Supporting Staff").count()

    total_male_non_teaching = StaffDetail.objects.filter(school_category="Muenseling",category="Non Teaching Staff",gender="Male").count()
    total_female_non_teaching = StaffDetail.objects.filter(school_category="Muenseling",category="Non Teaching Staff", gender="Female").count()
    total_non_teaching = StaffDetail.objects.filter(school_category="Muenseling",category="Non Teaching Staff").count()
    
    context = {
        "muenseling":muenseling,
        "total_male_std":total_male_std['total_boys__sum'],"total_female_std":total_female_std['total_girls__sum'],"total_students":total_students['total_students__sum'],
        "total_boarder_boys":total_boarder_boys['total_boarder_boys__sum'], "total_boarder_girls":total_boarder_girls['total_boarder_girls__sum'], "total_boarder_students":total_boarder_students['total_boarder_students__sum'],
        "total_dayscholar_boys":total_dayscholar_boys['total_dayscholar_boys__sum'],  "total_dayscholar_girls":total_dayscholar_girls['total_dayscholar_girls__sum'],"total_dayscholar_students":total_dayscholar_students['total_dayscholar_students__sum'],

        "total_male_staff": total_male_staff,"total_female_staff":total_female_staff, "total_staff":total_staff,
        "total_male_adm": total_male_adm,"total_female_adm":total_female_adm,"total_adm":total_adm, 
        "total_male_teacher": total_male_teacher,"total_female_teacher":total_female_teacher,"total_teacher":total_teacher,
        "total_male_support": total_male_support,"total_female_support":total_female_support,"total_support": total_support, 
        "total_male_non_teaching": total_male_non_teaching,"total_female_non_teaching":total_female_non_teaching,"total_non_teaching":total_non_teaching,   
    }
    return render(request, "muenselinginst.html", context)
