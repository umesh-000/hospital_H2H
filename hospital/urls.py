from django.urls import path
from hospital.views import views
from hospital.views import hospital_views

urlpatterns = [
    # Hospital Panel
    path('', hospital_views.hospital_dashboard, name='hospital_dashboard'),


    path('login/', views.hospital_login, name='hospital_login'),
    path('register/', views.hospital_register, name='hospital_login'),


    # Hospital
    path('hospitals/', hospital_views.hospital_list, name='hospital_panel_list'),
    path('hospital/create/', hospital_views.hospital_create, name='hospital_create'),
    path('hospital/<int:id>/edit/', hospital_views.hospital_edit, name='hospital_edit'),
    path('hospital/<int:id>/delete/', hospital_views.hospital_delete, name='hospital_delete'),

    # Ward
    path('hospital_wards/', hospital_views.ward_list, name='ward_list'),
    path('hospital_ward/create/', hospital_views.ward_create, name='ward_create'),
    path('hospital_ward/<int:id>/edit/', hospital_views.ward_edit, name='ward_edit'),
    path('hospital_ward/<int:id>/delete/', hospital_views.ward_delete, name='ward_delete'),

    # Bed
    path('hospital_beds/', hospital_views.bed_list, name='bed_list'),
    path('hospital_bed/create/', hospital_views.bed_create, name='bed_create'),
    path('hospital_bed/<int:id>/edit/', hospital_views.bed_edit, name='bed_edit'),
    path('hospital_bed/<int:id>/delete/', hospital_views.bed_delete, name='bed_delete'),

    # Bed Status 
    path('hospital_bed_status/', hospital_views.bed_status_list, name='bed_status_list'),
    path('hospital_bed_status/create/', hospital_views.bed_status_create, name='bed_status_create'),
    path('hospital_bed_status/<int:id>/edit/', hospital_views.bed_status_edit, name='bed_status_edit'),
    path('hospital_bed_status/<int:id>/delete/', hospital_views.bed_status_delete, name='bed_status_delete'),

    path('bed-requests/', hospital_views.bed_requests, name='bed_requests'),
    path('update_booking_status/', hospital_views.update_booking_status, name='update_booking_status'),

    # # Hospital Fee Setting # Edit Pending for this 
    # path('admin/hospital/fee_settings/', hospital_views.hospital_fee_setting_list, name='hospital_fee_setting_list'),
    # path('admin/hospital/fee_settings/create/', hospital_views.hospital_fee_setting_list_create, name='hospital_fee_setting_list_create'),

    # Hospital Service 
    path('hospital_services/', hospital_views.hospital_service_list, name='hospital_service_list'),
    path('hospital_service/create/', hospital_views.hospital_service_create, name='hospital_service_create'),
    path('hospital_service/<int:id>/edit/', hospital_views.hospital_service_edit, name='hospital_service_edit'),
    path('hospital_service/<int:id>/delete/', hospital_views.hospital_service_delete, name='hospital_service_delete'),

    # Hospital Department
    path('hospital_departments/', hospital_views.hospital_department_list, name='hospital_department_list'),
    path('hospital_department/create/', hospital_views.hospital_department_create, name='hospital_department_create'),
    path('hospital_department/<int:id>/edit/', hospital_views.hospital_department_edit, name='hospital_department_edit'),
    path('hospital_department/<int:id>/delete/', hospital_views.hospital_department_delete, name='hospital_department_delete'),


    # Hospital Facilities 
    path('hospital_facilities/', hospital_views.hospital_facilities_list, name='hospital_facilities_list'),
    path('hospital_facility/create/', hospital_views.hospital_facility_create, name='hospital_facility_create'),
    path('hospital_facility/<int:id>/edit/', hospital_views.hospital_facility_edit, name='hospital_facility_edit'),
    path('hospital_facility/<int:id>/delete/', hospital_views.hospital_facility_delete, name='hospital_facility_delete'),

    # Hospital Doctors 
    path('hospital_doctors/', hospital_views.hospital_doctors_list, name='hospital_doctors_list'),
    path('hospital_doctor/create', hospital_views.hospital_doctor_create, name='hospital_doctor_create'),
    path('hospital_doctor/<int:id>/edit/', hospital_views.hospital_doctor_edit, name='hospital_doctor_edit'),
    path('hospital_doctor/<int:id>/delete/', hospital_views.hospital_doctor_delete, name='hospital_doctor_delete'),

    # Insurances
    path('insurances/', hospital_views.insurances_list, name='insurances_list'),
    path('insurance/create/', hospital_views.insurance_create, name='insurance_create'),
    path('insurance/<int:id>/edit/', hospital_views.insurance_edit, name='insurance_edit'),
    path('insurance/<int:id>/delete/', hospital_views.insurance_delete, name='insurance_delete'),

    # Hospital Insurances
    path('hospital_insurances/', hospital_views.hospital_insurance_list, name='hospital_insurance_list'),
    path('hospital_insurance/create/', hospital_views.hospital_insurance_create, name='hospital_insurance_create'),
    path('hospital_insurance/<int:id>/edit/', hospital_views.hospital_insurance_edit, name='hospital_insurance_edit'),
    path('hospital_insurance/<int:id>/delete/', hospital_views.hospital_insurance_delete, name='hospital_insurance_delete'),
]