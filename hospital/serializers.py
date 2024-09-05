from hospital.models import Hospital,BedBooking,HospitalDoctors,HospitalFacility,Customer,HospitalService
from doctor.models import DoctorDetails,DoctorSpecialistCategory,Symptom
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Customer
        fields = ['customer_name', 'phone_number', 'email', 'password']

    def create(self, validated_data):
        customer = Customer.objects.create_user(
            phone_number=validated_data['phone_number'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return customer

class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        phone_number = data.get('phone_number')
        password = data.get('password')
        customer = authenticate(phone_number=phone_number, password=password)

        if customer is None:
            raise serializers.ValidationError('Invalid phone number or password')

        data['customer'] = customer
        return data

    def get_token(self, customer):
        refresh = RefreshToken.for_user(customer)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }



'''
------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------
'''

# Get All Hospital Details List Serializer
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


'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''
# getHospital_Details Serializer 
class HospitalFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalFacility
        fields = ['hospital', 'facility', 'icon']

class HospitalServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalService
        fields = ['hospital', 'service_name', 'service_icon', 'starting_from']

class HospitalDetailsSerializer(serializers.ModelSerializer):
    facilities = HospitalFacilitySerializer(many=True, read_only=True)
    services = HospitalServicesSerializer(many=True, read_only=True)

    class Meta:
        model = Hospital
        fields = [
            'id', 'hospital_name', 'phone_number', 'email', 'website_url', 'user_name', 'address',
            'latitude', 'longitude', 'open_time', 'close_time', 'description', 'overall_ratings',
            'no_of_ratings', 'type', 'is_recommended', 'city', 'hospital_logo', 'hospital_image',
            'facilities', 'services'
        ]
'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''

# Get Specialist Serializer 
class SpecialistCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorSpecialistCategory
        fields = ['id', 'category_name', 'category_image']
'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''
# Symptom Serializer
class SymptomSerializer(serializers.ModelSerializer):
    icon_url = serializers.SerializerMethodField()

    class Meta:
        model = Symptom
        fields = ['id', 'symptom_name', 'symptom_image', 'icon_url']

    def get_icon_url(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.symptom_image.url)
        return None
'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''

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

