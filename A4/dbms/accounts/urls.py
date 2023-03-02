#all urls of the web application is specified here
# name=" "; this name will be use for linking withing HTML
#views.func() indicates that func() defined in views will be called once the url is opened 

from django.urls import path
from .import  views
from django.urls import path

urlpatterns=[
     path('register/',views.register, name='register'),#path(url,function name, name of link)
     path('doctor_register/',views.doctor_register.as_view(), name='doctor_register'),
     path('front_desk_register/',views.front_desk_register.as_view(), name='front_desk_register'),
     path('data_entry_register/',views.data_entry_register.as_view(), name='data_entry_register'),
    
     path('patient_register/',views.patient_reg_help.as_view(), name='patient_reg'),
     path('admit_discharge/',views.handle_admit, name='handle_admit'),
     path('schedule_appointment/',views.schedule_appoint, name='schedule_appoint'),
     path('admission/',views.admit_patient.as_view(), name='patient_admit'),
     
     path('prescribe_medication/', views.doctor_prescribe.as_view(), name='prescribe_medic'),
     path('scheduler/',views.scheduler, name='scheduler'),
    
     path('',views.index, name='index'),
     path('admin_login/',views.login_admin, name='admin_login'),
     path('doctor_login/',views.login_doctor, name='doctor_login'),
     path('fr_login/',views.login_fr, name='fr_login'),
     path('de_login/',views.login_de, name='de_login'),
     path('logout/',views.logout_view, name='logout'),
     path('doctor_pat_record/', views.doctor_pat_record, name='doctor_pat_record'),
     path('record_treatment/', views.record_treatment, name='record_treatment'),
     path('patient_data_entry/',views.patient_data_entry, name='patient_data_entry'),
     path('tests/',views.test_patient.as_view(), name='patient_test'),
     path('treatments/',views.treatment_patient.as_view(), name='patient_treatment'),
    #  path('test_result/',views.patient_data_entry, name='patient_data_entry'),
    #  path('company_edit_details/',views.editCompProfile.as_view(), name='company_edit'),
    #  path('alumni_edit_details/',views.editAlumProfile.as_view(), name='alumni_edit'),
    #  path('request_feedback/',views.request_feedback, name='request_feedback'),
    #  path('feedback/',views.feedback, name='feedback'),
    #  path('stud_chat/',views.stud_chat, name='stud_chat'),
    #  path('chats/',views.chats, name='chats'),
    #  path('list_of_students/',views.list_of_students, name='list_of_students'),
    #  path('get_student_cv/',views.get_stud_cv, name='get_stud_cv'),
    #  path('get_cv/',views.get_cv, name='get_cv'),
]
