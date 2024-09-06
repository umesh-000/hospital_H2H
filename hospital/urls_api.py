from django.urls import path
from hospital.views import hospital_api_view


urlpatterns = [
    path('customer/register/', hospital_api_view.RegisterView.as_view(), name='customer_register'),
    path('customer/login/', hospital_api_view.LoginView.as_view(), name='customer_login'),

    path('hospitals/', hospital_api_view.get_hospitals_api, name='get_hospitals_api'),
    path('get_hospital_details/', hospital_api_view.get_hospital_details, name='get_hospital_details'), 
    path('customer/getSpecialities/', hospital_api_view.get_specialities_api, name='get_specialities_api'),
    path('customer/getSymptoms/', hospital_api_view.get_symptoms_api, name='get_symptoms_api'),
    path('customer/getHospitalWards/', hospital_api_view.get_hospital_wards_api, name='get_hospital_wards_api'),
    
    path('hospital_allbed_status/', hospital_api_view.hospital_all_bed_status, name='hospital_all_bed_status'),
    path('store_bed_booking/', hospital_api_view.store_bed_booking, name='store_bed_booking'),
]