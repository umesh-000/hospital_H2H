from django.urls import path
from doctor import views


urlpatterns = [
    path('', views.doctors_dashboard, name='doctors_dashboard'),

#     # Doctor Document
#     path('doctor_documents/', views.doctor_documents, name='doctor_documents_list'),
#     path('change_doc_status/', views.change_doc_status, name='change_doc_status'),
    
#     # Doctor Booking 
#     path('doctor-bookings/', views.doctor_booking_requests, name='doctor_booking_requests'),
#     path('update_doctor_booking_status/', views.update_doctor_booking_status, name='update_doctor_booking_status'),
]