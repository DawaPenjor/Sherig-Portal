from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contactUs, name='contactUs'),
    path('profile/<str:pk>', views.profile, name='profile'),

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
    
]