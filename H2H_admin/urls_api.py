from django.urls import path
from H2H_admin import hospital_api_view as API_view


urlpatterns = [
    path('customer/generate_otp/', API_view.GenerateOTPView.as_view(), name='generate_otp_api'),
    path('customer/verify_otp/', API_view.VerifyOTPView.as_view(), name='verify_otp_api'),
    path('customer/register_with_otp/', API_view.RegisterView_OTP.as_view(), name='RegisterView_OTP'),
    path('customer/login_with_otp/', API_view.LoginView_OTP.as_view(), name='customer_login_with_otp'),
    

    # social login 
    path('customer/social-login/', API_view.SocialLogin.as_view(), name='social-login'),
    # Auth
    path('customer/register/', API_view.RegisterView.as_view(), name='customer_register'),
    path('customer/login/', API_view.LoginView.as_view(), name='customer_login'),

    # # Hospital Bed Booking Flow
    path('customer/getHospitalsList/', API_view.get_hospitals_list_api, name='get_hospitals_api'),
    path('customer/getHospitalDetails/', API_view.get_hospital_details, name='get_hospital_details'), 
    path('customer/getBookingTimeSlots/', API_view.get_booking_time_slots, name='get_booking_time_slots'),
    path('customer/getSpecialities/', API_view.get_specialities_api, name='get_specialities_api'),
    path('customer/getSymptoms/', API_view.get_symptoms_api, name='get_symptoms_api'),
    path('customer/getHospitalWards/', API_view.get_hospital_wards_api, name='get_hospital_wards_api'),
    path('customer/getHospitalBeds/', API_view.get_hospital_beds_api, name='get_hospital_beds_api'),
    path('customer/getBloodGroup/', API_view.get_blood_group_api, name='get_blood_group_api'),
    
    path('customer/store_bed_booking/', API_view.store_bed_booking, name='store_bed_booking'),
    path('customer/allBedStatus/', API_view.allBedStatus, name='allBedStatus_api'),


    path('customer/getDoctors/', API_view.get_doctors_api, name='get_doctors_list'),
    path('customer/getDoctorsDetails/', API_view.get_doctors_details, name='get_doctors_details'),    
    path('customer/getClinicCategories/', API_view.getClinicCategories, name='getClinicCategories_api'),
    path('customer/getHospitalDoctors/', API_view.getHospitalDoctors, name='get_hospital_doctors_api'),
    path('customer/getExpertTalk/', API_view.getExpertTalk, name='get_expert_talk_api'),
    path('customer/getDoctorclinics/', API_view.getDoctorclinics, name='get_doctor_clinics_api'),
    path('customer/getClinicTimeSlots/', API_view.getClinicTimeSlots, name='get_clinic_time_slots_api'),
    path('customer/getDoctorBanners/', API_view.getDoctorBanners, name='get_doctor_banners_api'),
    path('customer/getHomeBanners/', API_view.getHomeBanners, name='get_home_banners_api'),

    path('customer/getRecommendedHospitals/', API_view.getRecommendedHospitals, name='getRecommendedHospitals_api'),
    path('customer/getBlogs/', API_view.getBlogs, name='get_blogs_api'),
    path('customer/getBlogDetails/<int:id>/', API_view.getBlogDetails, name='get_blog_details'),
    path('customer/getServices/', API_view.getServices, name='get_services_api'),

    path('customer/sendQuery/', API_view.sendQuery, name='sendQuery_api'),
    path('customer/getReminderCategories/', API_view.getReminderCategories, name='getReminderCategories_api'),
    path('customer/getReminders/', API_view.getReminders, name='getReminders_api'),
    path('customer/getCounts/', API_view.get_counts, name='get_counts_api'),
    path('customer/getAllergies/', API_view.getAllergies, name='getAllergies_api'),
    path('customer/getMedications/', API_view.getMedications, name='getMedications_api'),

    path('customer/getHelpDeskQueryDetails/', API_view.getHelpDeskQueryDetails, name='getHelpDeskQueryDetails_api'),
    path('customer/addReminder/', API_view.addReminder, name='add_reminder_api'),
    
    path('customer/addFeedback/', API_view.addFeedback, name='addFeedback_api'),
    path("customer/updateProfile/", API_view.updateProfile, name="updateProfile_api"),
    path('customer/mark_As_Done_Reminder/', API_view.mark_As_Done_Reminder, name='mark_as_done_reminder_api'),
    path('customer/getTopCities/', API_view.getTopCities, name='get_top_cities_api'),
    path('customer/addCustomerInsurance/', API_view.addCustomerInsurance, name='get_top_cities_api'),
    path('customer/deleteCustomerInsurance/', API_view.delete_Customer_Insurance, name='delete_Customer_Insurance_api'),
    path('customer/getCustomerInsurance/', API_view.getCustomerInsurance, name='getCustomerInsurance_api'),
    path('customer/updateReminder/', API_view.updateReminder, name='updateReminder_api'),
    path('customer/deleteReminder/', API_view.deleteReminder, name='deleteReminder_api'),

    # customer family member
    path('customer/familyMemberAdd/', API_view.familyMemberAdd, name='familyMemberAdd_api'),
    path('customer/familyMemberUpdate/', API_view.familyMemberUpdate, name='familyMemberUpdate_api'),
    path('customer/familyMemberDelete/', API_view.familyMemberDelete, name='familyMemberDelete_api'),
    path('customer/familyMemberLists/', API_view.familyMemberLists, name='familyMemberLists_api'),
    path('customer/fetchFamilyMemberDetails/<int:member_id>/', API_view.fetchFamilyMemberDetails, name='fetchFamilyMemberDetails_api'),

    # Laboratory 
    path('customer/labLists/', API_view.labLists, name='labLists_api'),        
    path('customer/labCategories/', API_view.labServicesList, name='labCategories_api'),        
    path('customer/labBookingTimeSlot/', API_view.labBookingTimeSlot, name='labBookingTimeSlot_api'),        
    path('customer/labDetails/', API_view.labDetails, name='labDetails_api'),  
    path('customer/labPackages/', API_view.labPackages, name='labPackages_api'),  
    path('customer/labPackageDetails/', API_view.labPackageDetails, name='labPackageDetails_api'),  


    path('customer/addAddress/', API_view.addAddress, name='addAddress_api'),    
    path('customer/updateAddress/', API_view.updateAddress, name='updateAddress_api'),    
    path('customer/editAddress/', API_view.editAddress, name='editAddress_api'),    
    path('customer/listAddresses/', API_view.listCustomerAddresses, name='listCustomerAddresses_api'),    
    path('customer/deleteAddresses/', API_view.deleteAddresses, name='deleteAddresses_api'),
    path('customer/addWalletAmount/', API_view.addWalletAmount, name='addWalletAmount_api'),    
    path('customer/getWalletTransactions/', API_view.getAllTransactionHistory, name='getWalletTransactions_api'),    
    path('customer/getProfileDetails/', API_view.getProfileDetails, name='getProfileDetails_api'),    
    path('customer/getBedBookings/', API_view.getBedBookings, name='getBedBookings_api'),  

    path('customer/getBedBookings/<int:booking_id>/', API_view.getBookingDetails, name='getBookingDetails_api'),  
    path('customer/updateBedBookings/<int:booking_id>/', API_view.updateBedBookings, name='updateBedBookings_api'),
    path('customer/addDoctorBookings/', API_view.addDoctorBooking, name='addDoctorBooking_api'),
    path('customer/getDoctorBookings/', API_view.getDoctorBooking, name='getDoctorBooking_api'),
    path('customer/getDoctorBookings/<int:booking_id>/', API_view.getDoctorBookingsDetails, name='getDoctorBookingsDetails_api'),  
    path('customer/cancelDoctorBooking/', API_view.cancelDoctorBooking, name='cancelDoctorBooking_api'),  
    path('customer/getNotifications/', API_view.getNotifications, name='getNotifications_api'),  
    path('customer/placeLabOrders/', API_view.PlaceLabOrder.as_view(), name='placeLabOrders_api'),  
    
]