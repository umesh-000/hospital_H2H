from django.urls import path
from .views import views
from .views import hospital_views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', views.index, name='index'),

    # Users
    path('admin/users/', views.users, name='users'),
    path('admin/users/<int:id>/', views.show_user, name='show_user'),
    path('admin/users/<int:id>/edit', views.edit_user, name='edit_user'),
    path('admin/users/<int:id>/delete', views.delete_user, name='delete_user'),

    path('admin/login/', views.login, name='login'),
    path('admin/register/', views.register, name='register'),

    # Hospital
    path('admin/hospital/', hospital_views.hospital_list, name='hospital_list'),
    path('admin/hospital/create/', hospital_views.hospital_create, name='hospital_create'),
    path('admin/hospital/<int:id>/edit/', hospital_views.hospital_edit, name='hospital_edit'),
    path('admin/hospital/<int:id>/delete/', hospital_views.hospital_delete, name='hospital_delete'),

    # Ward
    path('admin/hospital/ward/', hospital_views.ward_list, name='ward_list'),
    path('admin/hospital/ward/create/', hospital_views.ward_create, name='ward_create'),
    path('admin/hospital/ward/<int:id>/edit/', hospital_views.ward_edit, name='ward_edit'),
    path('admin/hospital/ward/<int:id>/delete/', hospital_views.ward_delete, name='ward_delete'),

    # Bed
    path('admin/hospital/ward/beds/', hospital_views.bed_list, name='bed_list'),
    path('admin/hospital/ward/bed/create/', hospital_views.bed_create, name='bed_create'),
    path('admin/hospital/ward/bed/<int:id>/edit/', hospital_views.bed_edit, name='bed_edit'),
    path('admin/hospital/ward/bed/<int:id>/delete/', hospital_views.bed_delete, name='bed_delete'),

    # Bed Status 
    path('admin/hospital/ward/bed/status/', hospital_views.bed_status_list, name='bed_status_list'),
    path('admin/hospital/ward/bed/status/create/', hospital_views.bed_status_create, name='bed_status_create'),
    path('admin/hospital/ward/bed/status/<int:id>/edit/', hospital_views.bed_status_edit, name='bed_status_edit'),
    path('admin/hospital/ward/bed/status/<int:id>/delete/', hospital_views.bed_status_delete, name='bed_status_delete'),

    path('admin/bed-requests/', hospital_views.bed_requests, name='bed_requests'),
    path('admin/update_booking_status/', hospital_views.update_booking_status, name='update_booking_status'),

    # Hospital Fee Setting 
    path('admin/hospital/fee_settings/', hospital_views.hospital_fee_setting_list, name='hospital_fee_setting_list'),
    path('admin/hospital/fee_settings/create/', hospital_views.hospital_fee_setting_list_create, name='hospital_fee_setting_list_create'),

    # Hospital Service 
    path('admin/hospital/services/', hospital_views.hospital_service_list, name='hospital_service_list'),
    path('admin/hospital/service/create/', hospital_views.hospital_service_create, name='hospital_service_create'),
    path('admin/hospital/service/<int:id>/edit/', hospital_views.hospital_service_edit, name='hospital_service_edit'),
    path('admin/hospital/service/<int:id>/delete/', hospital_views.hospital_service_delete, name='hospital_service_delete'),

    # Hospital Department
    path('admin/hospital/departments/', hospital_views.hospital_department_list, name='hospital_department_list'),
    path('admin/hospital/department/create/', hospital_views.hospital_department_create, name='hospital_department_create'),
    path('admin/hospital/department/<int:id>/edit/', hospital_views.hospital_department_edit, name='hospital_department_edit'),

    # Hospital Facilities 
    path('admin/hospital/facilities/', hospital_views.hospital_facilities_list, name='hospital_facilities_list'),
    path('admin/hospital/facility/create/', hospital_views.hospital_facility_create, name='hospital_facility_create'),
    path('admin/hospital/facility/<int:id>/edit/', hospital_views.hospital_facility_edit, name='hospital_facility_edit'),

    # Hospital Doctors 
    path('admin/hospital_doctors/', hospital_views.hospital_doctors_list, name='hospital_doctors_list'),
    path('admin/hospital_doctor/create', hospital_views.hospital_doctor_create, name='hospital_doctor_create'),
    path('admin/hospital_doctor/<int:id>/edit/', hospital_views.hospital_doctor_edit, name='hospital_doctor_edit'),
    path('admin/hospital_doctor/<int:id>/delete/', hospital_views.hospital_doctor_delete, name='hospital_doctor_delete'),

    # Insurances
    path('admin/insurances/', hospital_views.insurances_list, name='insurances_list'),
    path('admin/insurance/create/', hospital_views.insurance_create, name='insurance_create'),
    path('admin/insurance/<int:id>/edit/', hospital_views.insurance_edit, name='insurance_edit'),
    path('admin/insurance/<int:id>/delete/', hospital_views.insurance_delete, name='insurance_delete'),

    # Hospital Insurances
    path('admin/hospital_insurances/', hospital_views.hospital_insurance_list, name='hospital_insurance_list'),
    path('admin/hospital_insurance/create/', hospital_views.hospital_insurance_create, name='hospital_insurance_create'),
    path('admin/hospital_insurance/<int:id>/edit/', hospital_views.hospital_insurance_edit, name='hospital_insurance_edit'),
    path('admin/hospital_insurance/<int:id>/delete/', hospital_views.hospital_insurance_delete, name='hospital_insurance_delete'),
]