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
    
    path('customer/store_bed_booking/', hospital_api_view.store_bed_booking, name='store_bed_booking'),
    path('customer/allBedStatus/', hospital_api_view.allBedStatus, name='allBedStatus_api'),


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
    path("customer/updateProfile/", hospital_api_view.updateProfile, name="updateProfile_api"),
    path('customer/mark_As_Done_Reminder/', hospital_api_view.mark_As_Done_Reminder, name='mark_as_done_reminder_api'),
    path('customer/getTopCities/', hospital_api_view.getTopCities, name='get_top_cities_api'),
    path('customer/addCustomerInsurance/', hospital_api_view.addCustomerInsurance, name='get_top_cities_api'),
    path('customer/deleteCustomerInsurance/', hospital_api_view.delete_Customer_Insurance, name='delete_Customer_Insurance_api'),
    path('customer/getCustomerInsurance/', hospital_api_view.getCustomerInsurance, name='getCustomerInsurance_api'),
    path('customer/updateReminder/', hospital_api_view.updateReminder, name='updateReminder_api'),
    path('customer/deleteReminder/', hospital_api_view.deleteReminder, name='deleteReminder_api'),

    # customer family member
    path('customer/familyMemberAdd/', hospital_api_view.familyMemberAdd, name='familyMemberAdd_api'),
    path('customer/familyMemberUpdate/', hospital_api_view.familyMemberUpdate, name='familyMemberUpdate_api'),
    path('customer/familyMemberDelete/', hospital_api_view.familyMemberDelete, name='familyMemberDelete_api'),
    path('customer/familyMemberLists/', hospital_api_view.familyMemberLists, name='familyMemberLists_api'),
    path('customer/fetchFamilyMemberDetails/<int:member_id>/', hospital_api_view.fetchFamilyMemberDetails, name='fetchFamilyMemberDetails_api'),

    # Laboratory 
    path('customer/labLists/', hospital_api_view.labLists, name='labLists_api'),        
    path('customer/labCategories/', hospital_api_view.labServicesList, name='labCategories_api'),        
    path('customer/labBookingTimeSlot/', hospital_api_view.labBookingTimeSlot, name='labBookingTimeSlot_api'),        
    path('customer/labDetails/', hospital_api_view.labDetails, name='labDetails_api'),  
    path('customer/labPackages/', hospital_api_view.labPackages, name='labPackages_api'),  
    path('customer/labPackageDetails/', hospital_api_view.labPackageDetails, name='labPackageDetails_api'),  


    path('customer/addAddress/', hospital_api_view.addAddress, name='addAddress_api'),    
    path('customer/updateAddress/', hospital_api_view.updateAddress, name='updateAddress_api'),    
    path('customer/editAddress/', hospital_api_view.editAddress, name='editAddress_api'),    
    path('customer/listAddresses/', hospital_api_view.listCustomerAddresses, name='listCustomerAddresses_api'),    
    path('customer/deleteAddresses/', hospital_api_view.deleteAddresses, name='deleteAddresses_api'),
    path('customer/addWalletAmount/', hospital_api_view.addWalletAmount, name='addWalletAmount_api'),    
    path('customer/getWalletTransactions/', hospital_api_view.getAllTransactionHistory, name='getWalletTransactions_api'),    
    path('customer/getProfileDetails/', hospital_api_view.getProfileDetails, name='getProfileDetails_api'),    
    path('customer/getBedBookings/', hospital_api_view.getBedBookings, name='getBedBookings_api'),  

    path('customer/getBedBookings/<int:booking_id>/', hospital_api_view.getBookingDetails, name='getBookingDetails_api'),  
    path('customer/updateBedBookings/<int:booking_id>/', hospital_api_view.updateBedBookings, name='updateBedBookings_api'),
    path('customer/addDoctorBookings/', hospital_api_view.addDoctorBooking, name='addDoctorBooking_api'),
    path('customer/getDoctorBookings/', hospital_api_view.getDoctorBooking, name='getDoctorBooking_api'),
    path('customer/getDoctorBookings/<int:booking_id>/', hospital_api_view.getDoctorBookingsDetails, name='getDoctorBookingsDetails_api'),  
    path('customer/cancelDoctorBooking/', hospital_api_view.cancelDoctorBooking, name='cancelDoctorBooking_api'),  
    path('customer/getNotifications/', hospital_api_view.getNotifications, name='getNotifications_api'),  
    path('customer/placeLabOrders/', hospital_api_view.PlaceLabOrder.as_view(), name='placeLabOrders_api'),  
    
]