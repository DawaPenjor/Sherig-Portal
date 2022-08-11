from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class School(models.Model):
    school = models.CharField(max_length=250, unique=True)
    SCHOOL_TYPE = [
        ('DZO', 'Dzongkhag'),
        ('HSS', 'Higher Secondary School'),
        ('MSS', 'Middle Secondary School'),
        ('LSS', 'Lower Secondary School'),
        ('PS', 'Primary School'),
        ('ECR', 'Extended Classroom'),
        ('NFE', 'Non-formal Education'),
        ('Muenseling', 'Muenseling Institute')
    ]
    category = models.CharField(max_length=20, choices=SCHOOL_TYPE)

    def __str__(self):
        return self.school

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    school = models.ForeignKey(School, null=True, on_delete=models.CASCADE)
    is_school = models.BooleanField("school admin", default=False)
    is_dzongkhag = models.BooleanField("dzongkhag admin", default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']




    
    