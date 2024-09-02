from rest_framework import serializers
from hospital.models import Hospital,BedBooking,HospitalDoctors,HospitalFacility
from doctor.models import DoctorDetails,DoctorSpecialistCategory


# Serialize DoctorSpecialistCategory
class DoctorSpecialistCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorSpecialistCategory
        fields = ['id', 'category_name', 'category_image','status']

# Serialize DoctorDetails
class DoctorDetailsSerializer(serializers.ModelSerializer):
    specialist = DoctorSpecialistCategorySerializer(read_only=True)
    class Meta:
        model = DoctorDetails
        fields = ['id', 'dr_name','qualification','profile_img', 'gender', 'phone', 'email','specialist']

# Serialize HospitalDoctors
class HospitalDoctorsSerializer(serializers.ModelSerializer):
    doctor = DoctorDetailsSerializer(read_only=True)

    class Meta:
        model = HospitalDoctors
        fields = ['doctor']

# Serialize Hospital with nested HospitalDoctors
class HospitalSerializer(serializers.ModelSerializer):
    hospital_doctors = HospitalDoctorsSerializer(many=True, read_only=True)

    class Meta:
        model = Hospital
        fields = ['id', 'hospital_name', 'phone_number','email','website_url','user_name','address','latitude','longitude','open_time','close_time','description','overall_ratings','no_of_ratings','type','is_recommended','city','hospital_logo','hospital_image', 'hospital_doctors']


# Bed Booking 
class BedBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BedBooking
        fields = [
            'customer', 'hospital', 'ward_type', 'bed_type', 'booking_type',
            'patient_name', 'email', 'age', 'contact_number', 'emergency_contact',
            'blood_group', 'medical_history', 'booking_reason', 'insurance_info',
            'admission_date', 'discharge_date', 'doctor_assigned', 'booking_date',
            'time_slot', 'notes', 'status'
        ]



class HospitalBedStatusSerializer(serializers.ModelSerializer):
    class Meta:
        pass


class HospitalFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalFacility
        fields = ['hospital','facility', 'icon']