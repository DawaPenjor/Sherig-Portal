from django.shortcuts import render
from . models import StaffDetail, students, School
from django.db.models import Sum

def information(request):
    #Summary of Students at various levels
    # class PP
    total_male_std_pp = students.objects.filter(standard="PP").aggregate(Sum('total_boys'))
    total_female_std_pp = students.objects.filter(standard="PP").aggregate(Sum('total_girls'))
    total_std_pp = students.objects.filter(standard="PP").aggregate(Sum('total_students'))

    #class I
    total_male_std_I = students.objects.filter(standard="1").aggregate(Sum('total_boys'))
    total_female_std_I = students.objects.filter(standard="1").aggregate(Sum('total_girls'))
    total_std_I = students.objects.filter(standard="1").aggregate(Sum('total_students'))

    #class II
    total_male_std_II = students.objects.filter(standard="2").aggregate(Sum('total_boys'))
    total_female_std_II = students.objects.filter(standard="2").aggregate(Sum('total_girls'))
    total_std_II = students.objects.filter(standard="2").aggregate(Sum('total_students'))

    #class III
    total_male_std_III = students.objects.filter(standard="3").aggregate(Sum('total_boys'))
    total_female_std_III = students.objects.filter(standard="3").aggregate(Sum('total_girls'))
    total_std_III = students.objects.filter(standard="3").aggregate(Sum('total_students'))

    #class IV
    total_male_std_IV = students.objects.filter(standard="4").aggregate(Sum('total_boys'))
    total_female_std_IV = students.objects.filter(standard="4").aggregate(Sum('total_girls'))
    total_std_IV = students.objects.filter(standard="4").aggregate(Sum('total_students'))

    #class V
    total_male_std_V = students.objects.filter(standard="5").aggregate(Sum('total_boys'))
    total_female_std_V = students.objects.filter(standard="5").aggregate(Sum('total_girls'))
    total_std_V = students.objects.filter(standard="5").aggregate(Sum('total_students'))

    #class VI
    total_male_std_VI = students.objects.filter(standard="6").aggregate(Sum('total_boys'))
    total_female_std_VI = students.objects.filter(standard="6").aggregate(Sum('total_girls'))
    total_std_VI = students.objects.filter(standard="6").aggregate(Sum('total_students'))

    #class VII
    total_male_std_VII = students.objects.filter(standard="7").aggregate(Sum('total_boys'))
    total_female_std_VII = students.objects.filter(standard="7").aggregate(Sum('total_girls'))
    total_std_VII = students.objects.filter(standard="7").aggregate(Sum('total_students'))
    
    #class VIII
    total_male_std_VIII = students.objects.filter(standard="8").aggregate(Sum('total_boys'))
    total_female_std_VIII = students.objects.filter(standard="8").aggregate(Sum('total_girls'))
    total_std_VIII = students.objects.filter(standard="8").aggregate(Sum('total_students'))

    #class IX
    total_male_std_IX = students.objects.filter(standard="9").aggregate(Sum('total_boys'))
    total_female_std_IX = students.objects.filter(standard="9").aggregate(Sum('total_girls'))
    total_std_IX = students.objects.filter(standard="9").aggregate(Sum('total_students'))

    #class X
    total_male_std_X = students.objects.filter(standard="10").aggregate(Sum('total_boys'))
    total_female_std_X = students.objects.filter(standard="10").aggregate(Sum('total_girls'))
    total_std_X = students.objects.filter(standard="10").aggregate(Sum('total_students'))

    #class XI
    total_male_std_XI = students.objects.filter(standard="11").aggregate(Sum('total_boys'))
    total_female_std_XI = students.objects.filter(standard="11").aggregate(Sum('total_girls'))
    total_std_XI = students.objects.filter(standard="11").aggregate(Sum('total_students'))

    #class XII
    total_male_std_XII = students.objects.filter(standard="12").aggregate(Sum('total_boys'))
    total_female_std_XII = students.objects.filter(standard="12").aggregate(Sum('total_girls'))
    total_std_XII = students.objects.filter(standard="12").aggregate(Sum('total_students'))

    #Total Stds
    total_male_std = students.objects.all().aggregate(Sum('total_boys'))
    total_female_std = students.objects.all().aggregate(Sum('total_girls'))
    total_std = students.objects.all().aggregate(Sum('total_students'))

    #Details of Boarder and Dayscholar students
    # HSS
    total_male_boarder_std_hss = students.objects.filter(category="HSS").aggregate(Sum('total_boarder_boys'))
    total_female_boarder_std_hss = students.objects.filter(category="HSS").aggregate(Sum('total_boarder_girls'))
    total_boarder_std_hss = students.objects.filter(category="HSS").aggregate(Sum('total_boarder_students'))
    total_male_dayscholar_std_hss = students.objects.filter(category="HSS").aggregate(Sum('total_dayscholar_boys'))
    total_female_dayscholar_std_hss = students.objects.filter(category="HSS").aggregate(Sum('total_dayscholar_girls'))
    total_dayscholar_std_hss = students.objects.filter(category="HSS").aggregate(Sum('total_dayscholar_students'))

    # MSS
    total_male_boarder_std_mss = students.objects.filter(category="MSS").aggregate(Sum('total_boarder_boys'))
    total_female_boarder_std_mss = students.objects.filter(category="MSS").aggregate(Sum('total_boarder_girls'))
    total_boarder_std_mss = students.objects.filter(category="MSS").aggregate(Sum('total_boarder_students'))
    total_male_dayscholar_std_mss = students.objects.filter(category="MSS").aggregate(Sum('total_dayscholar_boys'))
    total_female_dayscholar_std_mss = students.objects.filter(category="MSS").aggregate(Sum('total_dayscholar_girls'))
    total_dayscholar_std_mss = students.objects.filter(category="MSS").aggregate(Sum('total_dayscholar_students'))

    # LSS
    total_male_boarder_std_lss = students.objects.filter(category="LSS").aggregate(Sum('total_boarder_boys'))
    total_female_boarder_std_lss = students.objects.filter(category="LSS").aggregate(Sum('total_boarder_girls'))
    total_boarder_std_lss = students.objects.filter(category="LSS").aggregate(Sum('total_boarder_students'))
    total_male_dayscholar_std_lss = students.objects.filter(category="LSS").aggregate(Sum('total_dayscholar_boys'))
    total_female_dayscholar_std_lss = students.objects.filter(category="LSS").aggregate(Sum('total_dayscholar_girls'))
    total_dayscholar_std_lss = students.objects.filter(category="LSS").aggregate(Sum('total_dayscholar_students'))
    
    # PS
    total_male_boarder_std_ps = students.objects.filter(category="PS").aggregate(Sum('total_boarder_boys'))
    total_female_boarder_std_ps = students.objects.filter(category="PS").aggregate(Sum('total_boarder_girls'))
    total_boarder_std_ps = students.objects.filter(category="PS").aggregate(Sum('total_boarder_students'))
    total_male_dayscholar_std_ps = students.objects.filter(category="PS").aggregate(Sum('total_dayscholar_boys'))
    total_female_dayscholar_std_ps = students.objects.filter(category="PS").aggregate(Sum('total_dayscholar_girls'))
    total_dayscholar_std_ps = students.objects.filter(category="PS").aggregate(Sum('total_dayscholar_students'))
    
    # Muenseling
    total_male_boarder_std_msi = students.objects.filter(category="Muenseling").aggregate(Sum('total_boarder_boys'))
    total_female_boarder_std_msi = students.objects.filter(category="Muenseling").aggregate(Sum('total_boarder_girls'))
    total_boarder_std_msi = students.objects.filter(category="Muenseling").aggregate(Sum('total_boarder_students'))
    total_male_dayscholar_std_msi = students.objects.filter(category="Muenseling").aggregate(Sum('total_dayscholar_boys'))
    total_female_dayscholar_std_msi = students.objects.filter(category="Muenseling").aggregate(Sum('total_dayscholar_girls'))
    total_dayscholar_std_msi = students.objects.filter(category="Muenseling").aggregate(Sum('total_dayscholar_students'))
    
    total_male_boarder_std = students.objects.all().aggregate(Sum('total_boarder_boys'))
    total_female_boarder_std = students.objects.all().aggregate(Sum('total_boarder_girls'))
    total_boarder_std = students.objects.all().aggregate(Sum('total_boarder_students'))
    total_male_dayscholar_std = students.objects.all().aggregate(Sum('total_dayscholar_boys'))
    total_female_dayscholar_std = students.objects.all().aggregate(Sum('total_dayscholar_girls'))
    total_dayscholar_std = students.objects.all().aggregate(Sum('total_dayscholar_students'))
    
    # Stats of staff at each school
    #HSS
    total_male_teacher_hss = StaffDetail.objects.filter(school_category="HSS",category="Teaching Staff",gender="Male").count()
    total_female_teacher_hss = StaffDetail.objects.filter(school_category="HSS",category="Teaching Staff", gender="Female").count()
    total_teacher_hss = StaffDetail.objects.filter(school_category="HSS",category="Teaching Staff").count()

    total_male_support_hss = StaffDetail.objects.filter(school_category="HSS",category="Supporting Staff", gender="Male").count()
    total_female_support_hss = StaffDetail.objects.filter(school_category="HSS",category="Supporting Staff",gender="Female").count()
    total_support_hss = StaffDetail.objects.filter(school_category="HSS",category="Supporting Staff").count()

    total_male_non_teaching_hss = StaffDetail.objects.filter(school_category="HSS",category="Non Teaching Staff",gender="Male").count()
    total_female_non_teaching_hss = StaffDetail.objects.filter(school_category="HSS",category="Non Teaching Staff", gender="Female").count()
    total_non_teaching_hss = StaffDetail.objects.filter(school_category="HSS",category="Non Teaching Staff").count()
    
    #MSS
    total_male_teacher_mss = StaffDetail.objects.filter(school_category="MSS",category="Teaching Staff",gender="Male").count()
    total_female_teacher_mss = StaffDetail.objects.filter(school_category="MSS",category="Teaching Staff", gender="Female").count()
    total_teacher_mss = StaffDetail.objects.filter(school_category="MSS",category="Teaching Staff").count()

    total_male_support_mss = StaffDetail.objects.filter(school_category="MSS",category="Supporting Staff", gender="Male").count()
    total_female_support_mss = StaffDetail.objects.filter(school_category="MSS",category="Supporting Staff",gender="Female").count()
    total_support_mss = StaffDetail.objects.filter(school_category="MSS",category="Supporting Staff").count()

    total_male_non_teaching_mss = StaffDetail.objects.filter(school_category="MSS",category="Non Teaching Staff",gender="Male").count()
    total_female_non_teaching_mss = StaffDetail.objects.filter(school_category="MSS",category="Non Teaching Staff", gender="Female").count()
    total_non_teaching_mss = StaffDetail.objects.filter(school_category="MSS",category="Non Teaching Staff").count()

    #LSS
    total_male_teacher_lss = StaffDetail.objects.filter(school_category="LSS",category="Teaching Staff",gender="Male").count()
    total_female_teacher_lss = StaffDetail.objects.filter(school_category="LSS",category="Teaching Staff", gender="Female").count()
    total_teacher_lss = StaffDetail.objects.filter(school_category="LSS",category="Teaching Staff").count()

    total_male_support_lss = StaffDetail.objects.filter(school_category="LSS",category="Supporting Staff", gender="Male").count()
    total_female_support_lss = StaffDetail.objects.filter(school_category="LSS",category="Supporting Staff",gender="Female").count()
    total_support_lss = StaffDetail.objects.filter(school_category="LSS",category="Supporting Staff").count()

    total_male_non_teaching_lss = StaffDetail.objects.filter(school_category="LSS",category="Non Teaching Staff",gender="Male").count()
    total_female_non_teaching_lss = StaffDetail.objects.filter(school_category="LSS",category="Non Teaching Staff", gender="Female").count()
    total_non_teaching_lss = StaffDetail.objects.filter(school_category="LSS",category="Non Teaching Staff").count()
    
    #PS
    total_male_teacher_ps = StaffDetail.objects.filter(school_category="PS",category="Teaching Staff",gender="Male").count()
    total_female_teacher_ps = StaffDetail.objects.filter(school_category="PS",category="Teaching Staff", gender="Female").count()
    total_teacher_ps = StaffDetail.objects.filter(school_category="PS",category="Teaching Staff").count()

    total_male_support_ps = StaffDetail.objects.filter(school_category="PS",category="Supporting Staff", gender="Male").count()
    total_female_support_ps = StaffDetail.objects.filter(school_category="PS",category="Supporting Staff",gender="Female").count()
    total_support_ps = StaffDetail.objects.filter(school_category="PS",category="Supporting Staff").count()

    total_male_non_teaching_ps = StaffDetail.objects.filter(school_category="PS",category="Non Teaching Staff",gender="Male").count()
    total_female_non_teaching_ps = StaffDetail.objects.filter(school_category="PS",category="Non Teaching Staff", gender="Female").count()
    total_non_teaching_ps = StaffDetail.objects.filter(school_category="PS",category="Non Teaching Staff").count()
    
    #muenseling
    total_male_teacher_msi = StaffDetail.objects.filter(school_category="Muenseling",category="Teaching Staff",gender="Male").count()
    total_female_teacher_msi = StaffDetail.objects.filter(school_category="Muenseling",category="Teaching Staff", gender="Female").count()
    total_teacher_msi = StaffDetail.objects.filter(school_category="Muenseling",category="Teaching Staff").count()

    total_male_support_msi = StaffDetail.objects.filter(school_category="Muenseling",category="Supporting Staff", gender="Male").count()
    total_female_support_msi = StaffDetail.objects.filter(school_category="Muenseling",category="Supporting Staff",gender="Female").count()
    total_support_msi = StaffDetail.objects.filter(school_category="Muenseling",category="Supporting Staff").count()

    total_male_non_teaching_msi = StaffDetail.objects.filter(school_category="Muenseling",category="Non Teaching Staff",gender="Male").count()
    total_female_non_teaching_msi = StaffDetail.objects.filter(school_category="Muenseling",category="Non Teaching Staff", gender="Female").count()
    total_non_teaching_msi = StaffDetail.objects.filter(school_category="Muenseling",category="Non Teaching Staff").count()

    #Grand total
    total_male_teacher = StaffDetail.objects.filter(category="Teaching Staff",gender="Male").count()
    total_female_teacher = StaffDetail.objects.filter(category="Teaching Staff", gender="Female").count()
    total_teacher = StaffDetail.objects.filter(category="Teaching Staff").count()

    total_male_support = StaffDetail.objects.filter(category="Supporting Staff", gender="Male").count()
    total_female_support = StaffDetail.objects.filter(category="Supporting Staff",gender="Female").count()
    total_support = StaffDetail.objects.filter(category="Supporting Staff").count()

    total_male_non_teaching = StaffDetail.objects.filter(category="Non Teaching Staff",gender="Male").count()
    total_female_non_teaching = StaffDetail.objects.filter(category="Non Teaching Staff", gender="Female").count()
    total_non_teaching = StaffDetail.objects.filter(category="Non Teaching Staff").count()    
    
    #Stats of students at each school
    sch_id  = School.objects.exclude(category="DZO")
    school_name = []
    boys = []
    girls = []
    total = []
    
    for i in sch_id:
        school_list = i
        school_name.append(school_list)
        total_male = students.objects.filter(school_id = i).aggregate(Sum('total_boys'))   
        boys.append(total_male['total_boys__sum'])        
        total_female = students.objects.filter(school_id = i).aggregate(Sum('total_girls'))
        girls.append(total_female['total_girls__sum'])    
        total_students = students.objects.filter(school_id = i).aggregate(Sum('total_students'))
        total.append(total_students['total_students__sum'])
        #print("name:",i)
        #print("Boys:",total_male['total_boys__sum']) 
        #print("Girls:",total_female['total_girls__sum'])
        #print("Total:",total_std['total_students__sum'])
        #print()


    context = {
        #Stats of students at each school
        "school_name":school_name,
        "total_male":total_male['total_boys__sum'],
        "total_female":total_female['total_girls__sum'],
        "total_students":total_students['total_students__sum'],

        #Summary of Students at various levels
        "total_male_std_pp":total_male_std_pp['total_boys__sum'],
        "total_female_std_pp":total_female_std_pp['total_girls__sum'],
        "total_std_pp":total_std_pp['total_students__sum'],

        "total_male_std_I":total_male_std_I['total_boys__sum'],
        "total_female_std_I":total_female_std_I['total_girls__sum'],
        "total_std_I":total_std_I['total_students__sum'],

        "total_male_std_II":total_male_std_II['total_boys__sum'],
        "total_female_std_II":total_female_std_II['total_girls__sum'],
        "total_std_II":total_std_II['total_students__sum'],

        "total_male_std_III":total_male_std_III['total_boys__sum'],
        "total_female_std_III":total_female_std_III['total_girls__sum'],
        "total_std_III":total_std_III['total_students__sum'],

        "total_male_std_IV":total_male_std_IV['total_boys__sum'],
        "total_female_std_IV":total_female_std_IV['total_girls__sum'],
        "total_std_IV":total_std_IV['total_students__sum'],
        
        "total_male_std_V":total_male_std_V['total_boys__sum'],
        "total_female_std_V":total_female_std_V['total_girls__sum'],
        "total_std_V":total_std_V['total_students__sum'],
        
        "total_male_std_VI":total_male_std_VI['total_boys__sum'],
        "total_female_std_VI":total_female_std_VI['total_girls__sum'],
        "total_std_VI":total_std_VI['total_students__sum'],

        "total_male_std_VII":total_male_std_VII['total_boys__sum'],
        "total_female_std_VII":total_female_std_VII['total_girls__sum'],
        "total_std_VII":total_std_VII['total_students__sum'],
        
        "total_male_std_VIII":total_male_std_VIII['total_boys__sum'],
        "total_female_std_VIII":total_female_std_VIII['total_girls__sum'],
        "total_std_VIII":total_std_VIII['total_students__sum'],

        "total_male_std_IX":total_male_std_IX['total_boys__sum'],
        "total_female_std_IX":total_female_std_IX['total_girls__sum'],
        "total_std_IX":total_std_IX['total_students__sum'],

        "total_male_std_X":total_male_std_X['total_boys__sum'],
        "total_female_std_X":total_female_std_X['total_girls__sum'],
        "total_std_X":total_std_X['total_students__sum'],

        "total_male_std_XI":total_male_std_XI['total_boys__sum'],
        "total_female_std_XI":total_female_std_XI['total_girls__sum'],
        "total_std_XI":total_std_XI['total_students__sum'],

        "total_male_std_XII":total_male_std_XII['total_boys__sum'],
        "total_female_std_XII":total_female_std_XII['total_girls__sum'],
        "total_std_XII":total_std_XII['total_students__sum'],

        "total_male_std":total_male_std['total_boys__sum'],
        "total_female_std":total_female_std['total_girls__sum'],
        "total_std":total_std['total_students__sum'],

        #Details of Boarder and Dayscholar students
        "total_male_boarder_std_hss":total_male_boarder_std_hss['total_boarder_boys__sum'],
        "total_female_boarder_std_hss":total_female_boarder_std_hss['total_boarder_girls__sum'],
        "total_boarder_std_hss":total_boarder_std_hss['total_boarder_students__sum'],
        "total_male_dayscholar_std_hss":total_male_dayscholar_std_hss['total_dayscholar_boys__sum'],
        "total_female_dayscholar_std_hss":total_female_dayscholar_std_hss['total_dayscholar_girls__sum'],
        "total_dayscholar_std_hss":total_dayscholar_std_hss['total_dayscholar_students__sum'],

        "total_male_boarder_std_mss":total_male_boarder_std_mss['total_boarder_boys__sum'],
        "total_female_boarder_std_mss":total_female_boarder_std_mss['total_boarder_girls__sum'],
        "total_boarder_std_mss":total_boarder_std_mss['total_boarder_students__sum'],
        "total_male_dayscholar_std_mss":total_male_dayscholar_std_mss['total_dayscholar_boys__sum'],
        "total_female_dayscholar_std_mss":total_female_dayscholar_std_mss['total_dayscholar_girls__sum'],
        "total_dayscholar_std_mss":total_dayscholar_std_mss['total_dayscholar_students__sum'],

        "total_male_boarder_std_lss":total_male_boarder_std_lss['total_boarder_boys__sum'],
        "total_female_boarder_std_lss":total_female_boarder_std_lss['total_boarder_girls__sum'],
        "total_boarder_std_lss":total_boarder_std_lss['total_boarder_students__sum'],
        "total_male_dayscholar_std_lss":total_male_dayscholar_std_lss['total_dayscholar_boys__sum'],
        "total_female_dayscholar_std_lss":total_female_dayscholar_std_lss['total_dayscholar_girls__sum'],
        "total_dayscholar_std_lss":total_dayscholar_std_lss['total_dayscholar_students__sum'],

        "total_male_boarder_std_ps":total_male_boarder_std_ps['total_boarder_boys__sum'],
        "total_female_boarder_std_ps":total_female_boarder_std_ps['total_boarder_girls__sum'],
        "total_boarder_std_ps":total_boarder_std_ps['total_boarder_students__sum'],
        "total_male_dayscholar_std_ps":total_male_dayscholar_std_ps['total_dayscholar_boys__sum'],
        "total_female_dayscholar_std_ps":total_female_dayscholar_std_ps['total_dayscholar_girls__sum'],
        "total_dayscholar_std_ps":total_dayscholar_std_ps['total_dayscholar_students__sum'],

        "total_male_boarder_std_msi":total_male_boarder_std_msi['total_boarder_boys__sum'],
        "total_female_boarder_std_msi":total_female_boarder_std_msi['total_boarder_girls__sum'],
        "total_boarder_std_msi":total_boarder_std_msi['total_boarder_students__sum'],
        "total_male_dayscholar_std_msi":total_male_dayscholar_std_msi['total_dayscholar_boys__sum'],
        "total_female_dayscholar_std_msi":total_female_dayscholar_std_msi['total_dayscholar_girls__sum'],
        "total_dayscholar_std_msi":total_dayscholar_std_msi['total_dayscholar_students__sum'],

        "total_male_boarder_std":total_male_boarder_std['total_boarder_boys__sum'],
        "total_female_boarder_std":total_female_boarder_std['total_boarder_girls__sum'],
        "total_boarder_std":total_boarder_std['total_boarder_students__sum'],
        "total_male_dayscholar_std":total_male_dayscholar_std['total_dayscholar_boys__sum'],
        "total_female_dayscholar_std":total_female_dayscholar_std['total_dayscholar_girls__sum'],
        "total_dayscholar_std":total_dayscholar_std['total_dayscholar_students__sum'],

        #staff stats 
        "total_male_teacher_hss": total_male_teacher_hss,"total_female_teacher_hss":total_female_teacher_hss,"total_teacher_hss":total_teacher_hss,
        "total_male_support_hss": total_male_support_hss,"total_female_support_hss":total_female_support_hss,"total_support_hss": total_support_hss, 
        "total_male_non_teaching_hss": total_male_non_teaching_hss,"total_female_non_teaching_hss":total_female_non_teaching_hss,"total_non_teaching_hss":total_non_teaching_hss,

        "total_male_teacher_mss": total_male_teacher_mss,"total_female_teacher_mss":total_female_teacher_mss,"total_teacher_mss":total_teacher_mss,
        "total_male_support_mss": total_male_support_mss,"total_female_support_mss":total_female_support_mss,"total_support_mss": total_support_mss, 
        "total_male_non_teaching_mss": total_male_non_teaching_mss,"total_female_non_teaching_mss":total_female_non_teaching_mss,"total_non_teaching_mss":total_non_teaching_mss,

        "total_male_teacher_lss": total_male_teacher_lss,"total_female_teacher_lss":total_female_teacher_lss,"total_teacher_lss":total_teacher_lss,
        "total_male_support_lss": total_male_support_lss,"total_female_support_lss":total_female_support_lss,"total_support_lss": total_support_lss, 
        "total_male_non_teaching_lss": total_male_non_teaching_lss,"total_female_non_teaching_lss":total_female_non_teaching_lss,"total_non_teaching_lss":total_non_teaching_lss,
    
        "total_male_teacher_ps": total_male_teacher_ps,"total_female_teacher_ps":total_female_teacher_ps,"total_teacher_ps":total_teacher_ps,
        "total_male_support_ps": total_male_support_ps,"total_female_support_ps":total_female_support_ps,"total_support_ps": total_support_ps, 
        "total_male_non_teaching_ps": total_male_non_teaching_ps,"total_female_non_teaching_ps":total_female_non_teaching_ps,"total_non_teaching_ps":total_non_teaching_ps,
    
        "total_male_teacher_msi": total_male_teacher_msi,"total_female_teacher_msi":total_female_teacher_msi,"total_teacher_msi":total_teacher_msi,
        "total_male_support_msi": total_male_support_msi,"total_female_support_msi":total_female_support_msi,"total_support_msi": total_support_msi, 
        "total_male_non_teaching_msi": total_male_non_teaching_msi,"total_female_non_teaching_msi":total_female_non_teaching_msi,"total_non_teaching_msi":total_non_teaching_msi, 

        "total_male_teacher": total_male_teacher,"total_female_teacher":total_female_teacher,"total_teacher":total_teacher,
        "total_male_support": total_male_support,"total_female_support":total_female_support,"total_support": total_support, 
        "total_male_non_teaching": total_male_non_teaching,"total_female_non_teaching":total_female_non_teaching,"total_non_teaching":total_non_teaching,   
    }
    return render(request, 'info_at_glance.html', context)


