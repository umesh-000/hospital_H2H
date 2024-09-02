from django.urls import path
from . import views

urlpatterns = [

    # Doctors
    path('doctors/', views.doctors_list, name='doctors_list'),
    path('doctor/create/', views.doctor_create, name='doctor_create'),
    path('doctor/<int:id>/edit/', views.doctor_edit, name='doctor_edit'),

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