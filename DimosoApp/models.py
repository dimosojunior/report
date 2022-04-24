from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from datetime import datetime, date
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("Your user name is required")
        
        

        user=self.model(
            email=self.normalize_email(email),
            username=username,
            
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,

        )
        user.is_admin=True
        user.is_staff=True
        
        user.is_superuser=True
        user.save(using=self._db)
        return user

    

  #HII NI PATH KWA AJILI YA KUHIFADHI HIZO IMAGE      
def get_profile_image_filepath(self, filename):
    return f'profile_images/{self.pk}/{"44.jpg"}'

#HII NI KWA AJILI YA KUPATA DEFAULT IMAGE KM MTU ASIPO INGIZA IMAGE ILI ISILETE ERRORS
def get_default_profile_image():
    return "media/44.jpg"

class MyUser(AbstractBaseUser):
    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
    username=models.CharField(verbose_name="user name", max_length=100, unique=True)
    middle_name=models.CharField(verbose_name="middle name", max_length=100, unique=False)
    last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
    company_name=models.CharField(verbose_name="company name", max_length=100, unique=False)
    phone=models.CharField(verbose_name="phone", max_length=15)
    profile_image = models.ImageField(upload_to='get_profile_image_filepath', blank=True, null=True)
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    


    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username']
    
    objects=MyUserManager()

    def __str__(self):
        return self.username

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class Darasa(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    idadi = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Combination(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    idadi = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
    
 


class ReportIssuesToParent(models.Model):
    
    email = models.EmailField(default="@gmail.com", blank=True, null=True)
    phone = models.CharField(default="+255", max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    send_through_email = RichTextUploadingField(blank=True, null=True)
    send_through_text = models.TextField(blank=True, null=True,default="NAME amepatikana na kosa la kuanzisha mgomo yeye pamoja na wanafunzi wenzake tarehe 20/4/2022 hivyo tunapenda kukutaarifu kupitia ofisi ya nidhamu shule ya secondary St.Dimoso kwamba mwanao amepewa suspension ya wiki mbili na pindi atakaporejea unaombwa kufika naye hapa shuleni, kwa taarifa zaidi wasiliana na mwalimu wa nidhamu shule ya secondary St. Dimoso.")
        
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    

    def __str__(self):
        return self.name







    
GENDER_CHOICES=(
    
    ('Male', 'Male'),
    ('Female', 'Female'),

    )    
        
class Form1Students(models.Model):
    darasa = models.ForeignKey(Darasa, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, blank=True, null=True)
    sname = models.CharField(max_length=200, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    year_of_study = models.CharField(max_length=200, blank=True, null=True)    
    
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/Form1Students/")
   # stu_class = models.CharField(default=name, max_length=200, blank=True, null=True)

    
    

# Create your models here.
class Form1Report(models.Model):
    title = RichTextUploadingField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(default="+255", max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField(default="Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021", max_length=1000, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/FormOne/")
    email = models.EmailField(blank=True, null=True)

    sub1 = models.CharField(default="Mathematics", max_length=200, blank=True, null=True)
    sub2 = models.CharField(default="English", max_length=200, blank=True, null=True)
    sub3 = models.CharField(default="Kiswahili", max_length=200, blank=True, null=True)
    sub4 = models.CharField(default="Physics", max_length=200, blank=True, null=True)
    sub5 = models.CharField(default="Biology", max_length=200, blank=True, null=True)
    

    sub1_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub2_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub3_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub4_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub5_marks = models.IntegerField(default= 100, blank=True, null=True)
    total_marks = models.IntegerField(default= 1000, blank=True, null=True)

    sub1_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub2_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub3_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub4_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub5_obtained = models.IntegerField(default= 80, blank=True, null=True)
    total_obtained = models.IntegerField(default= 800, blank=True, null=True)

    sub1_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub2_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub3_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub4_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub5_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    
    sub1_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub2_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub3_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub4_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub5_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)

    percentage = models.FloatField(blank=True, null=True)
    Overall_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    rank = models.CharField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=200, default= "Qualified", blank=True, null=True)
    stu_pos = models.IntegerField(blank=True, null=True)
    all_stu = models.IntegerField(blank=True, null=True)
    teacher_sign = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)




    #FORM TWO MODELS


GENDER_CHOICES=(
    
    ('Male', 'Male'),
    ('Female', 'Female'),

    )    
        
class Form2Students(models.Model):
    darasa = models.ForeignKey(Darasa, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, blank=True, null=True)
    sname = models.CharField(max_length=200, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    year_of_study = models.CharField(max_length=200, blank=True, null=True)    
    
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/Form2Students/")
   # stu_class = models.CharField(default=name, max_length=200, blank=True, null=True)

    
    

# Create your models here.
class Form2Report(models.Model):
    title = RichTextUploadingField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(default="+255", max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField(default="Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021", max_length=1000, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/FormTwo/")
    email = models.EmailField(blank=True, null=True)

    sub1 = models.CharField(default="Mathematics", max_length=200, blank=True, null=True)
    sub2 = models.CharField(default="English", max_length=200, blank=True, null=True)
    sub3 = models.CharField(default="Kiswahili", max_length=200, blank=True, null=True)
    sub4 = models.CharField(default="Physics", max_length=200, blank=True, null=True)
    sub5 = models.CharField(default="Biology", max_length=200, blank=True, null=True)
    

    sub1_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub2_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub3_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub4_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub5_marks = models.IntegerField(default= 100, blank=True, null=True)
    total_marks = models.IntegerField(default= 1000, blank=True, null=True)

    sub1_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub2_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub3_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub4_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub5_obtained = models.IntegerField(default= 80, blank=True, null=True)
    total_obtained = models.IntegerField(default= 800, blank=True, null=True)

    sub1_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub2_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub3_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub4_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub5_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    
    sub1_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub2_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub3_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub4_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub5_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)

    percentage = models.FloatField(blank=True, null=True)
    Overall_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    rank = models.CharField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=200, default= "Qualified", blank=True, null=True)
    stu_pos = models.IntegerField(blank=True, null=True)
    all_stu = models.IntegerField(blank=True, null=True)
    teacher_sign = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)




    #FORM THREE MODELS

    GENDER_CHOICES=(
    
    ('Male', 'Male'),
    ('Female', 'Female'),

    )    
        
class Form3Students(models.Model):
    darasa = models.ForeignKey(Darasa, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, blank=True, null=True)
    sname = models.CharField(max_length=200, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    year_of_study = models.CharField(max_length=200, blank=True, null=True)    
    
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/Form3Students/")
   # stu_class = models.CharField(default=name, max_length=200, blank=True, null=True)

    
    

# Create your models here.
class Form3Report(models.Model):
    title = RichTextUploadingField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(default="+255", max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField(default="Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021", max_length=1000, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/FormThree/")
    email = models.EmailField(blank=True, null=True)

    sub1 = models.CharField(default="Mathematics", max_length=200, blank=True, null=True)
    sub2 = models.CharField(default="English", max_length=200, blank=True, null=True)
    sub3 = models.CharField(default="Kiswahili", max_length=200, blank=True, null=True)
    sub4 = models.CharField(default="Physics", max_length=200, blank=True, null=True)
    sub5 = models.CharField(default="Biology", max_length=200, blank=True, null=True)
    

    sub1_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub2_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub3_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub4_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub5_marks = models.IntegerField(default= 100, blank=True, null=True)
    total_marks = models.IntegerField(default= 1000, blank=True, null=True)

    sub1_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub2_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub3_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub4_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub5_obtained = models.IntegerField(default= 80, blank=True, null=True)
    total_obtained = models.IntegerField(default= 800, blank=True, null=True)

    sub1_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub2_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub3_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub4_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub5_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    
    sub1_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub2_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub3_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub4_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub5_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)

    percentage = models.FloatField(blank=True, null=True)
    Overall_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    rank = models.CharField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=200, default= "Qualified", blank=True, null=True)
    stu_pos = models.IntegerField(blank=True, null=True)
    all_stu = models.IntegerField(blank=True, null=True)
    teacher_sign = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)



    #FORM FOUR MODELS

    GENDER_CHOICES=(
    
    ('Male', 'Male'),
    ('Female', 'Female'),

    )    
        
class Form4Students(models.Model):
    darasa = models.ForeignKey(Darasa, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, blank=True, null=True)
    sname = models.CharField(max_length=200, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    year_of_study = models.CharField(max_length=200, blank=True, null=True)    
    
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/Form4Students/")
   # stu_class = models.CharField(default=name, max_length=200, blank=True, null=True)

    
    

# Create your models here.
class Form4Report(models.Model):
    title = RichTextUploadingField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(default="+255", max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField(default="Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021", max_length=1000, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/FormFour/")
    email = models.EmailField(blank=True, null=True)

    sub1 = models.CharField(default="Mathematics", max_length=200, blank=True, null=True)
    sub2 = models.CharField(default="English", max_length=200, blank=True, null=True)
    sub3 = models.CharField(default="Kiswahili", max_length=200, blank=True, null=True)
    sub4 = models.CharField(default="Physics", max_length=200, blank=True, null=True)
    sub5 = models.CharField(default="Biology", max_length=200, blank=True, null=True)
    

    sub1_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub2_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub3_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub4_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub5_marks = models.IntegerField(default= 100, blank=True, null=True)
    total_marks = models.IntegerField(default= 1000, blank=True, null=True)

    sub1_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub2_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub3_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub4_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub5_obtained = models.IntegerField(default= 80, blank=True, null=True)
    total_obtained = models.IntegerField(default= 800, blank=True, null=True)

    sub1_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub2_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub3_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub4_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub5_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    
    sub1_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub2_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub3_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub4_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub5_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)

    percentage = models.FloatField(blank=True, null=True)
    Overall_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    rank = models.CharField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=200, default= "Qualified", blank=True, null=True)
    stu_pos = models.IntegerField(blank=True, null=True)
    all_stu = models.IntegerField(blank=True, null=True)
    teacher_sign = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)



    #FORM FIVE MODELS

    GENDER_CHOICES=(
    
    ('Male', 'Male'),
    ('Female', 'Female'),

    )    
        
class Form5Students(models.Model):
    darasa = models.ForeignKey(Darasa, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, blank=True, null=True)
    sname = models.CharField(max_length=200, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    year_of_study = models.CharField(max_length=200, blank=True, null=True)    
    
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/Form5Students/")
   # stu_class = models.CharField(default=name, max_length=200, blank=True, null=True)

    
    

# Create your models here.
class Form5Report(models.Model):
    title = RichTextUploadingField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(default="+255", max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField(default="Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021", max_length=1000, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/FormFive/")
    email = models.EmailField(blank=True, null=True)

    sub1 = models.CharField(default="Mathematics", max_length=200, blank=True, null=True)
    sub2 = models.CharField(default="English", max_length=200, blank=True, null=True)
    sub3 = models.CharField(default="Kiswahili", max_length=200, blank=True, null=True)
    sub4 = models.CharField(default="Physics", max_length=200, blank=True, null=True)
    sub5 = models.CharField(default="Biology", max_length=200, blank=True, null=True)
    

    sub1_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub2_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub3_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub4_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub5_marks = models.IntegerField(default= 100, blank=True, null=True)
    total_marks = models.IntegerField(default= 1000, blank=True, null=True)

    sub1_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub2_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub3_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub4_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub5_obtained = models.IntegerField(default= 80, blank=True, null=True)
    total_obtained = models.IntegerField(default= 800, blank=True, null=True)

    sub1_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub2_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub3_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub4_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub5_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    
    sub1_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub2_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub3_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub4_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub5_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)

    percentage = models.FloatField(blank=True, null=True)
    Overall_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    rank = models.CharField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=200, default= "Qualified", blank=True, null=True)
    stu_pos = models.IntegerField(blank=True, null=True)
    all_stu = models.IntegerField(blank=True, null=True)
    teacher_sign = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)



    #FORM SIX MODELS

    GENDER_CHOICES=(
    
    ('Male', 'Male'),
    ('Female', 'Female'),

    )    
        
class Form6Students(models.Model):
    darasa = models.ForeignKey(Darasa, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, blank=True, null=True)
    sname = models.CharField(max_length=200, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    year_of_study = models.CharField(max_length=200, blank=True, null=True)    
    
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/Form6Students/")
   # stu_class = models.CharField(default=name, max_length=200, blank=True, null=True)

    
    

# Create your models here.
class Form6Report(models.Model):
    title = RichTextUploadingField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(default="+255", max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField(default="Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021", max_length=1000, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/FormSix/")
    email = models.EmailField(blank=True, null=True)

    sub1 = models.CharField(default="Mathematics", max_length=200, blank=True, null=True)
    sub2 = models.CharField(default="English", max_length=200, blank=True, null=True)
    sub3 = models.CharField(default="Kiswahili", max_length=200, blank=True, null=True)
    sub4 = models.CharField(default="Physics", max_length=200, blank=True, null=True)
    sub5 = models.CharField(default="Biology", max_length=200, blank=True, null=True)
    

    sub1_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub2_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub3_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub4_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub5_marks = models.IntegerField(default= 100, blank=True, null=True)
    total_marks = models.IntegerField(default= 1000, blank=True, null=True)

    sub1_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub2_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub3_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub4_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub5_obtained = models.IntegerField(default= 80, blank=True, null=True)
    total_obtained = models.IntegerField(default= 800, blank=True, null=True)

    sub1_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub2_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub3_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub4_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub5_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    
    sub1_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub2_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub3_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub4_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub5_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)

    percentage = models.FloatField(blank=True, null=True)
    Overall_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    rank = models.CharField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=200, default= "Qualified", blank=True, null=True)
    stu_pos = models.IntegerField(blank=True, null=True)
    all_stu = models.IntegerField(blank=True, null=True)
    teacher_sign = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)



#PCM FORM 5 MODELS

GENDER_CHOICES=(
    
    ('Male', 'Male'),
    ('Female', 'Female'),

    )    
        
class PcmForm5Students(models.Model):
    darasa = models.ForeignKey(Combination, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, blank=True, null=True)
    sname = models.CharField(max_length=200, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    year_of_study = models.CharField(max_length=200, blank=True, null=True)    
    
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/PcmForm5Students/")
   # stu_class = models.CharField(default=name, max_length=200, blank=True, null=True)

    
    

# Create your models here.
class PcmForm5Report(models.Model):
    title = RichTextUploadingField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(default="+255", max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField(default="Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021", max_length=1000, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/PcmFormFive/")
    email = models.EmailField(blank=True, null=True)

    sub1 = models.CharField(default="Mathematics", max_length=200, blank=True, null=True)
    sub2 = models.CharField(default="English", max_length=200, blank=True, null=True)
    sub3 = models.CharField(default="Kiswahili", max_length=200, blank=True, null=True)
    sub4 = models.CharField(default="Physics", max_length=200, blank=True, null=True)
    sub5 = models.CharField(default="Biology", max_length=200, blank=True, null=True)
    

    sub1_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub2_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub3_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub4_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub5_marks = models.IntegerField(default= 100, blank=True, null=True)
    total_marks = models.IntegerField(default= 1000, blank=True, null=True)

    sub1_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub2_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub3_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub4_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub5_obtained = models.IntegerField(default= 80, blank=True, null=True)
    total_obtained = models.IntegerField(default= 800, blank=True, null=True)

    sub1_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub2_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub3_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub4_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub5_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    
    sub1_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub2_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub3_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub4_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub5_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)

    percentage = models.FloatField(blank=True, null=True)
    Overall_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    rank = models.CharField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=200, default= "Qualified", blank=True, null=True)
    stu_pos = models.IntegerField(blank=True, null=True)
    all_stu = models.IntegerField(blank=True, null=True)
    teacher_sign = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)



    #PCB FORM 5 MODELS


GENDER_CHOICES=(
    
    ('Male', 'Male'),
    ('Female', 'Female'),

    )    
        
class PcbForm5Students(models.Model):
    darasa = models.ForeignKey(Combination, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, blank=True, null=True)
    sname = models.CharField(max_length=200, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    year_of_study = models.CharField(max_length=200, blank=True, null=True)    
    
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/PcbForm5Students/")
   # stu_class = models.CharField(default=name, max_length=200, blank=True, null=True)

    
    

# Create your models here.
class PcbForm5Report(models.Model):
    title = RichTextUploadingField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(default="+255", max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField(default="Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021", max_length=1000, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/PcbFormFive/")
    email = models.EmailField(blank=True, null=True)

    sub1 = models.CharField(default="Mathematics", max_length=200, blank=True, null=True)
    sub2 = models.CharField(default="English", max_length=200, blank=True, null=True)
    sub3 = models.CharField(default="Kiswahili", max_length=200, blank=True, null=True)
    sub4 = models.CharField(default="Physics", max_length=200, blank=True, null=True)
    sub5 = models.CharField(default="Biology", max_length=200, blank=True, null=True)
    

    sub1_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub2_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub3_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub4_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub5_marks = models.IntegerField(default= 100, blank=True, null=True)
    total_marks = models.IntegerField(default= 1000, blank=True, null=True)

    sub1_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub2_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub3_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub4_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub5_obtained = models.IntegerField(default= 80, blank=True, null=True)
    total_obtained = models.IntegerField(default= 800, blank=True, null=True)

    sub1_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub2_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub3_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub4_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub5_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    
    sub1_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub2_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub3_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub4_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub5_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)

    percentage = models.FloatField(blank=True, null=True)
    Overall_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    rank = models.CharField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=200, default= "Qualified", blank=True, null=True)
    stu_pos = models.IntegerField(blank=True, null=True)
    all_stu = models.IntegerField(blank=True, null=True)
    teacher_sign = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)



    #PGM FORM 5 MODELS

GENDER_CHOICES=(
    
    ('Male', 'Male'),
    ('Female', 'Female'),

    )    
        
class PgmForm5Students(models.Model):
    darasa = models.ForeignKey(Combination, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, blank=True, null=True)
    sname = models.CharField(max_length=200, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    year_of_study = models.CharField(max_length=200, blank=True, null=True)    
    
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/PgmForm5Students/")
   # stu_class = models.CharField(default=name, max_length=200, blank=True, null=True)

    
    

# Create your models here.
class PgmForm5Report(models.Model):
    title = RichTextUploadingField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(default="+255", max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField(default="Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021", max_length=1000, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/PgmFormFive/")
    email = models.EmailField(blank=True, null=True)

    sub1 = models.CharField(default="Mathematics", max_length=200, blank=True, null=True)
    sub2 = models.CharField(default="English", max_length=200, blank=True, null=True)
    sub3 = models.CharField(default="Kiswahili", max_length=200, blank=True, null=True)
    sub4 = models.CharField(default="Physics", max_length=200, blank=True, null=True)
    sub5 = models.CharField(default="Biology", max_length=200, blank=True, null=True)
    

    sub1_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub2_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub3_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub4_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub5_marks = models.IntegerField(default= 100, blank=True, null=True)
    total_marks = models.IntegerField(default= 1000, blank=True, null=True)

    sub1_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub2_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub3_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub4_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub5_obtained = models.IntegerField(default= 80, blank=True, null=True)
    total_obtained = models.IntegerField(default= 800, blank=True, null=True)

    sub1_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub2_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub3_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub4_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub5_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    
    sub1_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub2_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub3_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub4_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub5_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)

    percentage = models.FloatField(blank=True, null=True)
    Overall_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    rank = models.CharField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=200, default= "Qualified", blank=True, null=True)
    stu_pos = models.IntegerField(blank=True, null=True)
    all_stu = models.IntegerField(blank=True, null=True)
    teacher_sign = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)



    #HGL FORM 5 MODELS

    GENDER_CHOICES=(
    
    ('Male', 'Male'),
    ('Female', 'Female'),

    )    
        
class HglForm5Students(models.Model):
    darasa = models.ForeignKey(Combination, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, blank=True, null=True)
    sname = models.CharField(max_length=200, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    year_of_study = models.CharField(max_length=200, blank=True, null=True)    
    
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/HglForm5Students/")
   # stu_class = models.CharField(default=name, max_length=200, blank=True, null=True)

    
    

# Create your models here.
class HglForm5Report(models.Model):
    title = RichTextUploadingField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(default="+255", max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField(default="Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021", max_length=1000, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/HglFormFive/")
    email = models.EmailField(blank=True, null=True)

    sub1 = models.CharField(default="Mathematics", max_length=200, blank=True, null=True)
    sub2 = models.CharField(default="English", max_length=200, blank=True, null=True)
    sub3 = models.CharField(default="Kiswahili", max_length=200, blank=True, null=True)
    sub4 = models.CharField(default="Physics", max_length=200, blank=True, null=True)
    sub5 = models.CharField(default="Biology", max_length=200, blank=True, null=True)
    

    sub1_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub2_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub3_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub4_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub5_marks = models.IntegerField(default= 100, blank=True, null=True)
    total_marks = models.IntegerField(default= 1000, blank=True, null=True)

    sub1_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub2_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub3_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub4_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub5_obtained = models.IntegerField(default= 80, blank=True, null=True)
    total_obtained = models.IntegerField(default= 800, blank=True, null=True)

    sub1_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub2_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub3_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub4_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub5_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    
    sub1_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub2_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub3_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub4_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub5_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)

    percentage = models.FloatField(blank=True, null=True)
    Overall_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    rank = models.CharField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=200, default= "Qualified", blank=True, null=True)
    stu_pos = models.IntegerField(blank=True, null=True)
    all_stu = models.IntegerField(blank=True, null=True)
    teacher_sign = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)



#HGK FORM 5 MODEL
GENDER_CHOICES=(
    
    ('Male', 'Male'),
    ('Female', 'Female'),

    )    
        
class HgkForm5Students(models.Model):
    darasa = models.ForeignKey(Combination, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, blank=True, null=True)
    sname = models.CharField(max_length=200, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    year_of_study = models.CharField(max_length=200, blank=True, null=True)    
    
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/HgkForm5Students/")
   # stu_class = models.CharField(default=name, max_length=200, blank=True, null=True)

    
    

# Create your models here.
class HgkForm5Report(models.Model):
    title = RichTextUploadingField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(default="+255", max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField(default="Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021", max_length=1000, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/HgkFormFive/")
    email = models.EmailField(blank=True, null=True)

    sub1 = models.CharField(default="Mathematics", max_length=200, blank=True, null=True)
    sub2 = models.CharField(default="English", max_length=200, blank=True, null=True)
    sub3 = models.CharField(default="Kiswahili", max_length=200, blank=True, null=True)
    sub4 = models.CharField(default="Physics", max_length=200, blank=True, null=True)
    sub5 = models.CharField(default="Biology", max_length=200, blank=True, null=True)
    

    sub1_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub2_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub3_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub4_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub5_marks = models.IntegerField(default= 100, blank=True, null=True)
    total_marks = models.IntegerField(default= 1000, blank=True, null=True)

    sub1_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub2_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub3_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub4_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub5_obtained = models.IntegerField(default= 80, blank=True, null=True)
    total_obtained = models.IntegerField(default= 800, blank=True, null=True)

    sub1_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub2_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub3_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub4_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub5_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    
    sub1_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub2_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub3_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub4_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub5_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)

    percentage = models.FloatField(blank=True, null=True)
    Overall_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    rank = models.CharField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=200, default= "Qualified", blank=True, null=True)
    stu_pos = models.IntegerField(blank=True, null=True)
    all_stu = models.IntegerField(blank=True, null=True)
    teacher_sign = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)



# CBG FORM 5 MODEL
GENDER_CHOICES=(
    
    ('Male', 'Male'),
    ('Female', 'Female'),

    )    
        
class CbgForm5Students(models.Model):
    darasa = models.ForeignKey(Combination, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, blank=True, null=True)
    sname = models.CharField(max_length=200, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    year_of_study = models.CharField(max_length=200, blank=True, null=True)    
    
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/CbgForm5Students/")
   # stu_class = models.CharField(default=name, max_length=200, blank=True, null=True)

    
    

# Create your models here.
class CbgForm5Report(models.Model):
    title = RichTextUploadingField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(default="+255", max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField(default="Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021", max_length=1000, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/CbgFormFive/")
    email = models.EmailField(blank=True, null=True)

    sub1 = models.CharField(default="Mathematics", max_length=200, blank=True, null=True)
    sub2 = models.CharField(default="English", max_length=200, blank=True, null=True)
    sub3 = models.CharField(default="Kiswahili", max_length=200, blank=True, null=True)
    sub4 = models.CharField(default="Physics", max_length=200, blank=True, null=True)
    sub5 = models.CharField(default="Biology", max_length=200, blank=True, null=True)
    

    sub1_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub2_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub3_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub4_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub5_marks = models.IntegerField(default= 100, blank=True, null=True)
    total_marks = models.IntegerField(default= 1000, blank=True, null=True)

    sub1_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub2_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub3_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub4_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub5_obtained = models.IntegerField(default= 80, blank=True, null=True)
    total_obtained = models.IntegerField(default= 800, blank=True, null=True)

    sub1_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub2_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub3_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub4_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub5_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    
    sub1_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub2_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub3_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub4_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub5_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)

    percentage = models.FloatField(blank=True, null=True)
    Overall_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    rank = models.CharField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=200, default= "Qualified", blank=True, null=True)
    stu_pos = models.IntegerField(blank=True, null=True)
    all_stu = models.IntegerField(blank=True, null=True)
    teacher_sign = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)


#HKL FORM 5 MODEL
GENDER_CHOICES=(
    
    ('Male', 'Male'),
    ('Female', 'Female'),

    )    
        
class HklForm5Students(models.Model):
    darasa = models.ForeignKey(Combination, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, blank=True, null=True)
    sname = models.CharField(max_length=200, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    year_of_study = models.CharField(max_length=200, blank=True, null=True)    
    
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/HklForm5Students/")
   # stu_class = models.CharField(default=name, max_length=200, blank=True, null=True)

    
    

# Create your models here.
class HklForm5Report(models.Model):
    title = RichTextUploadingField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(default="+255", max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField(default="Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021", max_length=1000, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/HklFormFive/")
    email = models.EmailField(blank=True, null=True)

    sub1 = models.CharField(default="Mathematics", max_length=200, blank=True, null=True)
    sub2 = models.CharField(default="English", max_length=200, blank=True, null=True)
    sub3 = models.CharField(default="Kiswahili", max_length=200, blank=True, null=True)
    sub4 = models.CharField(default="Physics", max_length=200, blank=True, null=True)
    sub5 = models.CharField(default="Biology", max_length=200, blank=True, null=True)
    

    sub1_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub2_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub3_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub4_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub5_marks = models.IntegerField(default= 100, blank=True, null=True)
    total_marks = models.IntegerField(default= 1000, blank=True, null=True)

    sub1_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub2_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub3_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub4_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub5_obtained = models.IntegerField(default= 80, blank=True, null=True)
    total_obtained = models.IntegerField(default= 800, blank=True, null=True)

    sub1_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub2_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub3_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub4_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub5_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    
    sub1_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub2_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub3_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub4_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub5_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)

    percentage = models.FloatField(blank=True, null=True)
    Overall_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    rank = models.CharField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=200, default= "Qualified", blank=True, null=True)
    stu_pos = models.IntegerField(blank=True, null=True)
    all_stu = models.IntegerField(blank=True, null=True)
    teacher_sign = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)


#ECA FORM 5 MODEL
GENDER_CHOICES=(
    
    ('Male', 'Male'),
    ('Female', 'Female'),

    )    
        
class EcaForm5Students(models.Model):
    darasa = models.ForeignKey(Combination, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, blank=True, null=True)
    sname = models.CharField(max_length=200, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    year_of_study = models.CharField(max_length=200, blank=True, null=True)    
    
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/EcaForm5Students/")
   # stu_class = models.CharField(default=name, max_length=200, blank=True, null=True)

    
    

# Create your models here.
class EcaForm5Report(models.Model):
    title = RichTextUploadingField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(default="+255", max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField(default="Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021", max_length=1000, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/EcaFormFive/")
    email = models.EmailField(blank=True, null=True)

    sub1 = models.CharField(default="Mathematics", max_length=200, blank=True, null=True)
    sub2 = models.CharField(default="English", max_length=200, blank=True, null=True)
    sub3 = models.CharField(default="Kiswahili", max_length=200, blank=True, null=True)
    sub4 = models.CharField(default="Physics", max_length=200, blank=True, null=True)
    sub5 = models.CharField(default="Biology", max_length=200, blank=True, null=True)
    

    sub1_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub2_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub3_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub4_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub5_marks = models.IntegerField(default= 100, blank=True, null=True)
    total_marks = models.IntegerField(default= 1000, blank=True, null=True)

    sub1_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub2_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub3_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub4_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub5_obtained = models.IntegerField(default= 80, blank=True, null=True)
    total_obtained = models.IntegerField(default= 800, blank=True, null=True)

    sub1_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub2_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub3_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub4_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub5_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    
    sub1_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub2_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub3_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub4_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub5_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)

    percentage = models.FloatField(blank=True, null=True)
    Overall_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    rank = models.CharField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=200, default= "Qualified", blank=True, null=True)
    stu_pos = models.IntegerField(blank=True, null=True)
    all_stu = models.IntegerField(blank=True, null=True)
    teacher_sign = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)













#FORM SIX FORM 6 FORM 6 FORM 6 ZINAANZIA APA


#PCM FORM 6 MODELS

GENDER_CHOICES=(
    
    ('Male', 'Male'),
    ('Female', 'Female'),

    )    
        
class PcmForm6Students(models.Model):
    darasa = models.ForeignKey(Combination, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, blank=True, null=True)
    sname = models.CharField(max_length=200, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    year_of_study = models.CharField(max_length=200, blank=True, null=True)    
    
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/PcmForm6Students/")
   # stu_class = models.CharField(default=name, max_length=200, blank=True, null=True)

    
    

# Create your models here.
class PcmForm6Report(models.Model):
    title = RichTextUploadingField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(default="+255", max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField(default="Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021", max_length=1000, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/PcmFormSix/")
    email = models.EmailField(blank=True, null=True)

    sub1 = models.CharField(default="Mathematics", max_length=200, blank=True, null=True)
    sub2 = models.CharField(default="English", max_length=200, blank=True, null=True)
    sub3 = models.CharField(default="Kiswahili", max_length=200, blank=True, null=True)
    sub4 = models.CharField(default="Physics", max_length=200, blank=True, null=True)
    sub5 = models.CharField(default="Biology", max_length=200, blank=True, null=True)
    

    sub1_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub2_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub3_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub4_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub5_marks = models.IntegerField(default= 100, blank=True, null=True)
    total_marks = models.IntegerField(default= 1000, blank=True, null=True)

    sub1_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub2_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub3_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub4_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub5_obtained = models.IntegerField(default= 80, blank=True, null=True)
    total_obtained = models.IntegerField(default= 800, blank=True, null=True)

    sub1_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub2_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub3_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub4_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub5_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    
    sub1_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub2_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub3_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub4_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub5_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)

    percentage = models.FloatField(blank=True, null=True)
    Overall_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    rank = models.CharField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=200, default= "Qualified", blank=True, null=True)
    stu_pos = models.IntegerField(blank=True, null=True)
    all_stu = models.IntegerField(blank=True, null=True)
    teacher_sign = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)



    #PCB FORM 6 MODELS


GENDER_CHOICES=(
    
    ('Male', 'Male'),
    ('Female', 'Female'),

    )    
        
class PcbForm6Students(models.Model):
    darasa = models.ForeignKey(Combination, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, blank=True, null=True)
    sname = models.CharField(max_length=200, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    year_of_study = models.CharField(max_length=200, blank=True, null=True)    
    
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/PcbForm6Students/")
   # stu_class = models.CharField(default=name, max_length=200, blank=True, null=True)

    
    

# Create your models here.
class PcbForm6Report(models.Model):
    title = RichTextUploadingField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(default="+255", max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField(default="Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021", max_length=1000, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/PcbFormSix/")
    email = models.EmailField(blank=True, null=True)

    sub1 = models.CharField(default="Mathematics", max_length=200, blank=True, null=True)
    sub2 = models.CharField(default="English", max_length=200, blank=True, null=True)
    sub3 = models.CharField(default="Kiswahili", max_length=200, blank=True, null=True)
    sub4 = models.CharField(default="Physics", max_length=200, blank=True, null=True)
    sub5 = models.CharField(default="Biology", max_length=200, blank=True, null=True)
    

    sub1_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub2_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub3_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub4_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub5_marks = models.IntegerField(default= 100, blank=True, null=True)
    total_marks = models.IntegerField(default= 1000, blank=True, null=True)

    sub1_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub2_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub3_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub4_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub5_obtained = models.IntegerField(default= 80, blank=True, null=True)
    total_obtained = models.IntegerField(default= 800, blank=True, null=True)

    sub1_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub2_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub3_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub4_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub5_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    
    sub1_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub2_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub3_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub4_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub5_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)

    percentage = models.FloatField(blank=True, null=True)
    Overall_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    rank = models.CharField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=200, default= "Qualified", blank=True, null=True)
    stu_pos = models.IntegerField(blank=True, null=True)
    all_stu = models.IntegerField(blank=True, null=True)
    teacher_sign = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)



    #PGM FORM 6 MODELS

GENDER_CHOICES=(
    
    ('Male', 'Male'),
    ('Female', 'Female'),

    )    
        
class PgmForm6Students(models.Model):
    darasa = models.ForeignKey(Combination, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, blank=True, null=True)
    sname = models.CharField(max_length=200, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    year_of_study = models.CharField(max_length=200, blank=True, null=True)    
    
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/PgmForm6Students/")
   # stu_class = models.CharField(default=name, max_length=200, blank=True, null=True)

    
    

# Create your models here.
class PgmForm6Report(models.Model):
    title = RichTextUploadingField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(default="+255", max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField(default="Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021", max_length=1000, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/PgmFormSix/")
    email = models.EmailField(blank=True, null=True)

    sub1 = models.CharField(default="Mathematics", max_length=200, blank=True, null=True)
    sub2 = models.CharField(default="English", max_length=200, blank=True, null=True)
    sub3 = models.CharField(default="Kiswahili", max_length=200, blank=True, null=True)
    sub4 = models.CharField(default="Physics", max_length=200, blank=True, null=True)
    sub5 = models.CharField(default="Biology", max_length=200, blank=True, null=True)
    

    sub1_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub2_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub3_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub4_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub5_marks = models.IntegerField(default= 100, blank=True, null=True)
    total_marks = models.IntegerField(default= 1000, blank=True, null=True)

    sub1_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub2_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub3_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub4_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub5_obtained = models.IntegerField(default= 80, blank=True, null=True)
    total_obtained = models.IntegerField(default= 800, blank=True, null=True)

    sub1_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub2_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub3_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub4_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub5_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    
    sub1_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub2_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub3_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub4_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub5_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)

    percentage = models.FloatField(blank=True, null=True)
    Overall_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    rank = models.CharField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=200, default= "Qualified", blank=True, null=True)
    stu_pos = models.IntegerField(blank=True, null=True)
    all_stu = models.IntegerField(blank=True, null=True)
    teacher_sign = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)



    #HGL FORM 6 MODELS

    GENDER_CHOICES=(
    
    ('Male', 'Male'),
    ('Female', 'Female'),

    )    
        
class HglForm6Students(models.Model):
    darasa = models.ForeignKey(Combination, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, blank=True, null=True)
    sname = models.CharField(max_length=200, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    year_of_study = models.CharField(max_length=200, blank=True, null=True)    
    
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/HglForm6Students/")
   # stu_class = models.CharField(default=name, max_length=200, blank=True, null=True)

    
    

# Create your models here.
class HglForm6Report(models.Model):
    title = RichTextUploadingField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(default="+255", max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField(default="Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021", max_length=1000, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/HglFormSix/")
    email = models.EmailField(blank=True, null=True)

    sub1 = models.CharField(default="Mathematics", max_length=200, blank=True, null=True)
    sub2 = models.CharField(default="English", max_length=200, blank=True, null=True)
    sub3 = models.CharField(default="Kiswahili", max_length=200, blank=True, null=True)
    sub4 = models.CharField(default="Physics", max_length=200, blank=True, null=True)
    sub5 = models.CharField(default="Biology", max_length=200, blank=True, null=True)
    

    sub1_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub2_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub3_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub4_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub5_marks = models.IntegerField(default= 100, blank=True, null=True)
    total_marks = models.IntegerField(default= 1000, blank=True, null=True)

    sub1_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub2_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub3_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub4_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub5_obtained = models.IntegerField(default= 80, blank=True, null=True)
    total_obtained = models.IntegerField(default= 800, blank=True, null=True)

    sub1_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub2_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub3_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub4_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub5_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    
    sub1_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub2_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub3_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub4_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub5_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)

    percentage = models.FloatField(blank=True, null=True)
    Overall_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    rank = models.CharField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=200, default= "Qualified", blank=True, null=True)
    stu_pos = models.IntegerField(blank=True, null=True)
    all_stu = models.IntegerField(blank=True, null=True)
    teacher_sign = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)



#HGK FORM 6 MODEL
GENDER_CHOICES=(
    
    ('Male', 'Male'),
    ('Female', 'Female'),

    )    
        
class HgkForm6Students(models.Model):
    darasa = models.ForeignKey(Combination, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, blank=True, null=True)
    sname = models.CharField(max_length=200, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    year_of_study = models.CharField(max_length=200, blank=True, null=True)    
    
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/HgkForm6Students/")
   # stu_class = models.CharField(default=name, max_length=200, blank=True, null=True)

    
    

# Create your models here.
class HgkForm6Report(models.Model):
    title = RichTextUploadingField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(default="+255", max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField(default="Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021", max_length=1000, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/HgkFormSix/")
    email = models.EmailField(blank=True, null=True)

    sub1 = models.CharField(default="Mathematics", max_length=200, blank=True, null=True)
    sub2 = models.CharField(default="English", max_length=200, blank=True, null=True)
    sub3 = models.CharField(default="Kiswahili", max_length=200, blank=True, null=True)
    sub4 = models.CharField(default="Physics", max_length=200, blank=True, null=True)
    sub5 = models.CharField(default="Biology", max_length=200, blank=True, null=True)
    

    sub1_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub2_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub3_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub4_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub5_marks = models.IntegerField(default= 100, blank=True, null=True)
    total_marks = models.IntegerField(default= 1000, blank=True, null=True)

    sub1_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub2_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub3_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub4_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub5_obtained = models.IntegerField(default= 80, blank=True, null=True)
    total_obtained = models.IntegerField(default= 800, blank=True, null=True)

    sub1_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub2_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub3_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub4_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub5_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    
    sub1_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub2_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub3_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub4_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub5_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)

    percentage = models.FloatField(blank=True, null=True)
    Overall_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    rank = models.CharField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=200, default= "Qualified", blank=True, null=True)
    stu_pos = models.IntegerField(blank=True, null=True)
    all_stu = models.IntegerField(blank=True, null=True)
    teacher_sign = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)



# CBG FORM 6 MODEL
GENDER_CHOICES=(
    
    ('Male', 'Male'),
    ('Female', 'Female'),

    )    
        
class CbgForm6Students(models.Model):
    darasa = models.ForeignKey(Combination, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, blank=True, null=True)
    sname = models.CharField(max_length=200, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    year_of_study = models.CharField(max_length=200, blank=True, null=True)    
    
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/CbgForm6Students/")
   # stu_class = models.CharField(default=name, max_length=200, blank=True, null=True)

    
    

# Create your models here.
class CbgForm6Report(models.Model):
    title = RichTextUploadingField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(default="+255", max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField(default="Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021", max_length=1000, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/CbgFormSix/")
    email = models.EmailField(blank=True, null=True)

    sub1 = models.CharField(default="Mathematics", max_length=200, blank=True, null=True)
    sub2 = models.CharField(default="English", max_length=200, blank=True, null=True)
    sub3 = models.CharField(default="Kiswahili", max_length=200, blank=True, null=True)
    sub4 = models.CharField(default="Physics", max_length=200, blank=True, null=True)
    sub5 = models.CharField(default="Biology", max_length=200, blank=True, null=True)
    

    sub1_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub2_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub3_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub4_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub5_marks = models.IntegerField(default= 100, blank=True, null=True)
    total_marks = models.IntegerField(default= 1000, blank=True, null=True)

    sub1_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub2_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub3_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub4_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub5_obtained = models.IntegerField(default= 80, blank=True, null=True)
    total_obtained = models.IntegerField(default= 800, blank=True, null=True)

    sub1_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub2_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub3_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub4_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub5_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    
    sub1_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub2_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub3_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub4_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub5_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)

    percentage = models.FloatField(blank=True, null=True)
    Overall_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    rank = models.CharField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=200, default= "Qualified", blank=True, null=True)
    stu_pos = models.IntegerField(blank=True, null=True)
    all_stu = models.IntegerField(blank=True, null=True)
    teacher_sign = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)


#HKL FORM 6 MODEL
GENDER_CHOICES=(
    
    ('Male', 'Male'),
    ('Female', 'Female'),

    )    
        
class HklForm6Students(models.Model):
    darasa = models.ForeignKey(Combination, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, blank=True, null=True)
    sname = models.CharField(max_length=200, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    year_of_study = models.CharField(max_length=200, blank=True, null=True)    
    
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/HklForm6Students/")
   # stu_class = models.CharField(default=name, max_length=200, blank=True, null=True)

    
    

# Create your models here.
class HklForm6Report(models.Model):
    title = RichTextUploadingField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(default="+255", max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField(default="Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021", max_length=1000, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/HklFormSix/")
    email = models.EmailField(blank=True, null=True)

    sub1 = models.CharField(default="Mathematics", max_length=200, blank=True, null=True)
    sub2 = models.CharField(default="English", max_length=200, blank=True, null=True)
    sub3 = models.CharField(default="Kiswahili", max_length=200, blank=True, null=True)
    sub4 = models.CharField(default="Physics", max_length=200, blank=True, null=True)
    sub5 = models.CharField(default="Biology", max_length=200, blank=True, null=True)
    

    sub1_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub2_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub3_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub4_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub5_marks = models.IntegerField(default= 100, blank=True, null=True)
    total_marks = models.IntegerField(default= 1000, blank=True, null=True)

    sub1_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub2_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub3_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub4_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub5_obtained = models.IntegerField(default= 80, blank=True, null=True)
    total_obtained = models.IntegerField(default= 800, blank=True, null=True)

    sub1_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub2_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub3_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub4_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub5_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    
    sub1_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub2_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub3_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub4_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub5_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)

    percentage = models.FloatField(blank=True, null=True)
    Overall_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    rank = models.CharField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=200, default= "Qualified", blank=True, null=True)
    stu_pos = models.IntegerField(blank=True, null=True)
    all_stu = models.IntegerField(blank=True, null=True)
    teacher_sign = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)


#ECA FORM 6 MODEL
GENDER_CHOICES=(
    
    ('Male', 'Male'),
    ('Female', 'Female'),

    )    
        
class EcaForm6Students(models.Model):
    darasa = models.ForeignKey(Combination, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, blank=True, null=True)
    sname = models.CharField(max_length=200, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    year_of_study = models.CharField(max_length=200, blank=True, null=True)    
    
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/EcaForm6Students/")
   # stu_class = models.CharField(default=name, max_length=200, blank=True, null=True)

    
    

# Create your models here.
class EcaForm6Report(models.Model):
    title = RichTextUploadingField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(default="+255", max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.TextField(default="Cecilia Charles ameshika nafasi ya 10 kati ya wanafunzi 225 darasani katika mitihani ya kufunga muhula wa 1 wa masomo kwa mwaka 2020-2021", max_length=1000, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/EcaFormSix/")
    email = models.EmailField(blank=True, null=True)

    sub1 = models.CharField(default="Mathematics", max_length=200, blank=True, null=True)
    sub2 = models.CharField(default="English", max_length=200, blank=True, null=True)
    sub3 = models.CharField(default="Kiswahili", max_length=200, blank=True, null=True)
    sub4 = models.CharField(default="Physics", max_length=200, blank=True, null=True)
    sub5 = models.CharField(default="Biology", max_length=200, blank=True, null=True)
    

    sub1_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub2_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub3_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub4_marks = models.IntegerField(default= 100, blank=True, null=True)
    sub5_marks = models.IntegerField(default= 100, blank=True, null=True)
    total_marks = models.IntegerField(default= 1000, blank=True, null=True)

    sub1_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub2_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub3_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub4_obtained = models.IntegerField(default= 80, blank=True, null=True)
    sub5_obtained = models.IntegerField(default= 80, blank=True, null=True)
    total_obtained = models.IntegerField(default= 800, blank=True, null=True)

    sub1_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub2_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub3_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub4_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    sub5_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    
    sub1_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub2_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub3_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub4_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)
    sub5_remaks = models.CharField(max_length=200, default= "Very Good", blank=True, null=True)

    percentage = models.FloatField(blank=True, null=True)
    Overall_grade = models.CharField(max_length=200, default= "A", blank=True, null=True)
    rank = models.CharField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=200, default= "Qualified", blank=True, null=True)
    stu_pos = models.IntegerField(blank=True, null=True)
    all_stu = models.IntegerField(blank=True, null=True)
    teacher_sign = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=200, blank=True, null=True)





















