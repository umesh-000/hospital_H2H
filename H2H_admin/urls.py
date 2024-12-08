from django.urls import path
from H2H_admin.views import views
from H2H_admin.views import hospital_views
from H2H_admin.views import lab_views
from H2H_admin.views import dr_views
from H2H_admin.views import customers_views

urlpatterns = [

    path('', views.admin_dashboard, name='admin_dashboard'),
    
    # Users
    path('users/', views.users, name='all_users'),
    path('users/<int:id>/show', views.show_user, name='show_user'),
    path('users/<int:id>/edit', views.edit_user, name='edit_user'),
    path('users/<int:id>/delete', views.delete_user, name='delete_user'),

    # Customer Module
    path('customers/', customers_views.customers_list, name='customers_list'),
    path('customers/<int:id>/edit/', customers_views.customers_edit, name='customers_edit'),
    path('customers/<int:id>/show/', customers_views.customers_show, name='customers_show'),
    path('customers/<int:id>/delete/', customers_views.customers_delete, name='customers_delete'),

    # Help Desk Query
    path('help_desk_query/', customers_views.help_desk_query, name='help_desk_query_list'),
    path('help_desk_query/<int:id>/edit/', customers_views.help_desk_query_edit, name='help_desk_query_edit'),
    path('help_desk_query/<int:id>/show/', customers_views.help_desk_query_show, name='help_desk_query_show'),
    path('help_desk_query/<int:id>/delete/', customers_views.help_desk_query_delete, name='help_desk_query_delete'),

    # User Feedback
    path('feedbacks/', customers_views.feedbacks, name='feedbacks_list'),
    path('feedbacks/<int:id>/edit/', customers_views.feedbacks_edit, name='feedbacks_edit'),
    path('feedbacks/<int:id>/show/', customers_views.feedbacks_show, name='feedbacks_show'),
    path('feedbacks/<int:id>/delete/', customers_views.feedbacks_delete, name='feedbacks_delete'),
     path('feedbacks/approve-status/', customers_views.update_approval_status, name='update_approval_status'),

    # Blogs
    path('blogs/', views.blogs_list, name='blogs_list'),
    path('blogs/create/', views.blogs_create, name='blogs_create'),
    path('blogs/<int:id>/edit/', views.blogs_edit, name='blogs_edit'),
    path('blogs/<int:id>/delete/', views.blogs_delete, name='blogs_delete'),

    # Hospital
    path('hospital/', hospital_views.hospital_list, name='hospital_list'),
    path('hospital_create/', hospital_views.hospital_create, name='hospital_create'),
    path('hospital/<int:id>/edit/', hospital_views.hospital_edit, name='hospital_edit'),
    path('hospital/<int:id>/delete/', hospital_views.hospital_delete, name='hospital_delete'),

    # # Ward
    path('hospital_wards/', hospital_views.ward_list, name='ward_list'),
    path('hospital_ward_create/', hospital_views.ward_create, name='ward_create'),
    path('hospital_ward/<int:id>/edit/', hospital_views.ward_edit, name='ward_edit'),
    path('hospital_ward/<int:id>/delete/', hospital_views.ward_delete, name='ward_delete'),

    # # Bed
    path('hospital_beds/', hospital_views.bed_list, name='bed_list'),
    path('hospital_bed_create/', hospital_views.bed_create, name='bed_create'),
    path('hospital_bed/<int:id>/edit/', hospital_views.bed_edit, name='bed_edit'),
    path('hospital_bed/<int:id>/delete/', hospital_views.bed_delete, name='bed_delete'),

    # Bed Status 
    path('hospital_bed_status/', hospital_views.bed_status_list, name='bed_status_list'),
    path('hospital_bed_status_create/', hospital_views.bed_status_create, name='bed_status_create'),
    path('hospital_bed_status/<int:id>/edit/', hospital_views.bed_status_edit, name='bed_status_edit'),
    path('hospital_bed_status/<int:id>/delete/', hospital_views.bed_status_delete, name='bed_status_delete'),

    # # Hospital Fee Setting # Edit Pending for this 
    # path('admin/hospital/fee_settings/', hospital_views.hospital_fee_setting_list, name='hospital_fee_setting_list'),
    # path('admin/hospital/fee_settings/create/', hospital_views.hospital_fee_setting_list_create, name='hospital_fee_setting_list_create'),

    # Hospital Service 
    path('hospital_services/', hospital_views.hospital_service_list, name='hospital_service_list'),
    path('hospital_service_create/', hospital_views.hospital_service_create, name='hospital_service_create'),
    path('hospital_service/<int:id>/edit/', hospital_views.hospital_service_edit, name='hospital_service_edit'),
    path('hospital_service/<int:id>/delete/', hospital_views.hospital_service_delete, name='hospital_service_delete'),

    # Hospital Department
    path('hospital_departments/', hospital_views.hospital_department_list, name='hospital_department_list'),
    path('hospital_department_create/', hospital_views.hospital_department_create, name='hospital_department_create'),
    path('hospital_department/<int:id>/edit/', hospital_views.hospital_department_edit, name='hospital_department_edit'),
    path('hospital_department/<int:id>/delete/', hospital_views.hospital_department_delete, name='hospital_department_delete'),


    # Hospital Facilities 
    path('hospital_facilities/', hospital_views.hospital_facilities_list, name='hospital_facilities_list'),
    path('hospital_facility_create/', hospital_views.hospital_facility_create, name='hospital_facility_create'),
    path('hospital_facility/<int:id>/edit/', hospital_views.hospital_facility_edit, name='hospital_facility_edit'),
    path('hospital_facility/<int:id>/delete/', hospital_views.hospital_facility_delete, name='hospital_facility_delete'),


    

    # Specialist
    path('specialists/', hospital_views.specialist_list, name='specialist_list'),
    path('specialist_create/', hospital_views.specialist_create, name='specialist_create'),
    path('specialist/<int:id>/edit/', hospital_views.specialist_edit, name='specialist_edit'),
    path('specialist/<int:id>/delete/', hospital_views.specialist_delete, name='specialist_delete'),

    # Symptoms
    path('symptoms/', hospital_views.symptoms_list, name='symptoms_list'),
    path('symptom_create/', hospital_views.symptom_create, name='symptom_create'),
    path('symptom/<int:id>/edit/', hospital_views.symptom_edit, name='symptom_edit'),
    path('symptom/<int:id>/delete/', hospital_views.symptom_delete, name='symptom_delete'),

    # Hospital Doctors 
    path('hospital_doctors/', hospital_views.hospital_doctors_list, name='hospital_doctors_list'),
    path('hospital_doctor/create', hospital_views.hospital_doctor_create, name='hospital_doctor_create'),
    path('hospital_doctor/<int:id>/edit/', hospital_views.hospital_doctor_edit, name='hospital_doctor_edit'),
    path('hospital_doctor/<int:id>/delete/', hospital_views.hospital_doctor_delete, name='hospital_doctor_delete'),
    
    
    # Doctors
    path('doctors/', dr_views.doctors_list, name='doctors_list'),
    path('doctor/create/', dr_views.doctor_create, name='doctor_create'),
    path('doctor/<int:id>/edit/', dr_views.doctor_edit, name='doctor_edit'),
    path('doctor/<int:id>/delete/', dr_views.doctor_delete, name='doctor_delete'),

    # Doctor Clinics Category
    path('doctor_clinic_categories/', dr_views.doctor_clinic_categories, name='doctor_clinic_categories'),
    path('doctor_clinic_category/create/', dr_views.clinic_category_create, name='clinic_category_create'),
    path('doctor_clinic_category/<int:id>/edit/', dr_views.clinic_category_edit, name='clinic_category_edit'),
    path('doctor_clinic_category/<int:id>/delete/', dr_views.clinic_category_delete, name='clinic_category_delete'),


   # Doctor Clinics Category
    path('doctor_clinics/', dr_views.doctor_clinics, name='doctor_clinic_list'),
    path('doctor_clinic/create', dr_views.doctor_clinics_create, name='doctor_clinic_create'),
    path('doctor_clinic/<int:id>/edit/', dr_views.doctor_clinics_edit, name='doctor_clinics_edit'),
    path('doctor_clinic/<int:id>/delete/', dr_views.doctor_clinics_delete, name='doctor_clinics_delete'),

    # Doctor Banner Category
    path('doctor_banner/', dr_views.dr_banner_list, name='dr_banner_list'),
    path('doctor_banner/create/', dr_views.doctor_banner_create, name='doctor_banner_create'),
    path('doctor_banner/<int:id>/edit/', dr_views.doctor_banner_edit, name='doctor_banner_edit'),
    path('doctor_banner/<int:id>/delete/', dr_views.doctor_banner_delete, name='doctor_banner_delete'),

#     # Doctor Document
    path('doctor_documents/', dr_views.doctor_documents, name='doctor_documents_list'),
    path('change_doc_status/', dr_views.change_doc_status, name='change_doc_status'),
    

    

#     # Doctor Booking 
#     path('doctor-bookings/', views.doctor_booking_requests, name='doctor_booking_requests'),
#     path('update_doctor_booking_status/', views.update_doctor_booking_status, name='update_doctor_booking_status'),

    # LAB 
    path('laboratories/', lab_views.laboratories, name='laboratories_list'),
    path('laboratories/create/', lab_views.laboratories_create, name='laboratories_create'),
    path('laboratories/<int:id>/edit/', lab_views.laboratories_edit, name='laboratories_edit'),
    path('laboratories/<int:id>/delete/', lab_views.laboratories_delete, name='laboratories_delete'),


    # LAB Tags
    path('lab_tags/', lab_views.lab_tags, name='lab_tags_list'),
    path('lab_tags/create/', lab_views.lab_tags_create, name='lab_tags_create'),
    path('lab_tags/<int:id>/edit/', lab_views.lab_tags_edit, name='lab_tags_edit'),
    path('lab_tags/<int:id>/delete/', lab_views.lab_tags_delete, name='lab_tags_delete'),

    #Service
    path('services/', lab_views.services_list, name='services_list'),
    path('services/create/', lab_views.services_create, name='services_create'),
    path('services/<int:id>/edit/', lab_views.services_edit, name='services_edit'),
    path('services/<int:id>/delete/', lab_views.services_delete, name='services_delete'),

    #Lab Service
    path('lab_services/', lab_views.lab_services_list, name='lab_services_list'),
    path('lab_services/create/', lab_views.lab_services_create, name='lab_services_create'),
    path('lab_services/<int:id>/edit/', lab_views.lab_services_edit, name='lab_services_edit'),
    path('lab_services/<int:id>/delete/', lab_views.lab_services_delete, name='lab_services_delete'),

    #Lab Banners
    path('lab_banners/', lab_views.lab_banners_list, name='lab_banners_list'),
    path('lab_banners/create/', lab_views.lab_banners_create, name='lab_banners_create'),
    path('lab_banners/<int:id>/edit/', lab_views.lab_banners_edit, name='lab_banners_edit'),
    path('lab_banners/<int:id>/delete/', lab_views.lab_banners_delete, name='lab_banners_delete'),

    #Lab Staff
    path('lab_staff/', lab_views.lab_staff_list, name='lab_staff_list'),
    path('lab_staff/create/', lab_views.lab_staff_create, name='lab_staff_create'),
    path('lab_staff/<int:id>/edit/', lab_views.lab_staff_edit, name='lab_staff_edit'),
    path('lab_staff/<int:id>/delete/', lab_views.lab_staff_delete, name='lab_staff_delete'),

    #Lab Package
    path('lab_package/', lab_views.lab_package_list, name='lab_package_list'),
    path('lab_package/create/', lab_views.lab_package_create, name='lab_package_create'),
    path('lab_package/<int:id>/edit/', lab_views.lab_package_edit, name='lab_package_edit'),
    path('lab_package/<int:id>/delete/', lab_views.lab_package_delete, name='lab_package_delete'),

    path('banners/', views.banners_list, name='banners_list'),
    path('banner_create/', views.banner_create, name='banner_create'),
    path('banner/<int:id>/edit/', views.banner_edit, name='banner_edit'),
    path('banner/<int:id>/delete/', views.banner_delete, name='banner_delete'),

    path('module_offer_banners/', views.module_offer_banners, name='module_offer_banners_list'),
    path('module_offer_banner_create/', views.module_offer_banners_create, name='module_offer_banners_create'),
    path('module_offer_banner/<int:id>/edit/', views.module_offer_banners_edit, name='module_offer_banners_edit'),
    path('module_offer_banner/<int:id>/delete/', views.module_offer_banners_delete, name='module_offer_banners_delete'),

    path('expert_talks/', views.expert_talks_list, name='expert_talks_list'),
    path('expert_talks/create/', views.expert_talks_create, name='expert_talks_create'),
    path('expert_talks/<int:id>/edit/', views.expert_talks_edit, name='expert_talks_edit'),
    path('expert_talks/<int:id>/delete/', views.expert_talks_delete, name='expert_talks_delete'),

    path('bed-requests/', hospital_views.bed_requests, name='bed_requests'),
    path('update_booking_status/', hospital_views.update_booking_status, name='update_booking_status'),

]