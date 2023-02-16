from django.db import models
from django.contrib.auth.models import AbstractUser
import os
import uuid
from django.conf import settings

# Create your models here.

class School(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    school = models.CharField(max_length=250, unique=True)
    SCHOOL_TYPE = [
        ('DZO', 'Dzongkhag'),
        ('HSS', 'Higher Secondary School'),
        ('MSS', 'Middle Secondary School'),
        ('LSS', 'Lower Secondary School'),
        ('PS', 'Primary School'),
        ('Muenseling', 'Muenseling Institute')
    ]
    category = models.CharField(max_length=20, choices=SCHOOL_TYPE)
    

    def __str__(self):
        return self.school

class CustomUser(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    school = models.ForeignKey(School, null=True, on_delete=models.CASCADE)
    is_superuser = models.BooleanField("Super admin", default=False)
    is_school = models.BooleanField("school admin", default=False)
    is_dzongkhag = models.BooleanField("dzongkhag admin", default=False)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    school = models.ForeignKey(School, null=True, on_delete=models.CASCADE)
    pro_pic = models.ImageField(default='profiles/user-default.png', upload_to='profiles', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return str(self.user.username)

class APA(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    date_uploaded = models.DateTimeField(auto_now=True)
    APA_file = models.FileField(blank=True, null=True, upload_to="files")
    

class FYP(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    date_uploaded = models.DateTimeField(auto_now=True)
    FYP_file = models.FileField(blank=True, null=True, upload_to="files")
    

class StaffDetail(models.Model):
    Owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    School = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    school_category = models.CharField(max_length=50, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Employee_ID = models.BigIntegerField(null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)

    GENDER_MALE = 'Male'
    GENDER_FEMALE = 'Female'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=30, blank=True)
    date_of_birth = models.DateField(
        auto_now=False, auto_now_add=False, blank=True)
    CID = models.CharField(max_length=11, unique=True, blank=True)

    Administration = 'Administration'
    TeachingStaff = 'Teaching Staff'
    NonTeachingStaff = 'Non Teaching Staff'
    SupportingStaff = 'Supporting Staff'
    Category_choices = [(Administration, 'Administration'),
                        (TeachingStaff, 'Teaching Staff'),
                        (NonTeachingStaff, 'Non Teaching Staff'),
                        (SupportingStaff, 'Supporting Staff'), ]
    category = models.CharField(
        choices=Category_choices, max_length=30, blank=True)

    position_title = models.CharField(max_length=50, blank=True)
    position_level = models.CharField(max_length=10, blank=True)
    grade = models.CharField(max_length=5, blank=True)
    appointment_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=True)
    joining_date_of_present_school = models.DateField(
        auto_now=False, auto_now_add=False, blank=True)
    transfered_from = models.CharField(max_length=50, blank=True)

    Regular = 'Regular'
    Contract = 'Contract'
    Employment_choices = [(Regular, 'Regular'), (Contract, 'Contract')]
    Employment_type = models.CharField(
        choices=Employment_choices, max_length=30, blank=True)

    nationality = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=50, blank=True)
    qualification = models.TextField(blank=True)
    contact_number = models.CharField(
        max_length=8, blank=True)
    email = models.EmailField(blank=True, unique=True)
    permanent_address = models.TextField(blank=True)
    profile_pic = models.ImageField(
        default='profiles/user-default.png', upload_to='staff', null=True, blank=True)

    def __str__(self):
        return self.name

class StaffOnleave(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    School = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)

    ML = 'ML'
    LTT = 'LTT'
    EoL = 'EoL'
    Superannuation = 'Superannuation'
    Resignation = 'Resignation'
    leave_choices = [(ML, 'ML'),
                    (LTT, 'LTT'),
                    (EoL, 'EoL'),
                    (Superannuation, 'Superannuation'),
                    (Resignation, 'Resignation'),]
    type_of_leave = models.CharField(
        choices=leave_choices, max_length=30, blank=True, null=True)

    office_order = models.CharField(max_length=250, null=True, blank=True)
    Start_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    End_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    remark = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

class students(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True, related_name='school_name')
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)

    PP = 'PP'
    I = '1'
    II = '2'
    III = '3'
    IV = '4'
    V = '5'
    VI = '6'
    VII = '7'
    VIII = '8'
    IX = '9'
    X = '10'
    XI = '11'
    XII = '12'
    Braille = "Braille"
    
    standard_choices = [(PP, 'PP'),(I, '1'),(II, '2'),
                        (III, '3'),(IV, '4'),(V, '5'),(VI, '6'),(VII, '7'),
                        (VIII, '8'),(IX, '9'),(X, '10'),(XI, '11'),(XII, '12'),(Braille, "Braille")]
    standard = models.CharField(choices=standard_choices, max_length=30, blank=True)

    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'

    section_choices = [(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D'), (E, 'E')]
    section = models.CharField(choices=section_choices, max_length=2, null=True, blank=True)

    EVS = 'EVS'
    Economics = 'Economics'
    Agri = 'Agri'
    Arts = 'Arts'
    Commerce = 'Commerce'
    Science = 'Science'
    General = 'General'

    stream_choices = [(EVS,'EVS'),(Economics,'Economics'),(Agri,'Agri'),(Arts, 'Arts'), (Commerce, 'Commerce'), (Science, 'Science'), (General, 'General'),]
    stream = models.CharField(choices=stream_choices, max_length=100, null=True, blank=True)

    total_boys = models.IntegerField(null=True, blank=True)
    total_girls = models.IntegerField(null=True, blank=True)
    total_students = models.IntegerField(null=True, blank=True)

    total_boarder_boys = models.IntegerField(null=True, blank=True)
    total_boarder_girls = models.IntegerField(null=True, blank=True)
    total_boarder_students = models.IntegerField(null=True, blank=True)

    total_dayscholar_boys = models.IntegerField(null=True, blank=True)
    total_dayscholar_girls = models.IntegerField(null=True, blank=True)
    total_dayscholar_students = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.standard

class TopperOfYear(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=100, null=True, blank=True)
    
    Male = 'Male'
    Female = 'Female'
    gender_choices = [(Male, 'Male'), (Female, 'Female')]
    gender = models.CharField(choices=gender_choices, max_length=30, blank=True)

    PP = 'PP'
    I = '1'
    II = '2'
    III = '3'
    IV = '4'
    V = '5'
    VI = '6'
    VII = '7'
    VIII = '8'
    IX = '9'
    X = '10'
    XI = '11'
    XII = '12'
    Braille = "Braille"
    
    standard_choices = [(PP, 'PP'),(I, '1'),(II, '2'),
                        (III, '3'),(IV, '4'),(V, '5'),(VI, '6'),(VII, '7'),
                        (VIII, '8'),(IX, '9'),(X, '10'),(XI, '11'),(XII, '12'),(Braille, "Braille")]
    standard = models.CharField(choices=standard_choices, max_length=30, blank=True)

    EVS = 'EVS'
    Economics = 'Economics'
    Agri = 'Agri'
    Arts = 'Arts'
    Commerce = 'Commerce'
    Science = 'Science'
    General = 'General'

    stream_choices = [(EVS,'EVS'),(Economics,'Economics'),(Agri,'Agri'),(Arts, 'Arts'), (Commerce, 'Commerce'), (Science, 'Science'), (General, 'General'),]
    stream = models.CharField(choices=stream_choices, max_length=100, null=True, blank=True)
    
    subject = models.CharField(max_length=100, null=True, blank=True)
    percentage = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Tozay(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=100, null=True, blank=True)
    
    Male = 'Male'
    Female = 'Female'
    gender_choices = [(Male, 'Male'), (Female, 'Female')]
    gender = models.CharField(choices=gender_choices, max_length=30, blank=True)

    PP = 'PP'
    I = '1'
    II = '2'
    III = '3'
    IV = '4'
    V = '5'
    VI = '6'
    VII = '7'
    VIII = '8'
    IX = '9'
    X = '10'
    XI = '11'
    XII = '12'
    Braille = "Braille"
    
    standard_choices = [(PP, 'PP'),(I, '1'),(II, '2'),
                        (III, '3'),(IV, '4'),(V, '5'),(VI, '6'),(VII, '7'),
                        (VIII, '8'),(IX, '9'),(X, '10'),(XI, '11'),(XII, '12'),(Braille, "Braille")]
    standard = models.CharField(choices=standard_choices, max_length=30, blank=True)

    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'

    section_choices = [(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D'), (E, 'E')]
    section = models.CharField(choices=section_choices, max_length=2, null=True, blank=True)

    EVS = 'EVS'
    Economics = 'Economics'
    Agri = 'Agri'
    Arts = 'Arts'
    Commerce = 'Commerce'
    Science = 'Science'
    General = 'General'

    stream_choices = [(EVS,'EVS'),(Economics,'Economics'),(Agri,'Agri'),(Arts, 'Arts'), (Commerce, 'Commerce'), (Science, 'Science'), (General, 'General'),]
    stream = models.CharField(choices=stream_choices, max_length=100, null=True, blank=True)
    percentage = models.CharField(max_length=100, null=True, blank=True)
    DoB = models.DateField(
        auto_now=False, auto_now_add=False, blank=True)
    CID = models.CharField(max_length=11, unique=True, blank=True)
    student_code = models.CharField(max_length=100, null=True, blank=True)
    village = models.CharField(max_length=50, null=True, blank=True)
    gewog = models.CharField(max_length=50, null=True, blank=True)
    dzongkhag = models.CharField(max_length=50, null=True, blank=True)
    father_name = models.CharField(max_length=50, null=True, blank=True)
    father_CID = models.CharField(max_length=50, null=True, blank=True)
    mother_name = models.CharField(max_length=50, null=True, blank=True)
    mother_CID = models.CharField(max_length=50, null=True, blank=True) 
    reason = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class CapitalActivites(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    activity = models.CharField(max_length=300, null=True, blank=True)
    budget = models.BigIntegerField(null=True, blank=True)
    start_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    contractor_name = models.CharField(max_length=50, blank=True)
    contractor_mobile_number = models.CharField(max_length=12, blank=True)
    engineer_name = models.CharField(max_length=50, blank=True)
    engineer_mobile_number = models.CharField(max_length=12, blank=True)
    remark = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.activity

class SchoolInfrastructure(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    item = models.CharField(max_length=200, null=True, blank=True)
    total_number = models.IntegerField(null=True, blank=True)
    units = models.IntegerField(null=True, blank=True)
    bought_year = models.IntegerField(null=True, blank=True)
    renovation_year = models.IntegerField(null=True, blank=True)
    remark = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.item