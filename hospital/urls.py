from django.urls import path
from hospital.views import views
from hospital.views import hospital_views

urlpatterns = [
    # # Hospital Panel
    path('', hospital_views.hospital_dashboard, name='hospital_dashboard'),


    # path('login/', views.hospital_login, name='hospital_login'),
    # path('register/', views.hospital_register, name='hospital_login'),

    # path('bed-requests/', hospital_views.bed_requests, name='bed_requests'),
    # path('update_booking_status/', hospital_views.update_booking_status, name='update_booking_status'),

    # # # Hospital Fee Setting # Edit Pending for this 
    # # path('admin/hospital/fee_settings/', hospital_views.hospital_fee_setting_list, name='hospital_fee_setting_list'),
    # # path('admin/hospital/fee_settings/create/', hospital_views.hospital_fee_setting_list_create, name='hospital_fee_setting_list_create'),




    # # Insurances
    # path('insurances/', hospital_views.insurances_list, name='insurances_list'),
    # path('insurance/create/', hospital_views.insurance_create, name='insurance_create'),
    # path('insurance/<int:id>/edit/', hospital_views.insurance_edit, name='insurance_edit'),
    # path('insurance/<int:id>/delete/', hospital_views.insurance_delete, name='insurance_delete'),

    # # Hospital Insurances
    # path('hospital_insurances/', hospital_views.hospital_insurance_list, name='hospital_insurance_list'),
    # path('hospital_insurance/create/', hospital_views.hospital_insurance_create, name='hospital_insurance_create'),
    # path('hospital_insurance/<int:id>/edit/', hospital_views.hospital_insurance_edit, name='hospital_insurance_edit'),
    # path('hospital_insurance/<int:id>/delete/', hospital_views.hospital_insurance_delete, name='hospital_insurance_delete'),
]