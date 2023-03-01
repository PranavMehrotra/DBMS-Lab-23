import json
from django import forms
from django.db import transaction
from .models import *
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password, check_password
from django.forms.widgets import DateTimeInput

BLOOD_GROUP_CHOICES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
]


class DoctorSignUpForm(forms.ModelForm):#form and formfields defined
    
    Email_ID = forms.CharField(required=True)
    Employee_ID = forms.IntegerField(required=True)
    First_Name =forms.CharField(required=True,label="First Name")
    Last_Name =forms.CharField(required=True,label="Last Name")
    Position =forms.CharField(required=True)
    Department = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    class Meta(forms.ModelForm):#Model Meta is basically used to change the behavior of your model fields like changing order options,verbose_name and lot of other options.
        model = physician
        # Order of Fields in the Form
        fields = ['Email_ID','Employee_ID','First_Name','Last_Name','Position','Department', 'password']
    
    def clean_strings(self,*args,**kwargs):
        Email_ID =  self.cleaned_data.get('Email_ID')
        First_Name = self.cleaned_data.get('First_Name').upper()#get the data from form which would be stored in self.cleaned and store it in upper case
        Last_Name = self.cleaned_data.get('Last_Name').upper()
        Position = self.cleaned_data.get('Position').upper() #extract email from form
        Employee_ID = self.cleaned_data.get('Employee_ID')
        Department = self.cleaned_data.get('Department')
        # print(email)


    @transaction.atomic  #if an exception occurs changes are not saved
    def save(self):
        Email_ID =  self.cleaned_data.get('Email_ID')
        First_Name = self.cleaned_data.get('First_Name').upper()#get the data from form which would be stored in self.cleaned and store it in upper case
        Last_Name = self.cleaned_data.get('Last_Name').upper()
        Position = self.cleaned_data.get('Position').upper() #extract email from form
        Employee_ID = self.cleaned_data.get('Employee_ID')
        Department = self.cleaned_data.get('Department')
        password = make_password(self.cleaned_data.get('password'))
        
        doctor = physician(Email_ID=Email_ID, First_Name=First_Name,Last_Name = Last_Name,Position = Position, Employee_ID = Employee_ID, Department = Department, password=password)
        doctor.save()
        return doctor

class FrontSignUpForm(forms.ModelForm):#form and formfields defined
   
    Email_ID = models.EmailField()
    First_Name =forms.CharField(required=True, label="First Name")
    Last_Name =forms.CharField(required=True, label="Last Name")
    Employee_ID = forms.IntegerField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    

    class Meta(forms.ModelForm):#Model Meta is basically used to change the behavior of your model fields like changing order options,verbose_name and lot of other options.
        model = front_desk
        # Order of Fields in the Form
        fields = ['Email_ID','First_Name', 'Last_Name', 'Employee_ID', 'password']
    
    def clean_strings(self,*args,**kwargs):
        
        First_Name = self.cleaned_data.get('First_Name').upper()#get the data from form which would be stored in self.cleaned and store it in upper case
        Last_Name = self.cleaned_data.get('Last_Name').upper() #extract email from form
        Employee_ID = self.cleaned_data.get('Employee_ID')
        Email_ID = self.cleaned_data.get('Email_ID')
        
        # print(email)


    @transaction.atomic  #if an exception occurs changes are not saved
    def save(self):

        First_Name = self.cleaned_data.get('First_Name').upper()#get the data from form which would be stored in self.cleaned and store it in upper case
        Last_Name = self.cleaned_data.get('Last_Name').upper() #extract email from form
        Employee_ID = self.cleaned_data.get('Employee_ID')
        Email_ID = self.cleaned_data.get('Email_ID')
        password = make_password(self.cleaned_data.get('password'))
        front = front_desk(First_Name=First_Name,Last_Name = Last_Name, Employee_ID = Employee_ID, password=password, Email_ID = Email_ID)
        front.save()
        return front
    
class DataSignUpForm(forms.ModelForm):#form and formfields defined
    
    Email_ID = models.EmailField()
    First_Name =forms.CharField(required=True, label="First Name")
    Last_Name =forms.CharField(required=True, label="Last Name")
    Employee_ID = forms.IntegerField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    

    class Meta(forms.ModelForm):#Model Meta is basically used to change the behavior of your model fields like changing order options,verbose_name and lot of other options.
        model = front_desk
        # Order of Fields in the Form
        fields = ['Email_ID','First_Name', 'Last_Name', 'Employee_ID', 'password']
    
    def clean_strings(self,*args,**kwargs):
        
        First_Name = self.cleaned_data.get('First_Name').upper()#get the data from form which would be stored in self.cleaned and store it in upper case
        Last_Name = self.cleaned_data.get('Last_Name').upper() #extract email from form
        Employee_ID = self.cleaned_data.get('Employee_ID')
        Email_ID = self.cleaned_data.get('Email_ID')
        
        # print(email)


    @transaction.atomic  #if an exception occurs changes are not saved
    def save(self):

        First_Name = self.cleaned_data.get('First_Name').upper()#get the data from form which would be stored in self.cleaned and store it in upper case
        Last_Name = self.cleaned_data.get('Last_Name').upper() #extract email from form
        Employee_ID = self.cleaned_data.get('Employee_ID')
        Email_ID = self.cleaned_data.get('Email_ID')
        password = make_password(self.cleaned_data.get('password'))
        data = data_entry(First_Name=First_Name,Last_Name = Last_Name, Employee_ID = Employee_ID, password=password, Email_ID = Email_ID)
        data.save()
        return data

