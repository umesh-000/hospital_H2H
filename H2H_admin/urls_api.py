from django.urls import path
from H2H_admin.views import hospital_api_view


urlpatterns = [
    # Auth
    path('customer/register/', hospital_api_view.RegisterView.as_view(), name='customer_register'),
    path('customer/login/', hospital_api_view.LoginView.as_view(), name='customer_login'),

    # # Hospital Bed Booking Flow
    path('customer/getHospitalsList/', hospital_api_view.get_hospitals_list_api, name='get_hospitals_api'),
    path('customer/getHospitalDetails/', hospital_api_view.get_hospital_details, name='get_hospital_details'), 
    path('customer/getBookingTimeSlots/', hospital_api_view.get_booking_time_slots, name='get_booking_time_slots'),
    path('customer/getSpecialities/', hospital_api_view.get_specialities_api, name='get_specialities_api'),
    path('customer/getSymptoms/', hospital_api_view.get_symptoms_api, name='get_symptoms_api'),
    path('customer/getHospitalWards/', hospital_api_view.get_hospital_wards_api, name='get_hospital_wards_api'),
    path('customer/getHospitalBeds/', hospital_api_view.get_hospital_beds_api, name='get_hospital_beds_api'),
    path('customer/getBloodGroup/', hospital_api_view.get_blood_group_api, name='get_blood_group_api'),
    
    path('store_bed_booking/', hospital_api_view.store_bed_booking, name='store_bed_booking'),
    # path('hospital_allbed_status/', hospital_api_view.hospital_all_bed_status, name='hospital_all_bed_status'),


    path('customer/getDoctors/', hospital_api_view.get_doctors_api, name='get_doctors_list'),
    path('customer/getDoctorsDetails/', hospital_api_view.get_doctors_details, name='get_doctors_details'),    
    path('customer/getClinicCategories/', hospital_api_view.getClinicCategories, name='getClinicCategories_api'),
    path('customer/getHospitalDoctors/', hospital_api_view.getHospitalDoctors, name='get_hospital_doctors_api'),
    path('customer/getExpertTalk/', hospital_api_view.getExpertTalk, name='get_expert_talk_api'),
    path('customer/getDoctorclinics/', hospital_api_view.getDoctorclinics, name='get_doctor_clinics_api'),
    path('customer/getClinicTimeSlots/', hospital_api_view.getClinicTimeSlots, name='get_clinic_time_slots_api'),
    path('customer/getDoctorBanners/', hospital_api_view.getDoctorBanners, name='get_doctor_banners_api'),
    path('customer/getHomeBanners/', hospital_api_view.getHomeBanners, name='get_home_banners_api'),

    path('customer/getRecommendedHospitals/', hospital_api_view.getRecommendedHospitals, name='getRecommendedHospitals_api'),
    path('customer/getBlogs/', hospital_api_view.getBlogs, name='get_blogs_api'),
    path('customer/getBlogDetails/<int:id>/', hospital_api_view.getBlogDetails, name='get_blog_details'),
    path('customer/getServices/', hospital_api_view.getServices, name='get_services_api'),

    path('customer/sendQuery/', hospital_api_view.sendQuery, name='sendQuery_api'),
    path('customer/getReminderCategories/', hospital_api_view.getReminderCategories, name='getReminderCategories_api'),
    path('customer/getReminders/', hospital_api_view.getReminders, name='getReminders_api'),
    path('customer/getCounts/', hospital_api_view.get_counts, name='get_counts_api'),
    path('customer/getAllergies/', hospital_api_view.getAllergies, name='getAllergies_api'),
    path('customer/getMedications/', hospital_api_view.getMedications, name='getMedications_api'),

    path('customer/getHelpDeskQueryDetails/', hospital_api_view.getHelpDeskQueryDetails, name='getHelpDeskQueryDetails_api'),
    path('customer/addReminder/', hospital_api_view.addReminder, name='add_reminder_api'),
    
    path('customer/addFeedback/', hospital_api_view.addFeedback, name='addFeedback_api'),
]