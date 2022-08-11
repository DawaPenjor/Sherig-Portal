from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contactUs, name='contactUs'),

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