class admit_pat(forms.ModelForm):
    
    First_Name = forms.CharField(max_length = 255,required=True)
    Last_Name = forms.CharField(max_length = 255,required=True)
    Room = forms.ChoiceField(choices=[])
    Start = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}))
    PCP_Name = forms.ChoiceField(choices=[])
    
    def get_pcp(self):
        # Retrieve the choices from the database or some other source
        # and return them as a list of tuples in the format (value, label)
        patient_list=[]
        doct = physician.objects.all()
        for x in doct:
            print(x.Email_ID) 
            patient_list.append((x.Email_ID,x.First_Name+" "+x.Last_Name))
        return patient_list
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Room'].choices = self.get_my_choices()
        self.fields['PCP_Name'].choices = self.get_pcp()

    def get_my_choices(self):
        # Retrieve the choices from the database or some other source
        # and return them as a list of tuples in the format (value, label)
        all_room=[]
        rooms = room.objects.all()
        for x in rooms: 
            if(x.Capacity>=1):
                all_room.append((x.Room_ID,x.Room_name+" "+str(x.Type)))
        if all_room == []:
                all_room.append((-1, "NO ROOM AVAILABLE"))
        return all_room
    
    class Meta():
        model = patient
        fields = ['First_Name','Last_Name', "Room", 'Start', "PCP_Name"]
        


    @transaction.atomic  #if an exception occurs changes are not saved
    def save(self):
        return self.cleaned_data.get('First_Name'),self.cleaned_data.get("Last_Name"),self.cleaned_data.get('Room'),self.cleaned_data.get('Start'), self.cleaned_data.get("PCP_Name")

class patient_register(forms.ModelForm):
    
    Email_ID = forms.CharField(max_length=255,required=True)   
    SSN = forms.IntegerField(required=True)
    First_Name = forms.CharField(max_length = 255,required=True)
    Last_Name = forms.CharField(max_length = 255,required=True)
    Address = forms.CharField(max_length = 255,required=True)
    Phone = forms.CharField(max_length = 255,required=True)
    Insurance_ID = forms.IntegerField(required=True)
    Age = forms.IntegerField(required=True)
    Blood_Group = forms.ChoiceField(choices = BLOOD_GROUP_CHOICES, label="Blood Group")
    
    class Meta():
        model = patient
        fields = ['Email_ID','SSN','First_Name','Last_Name','Address','Phone','Insurance_ID','Age', 'Blood_Group']


    @transaction.atomic  #if an exception occurs changes are not saved
    def save(self):
        return self.cleaned_data.get('Email_ID'),self.cleaned_data.get('SSN'),self.cleaned_data.get('First_Name'),self.cleaned_data.get('Last_Name'),self.cleaned_data.get('Address'),self.cleaned_data.get('Insurance_ID'),self.cleaned_data.get('Phone'),self.cleaned_data.get('Age'),self.cleaned_data.get('Blood_Group'),0
        
        # Phone = self.cleaned_data.get('Phone')
        # if len(Phone)==10 and Phone.isdigit():
        #     return self.cleaned_data.get('SSN'),self.cleaned_data.get('First_Name'),self.cleaned_data.get('Address'),self.cleaned_data.get('Phone'),self.cleaned_data.get('Insurance_ID'),self.cleaned_data.get('PCP'),0
        # else:   
            # raise forms.ValidationError(_("Invalid Number Format"),code='invalid_format')

# class AlumniSignUpForm(UserCreationForm):
#     first_name = forms.CharField(required=True) 
#     last_name = forms.CharField(required=True)
#     department = forms.ChoiceField(choices=Dep_choices)
#     roll_number =forms.CharField(required=True)
#     year_of_graduation = forms.IntegerField(required=True,min_value=1951,max_value=2021)

#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ['email','contact_number','roll_number','first_name','last_name','department','year_of_graduation']
    
