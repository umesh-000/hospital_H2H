from django.urls import path
from doctor import views


urlpatterns = [
    path('', views.doctors_dashboard, name='doctors_dashboard'),

    path('register/', views.doctor_register, name='doctor_register'),
    path('login/', views.doctor_login, name='doctor_login'),



    # Doctors
    path('doctors/', views.doctors_list, name='doctors_list'),
    path('doctor/create/', views.doctor_create, name='doctor_create'),
    path('doctor/<int:id>/edit/', views.doctor_edit, name='doctor_edit'),


    # Doctor Clinics Category
    path('doctor_clinic_categories/', views.doctor_clinic_categories, name='doctor_clinic_categories'),
    path('doctor_clinic_category/create/', views.clinic_category_create, name='clinic_category_create'),
    path('doctor_clinic_category/<int:id>/edit/', views.clinic_category_edit, name='clinic_category_edit'),
    path('doctor_clinic_category/<int:id>/delete/', views.clinic_category_delete, name='clinic_category_delete'),


   # Doctor Clinics Category
    path('doctor_clinics/', views.doctor_clinics, name='doctor_clinic_list'),
    path('doctor_clinic/create', views.doctor_clinics_create, name='doctor_clinic_create'),
    path('doctor_clinic/<int:id>/edit/', views.doctor_clinics_edit, name='doctor_clinics_edit'),
    path('doctor_clinic/<int:id>/delete/', views.doctor_clinics_delete, name='doctor_clinics_delete'),


    # Symptoms
    path('symptoms/', views.symptoms_list, name='symptoms_list'),
    path('symptom/create/', views.symptom_create, name='symptom_create'),
    path('symptom/<int:id>/edit/', views.symptom_edit, name='symptom_edit'),
    path('symptom/<int:id>/delete/', views.symptom_delete, name='symptom_delete'),
    

    # Specialist
    path('specialists/', views.specialist_list, name='specialist_list'),
    path('specialist/create/', views.specialist_create, name='specialist_create'),
    path('specialist/<int:id>/edit/', views.specialist_edit, name='specialist_edit'),
    path('specialist/<int:id>/delete/', views.specialist_delete, name='specialist_delete'),
    
]