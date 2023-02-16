from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Profile)
admin.site.register(APA)
admin.site.register(FYP)
admin.site.register(StaffDetail)
admin.site.register(students)
admin.site.register(TopperOfYear)
admin.site.register(Tozay)
admin.site.register(CapitalActivites)

