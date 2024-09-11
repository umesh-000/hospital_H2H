from hospital.models import Hospital,BedBooking,HospitalDoctors,HospitalFacility,Customer,HospitalService,Ward, HospitalImage
from doctor.models import DoctorDetails,DoctorSpecialistCategory,Symptom
from django.contrib.auth import authenticate
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['phone_number', 'email', 'customer_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        customer = Customer.objects.create_user(
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            customer_name=validated_data.get('customer_name', ''),
            password=validated_data['password']
        )
        return customer


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        print("Data in validate:", data)
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                return {'user': user}
            else:
                raise serializers.ValidationError('Invalid email or password')
        raise serializers.ValidationError('Email and password are required')
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

class HospitalImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalImage
        fields = ['image']

class HospitalDetailsSerializer(serializers.ModelSerializer):
    facilities = HospitalFacilitySerializer(many=True, read_only=True)
    services = HospitalServicesSerializer(many=True, read_only=True)
    images = HospitalImageSerializer(source='images.all', many=True, read_only=True)

    class Meta:
        model = Hospital
        fields = [
            'id', 'hospital_name', 'phone_number', 'email', 'website_url', 'user_name', 'address',
            'latitude', 'longitude', 'open_time', 'close_time', 'description', 'overall_ratings',
            'no_of_ratings', 'type', 'is_recommended', 'city', 'hospital_logo', 'hospital_image',
            'facilities', 'services', 'images'
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
class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = ['id', 'ward_name', 'status']
'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''




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

