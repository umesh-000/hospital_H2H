from django.urls import path
from . import views

urlpatterns = [

    # Hospital Panel
    path('', views.hospital_dashboard, name='hospital_dashboard'),
    # path('doctor/create/', views.doctor_create, name='doctor_create'),
    # path('doctor/<int:id>/edit/', views.doctor_edit, name='doctor_edit'),   
]