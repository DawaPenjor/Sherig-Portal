from django.urls import path
from . import views, schooladminviews, infoviews, schoolpageviews
from django.contrib.auth import views as auth_views 

urlpatterns = [
    # Admin URL
    path('', views.home, name='home'),
    path('HSS', schoolpageviews.hss_home, name="hss_home"),
    path('MSS', schoolpageviews.mss_home, name="mss_home"),
    path('LSS', schoolpageviews.lss_home, name="lss_home"),
    path('PS', schoolpageviews.ps_home, name="ps_home"),
    path('Muenseling Inst', schoolpageviews.msi_home, name="msi_home"),
    path('contact', views.contactUs, name='contactUs'),
    path('principal contact', views.principalContact, name="principalContact"),
    path('about', views.about, name='about'),
    path('info-at-glance', infoviews.information, name="info"),

    path('profile/<str:pk>', views.profiles, name='profile'),
    
    path('APA', views.viewAPA, name='APA'),
    path('uploadAPA', views.uploadAPA, name='uploadAPA'),
    path('delete-apa/<str:pk>', views.deleteAPAFile, name='deleteAPA'),

    path('FYP', views.viewFYP, name='FYP'),
    path('uploadFYP', views.uploadFYP, name='uploadFYP'),
    path('delete-fyp/<str:pk>', views.deleteFYPFile, name='deleteFYP'),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="reset_password.html"),
        name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"),
        name='password_reset_done' ),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"),
        name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"),
        name='password_reset_complete'),
        

    path('login', views.loginUser, name='loginUser'),
    path('logout', views.logoutUser, name='logoutUser'),

    path('administrator', views.admIndex, name='admIndex'),

    path('add-school', views.registerSchool, name='registerSchool'),
    path('update-school/<str:school_id>', views.updateSchool, name='updateSchool'),
    path('delete-school/<str:school_id>', views.deleteSchool, name='deleteSchool'),
    
    path('reg-user', views.registerUser, name="registerUser"),    
    path('update-user/<str:user_id>', views.updateUser, name='updateUser'),
    path('delete-user/<str:user_id>', views.deleteUser, name='deleteUser'),
    
    #School Admin URL
    path('school-dashboard', schooladminviews.schoolIndex, name='schoolIndex'),
    path('account/<str:pk>', schooladminviews.accounts, name='account'),

    path('reg-staff', schooladminviews.addStaff, name='addStaff'),
    path('staff-list', schooladminviews.staffList, name='staffList'),
    path('staff-detail/<str:pk>', schooladminviews.staff_details, name='staff-details'),
    path('update-staff/<str:staff_id>', schooladminviews.updateStaff, name='updateStaff'),
    path('delete-staff/<str:staff_id>', schooladminviews.deleteStaff, name='deleteStaff'),

    path('add-staff-on-leave', schooladminviews.add_staff_on_leave, name='addStaffOnLeave'),
    path('staff-leave-list', schooladminviews.list_of_staff_on_leave, name='staffLeaveList'),
    path('update-staff-leave/<str:staff_id>', schooladminviews.update_staff_leave, name='updateStaffLeave'),
    path('delete-staff-on-leave/<str:staff_id>', schooladminviews.deleteStaffOnLeave, name='deleteStaffLeave'),

    path('reg-student', schooladminviews.addStudents, name='addStudents'),
    path('student-stats', schooladminviews.studentStats, name='studentStats'),
    path('update-std-stats/<str:std_id>', schooladminviews.update_students_stats, name='updateStudent'),
    path('delete-std-stats/<str:std_id>', schooladminviews.deleteStdStats, name='deleteStudent'),

    path('add-topper', schooladminviews.addTopper, name='addTopper'),
    path('topper-list', schooladminviews.topperList, name='topperList'),
    path('update-topper/<str:topper_id>', schooladminviews.update_topper_list, name='updateTopper'),
    path('delete-topper/<str:topper_id>', schooladminviews.deleteTopper, name='deleteTopper'),

    path('add-tozay', schooladminviews.addTozay, name='addTozay'),
    path('tozay-list', schooladminviews.tozayList, name='tozayList'),
    path('update-tozay/<str:tozay_id>', schooladminviews.update_tozay_list, name='updateTozay'),
    path('delete-tozay/<str:tozay_id>', schooladminviews.deleteTozay, name='deleteTozay'),

    path('add-cap-activity', schooladminviews.addCapitalActivity, name='addCapitalActivity'),
    path('cap-activity-list', schooladminviews.capActivityList, name='capActivityList'),
    path('update-cap-activity/<str:activity_id>', schooladminviews.update_cap_activity, name='updateCapitalActivity'),
    path('delete-cap-activity/<str:activity_id>', schooladminviews.deleteActivity, name='deleteActivity'),

    path('add-school-item', schooladminviews.addSchoolInfrastructure, name='addSchoolInfrastructure'),
    path('school-insfrastructure-list', schooladminviews.schoolInsfrastructureList, name='schoolInsfrastructureList'),
    path('update-school-insfrastructure/<str:item_id>', schooladminviews.update_school_insfrastructure, name='updateSchoolInsfrastructure'),
    path('delete-item/<str:item_id>', schooladminviews.deleteItem, name='deleteItem'),

]