#     @transaction.atomic#if an exception occurs changes are not saved
#     def save(self):
#         user = super().save(commit=False)#before saving save the details
#         user.is_alumni = True
#         user.first_name = self.cleaned_data.get('first_name')
#         user.last_name = self.cleaned_data.get('last_name')
#         user.contact_number=self.cleaned_data.get('contact_number')
#         user.email = self.cleaned_data.get('email')
#         user.username = user.email
#         user.save()
#         alumni = Alumni.objects.create(user=user)#instance created
#         alumni.department=self.cleaned_data.get('department')
#         alumni.roll_number=self.cleaned_data.get('roll_number').upper()
#         alumni.year_of_graduation=int(self.cleaned_data.get('year_of_graduation'))
#         alumni.save()
#         return user

# class AlumniEditForm(forms.ModelForm):
#     email = forms.EmailField(required=True)
#     contact_number = forms.CharField(max_length=12,required=True)
#     roll_number =forms.CharField(required=True)
#     first_name = forms.CharField(required=True) 
#     last_name = forms.CharField(required=True)
#     department = forms.CharField(required=True)
#     year_of_graduation = forms.IntegerField(required=True,min_value=1951,max_value=2021)

#     class Meta():
#         model = Alumni
#         fields = ['email','contact_number','first_name','last_name','department','year_of_graduation']

#     @transaction.atomic  #if an exception occurs changes are not saved
#     def save(self):
#         return self.cleaned_data.get('contact_number')

# class CompanySignUpForm(UserCreationForm):
#     email = forms.EmailField(label="Email (Email will be your username for Logging in the portal)")
#     contact_number = forms.CharField(max_length=12)
#     # first_name = forms.CharField(required=True) 
#     # last_name = forms.CharField(required=True)
#     profile = forms.CharField(required=True)
#     company_name =forms.CharField(required=True)
#     address = forms.CharField(required=True)
#     profile = forms.ChoiceField(choices=Profiles_choices)
#     # overview = forms.Textarea(attrs={"cols": "35", "rows": "10"})
#     # work_environ = forms.Textarea(attrs={"cols": "35", "rows": "10"})
#     # job_desc = forms.Textarea(attrs={"cols": "35", "rows": "10"})
#     # other_details = forms.Textarea(attrs={"cols": "35", "rows": "10"})
#     verify_doc = forms.FileField(label="Upload your Verification Documents(Single PDF)",required=False)

#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ['email','contact_number','company_name','address','profile'] 
    
#     @transaction.atomic#if an exception occurs changes are not saved
#     def save(self):
#         user = super().save(commit=False)#before saving save the details
#         user.is_company = True
#         user.contact_number=self.cleaned_data.get('contact_number')
#         user.email = self.cleaned_data.get('email')
#         user.username = user.email
#         user.save()
#         company = Company.objects.create(user=user)#instance created
#         company.profile=self.cleaned_data.get('profile')
#         company.company_name=self.cleaned_data.get('company_name')
#         company.address=self.cleaned_data.get('address')
#         company.verify_doc = self.cleaned_data.get('verify_doc')
#         company.save()
#         return user

# class CompanydescForm(forms.ModelForm):
#     overview = forms.Textarea(attrs={"cols": "35", "rows": "10"})
#     work_environ = forms.Textarea(attrs={"cols": "35", "rows": "10"})
#     job_desc = forms.Textarea(attrs={"cols": "35", "rows": "10","required": False})
#     other_details = forms.Textarea(attrs={"cols": "35", "rows": "10"})

#     class Meta:
#         model = Company
#         fields = ['overview','work_environ','job_desc','other_details']


#     @transaction.atomic#if an exception occurs changes are not saved
#     def save(self):
#         return self.cleaned_data.get('overview'),self.cleaned_data.get('work_environ'),self.cleaned_data.get('job_desc'),self.cleaned_data.get('other_details')

# class CompanyEditForm(forms.ModelForm):
    # email = forms.EmailField(required=True)
    # contact_number = forms.CharField(max_length=12,required=True)
    # company_name =forms.CharField(required=True)
    # address = forms.CharField(required=True)
    # profile = forms.ChoiceField(choices=Profiles_choices)
    # overview = forms.Textarea(attrs={"cols": "35", "rows": "10"})
    # work_environ = forms.Textarea(attrs={"cols": "35", "rows": "10"})
    # job_desc = forms.Textarea(attrs={"cols": "35", "rows": "10"})
    # other_details = forms.Textarea(attrs={"cols": "35", "rows": "10"})

    # class Meta():
    #     model = Company
    #     fields = ['email','contact_number','company_name','address','profile','overview','work_environ','job_desc','other_details']

    # @transaction.atomic  #if an exception occurs changes are not saved
    # def save(self):
    #     return self.cleaned_data.get('contact_number'),self.cleaned_data.get('address'),self.cleaned_data.get('profile'),self.cleaned_data.get('overview'),self.cleaned_data.get('work_environ'),self.cleaned_data.get('job_desc'),self.cleaned_data.get('other_details')