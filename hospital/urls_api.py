from django.urls import path
from hospital.views import hospital_api_view


urlpatterns = [
    path('hospitals/', hospital_api_view.get_hospitals_api, name='get_hospitals_api'),
    path('store_bed_booking/', hospital_api_view.store_bed_booking, name='store_bed_booking'),
    path('hospital_allbed_status/', hospital_api_view.hospital_all_bed_status, name='hospital_all_bed_status'),
    path('hospital_facilities/', hospital_api_view.hospital_all_facilities, name='hospital_all_facilities'),
]