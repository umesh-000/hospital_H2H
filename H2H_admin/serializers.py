from django.contrib.auth.hashers import make_password
from accounts import models as account_models
from H2H_admin import models as admin_models
from django.contrib.auth import authenticate
from rest_framework import serializers
from accounts.models import User


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    customer_name = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    dob = serializers.DateField(format='%Y-%m-%d', input_formats=['%Y-%m-%d'], required=False)
    gender = serializers.ChoiceField(choices=account_models.GENDER_CHOICES, required=False)

    class Meta:
        model = account_models.Customer
        fields = ['email', 'password', 'customer_name', 'phone_number', 'dob', 'gender']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate_phone_number(self, value):
        if account_models.Customer.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("A user with this phone number already exists.")
        return value

    def create(self, validated_data):
        user = User.objects.create( username=validated_data['email'], email=validated_data['email'], user_type='customer', password=make_password(validated_data['password']), )
        customer = account_models.Customer.objects.create( user=user, customer_name=validated_data['customer_name'], phone_number=validated_data['phone_number'], dob=validated_data.get('dob'), gender=validated_data.get('gender') )
        return customer

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(username=email, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User account is disabled.")
                return {'user': user}
            else:
                raise serializers.ValidationError("Invalid email or password.")
        raise serializers.ValidationError("Email and password are required.")
    
'''
------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------
'''

class DoctorSpecialistCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = admin_models.SpecialistCategory
        fields = ['id', 'category_name', 'category_image', 'status']

# Serialize DoctorDetails
class DoctorDetailsSerializer(serializers.ModelSerializer):
    specialist = DoctorSpecialistCategorySerializer(read_only=True)

    class Meta:
        model = account_models.DoctorDetails
        fields = [ 'id', 'dr_name', 'qualification', 'profile_img',  'gender', 'phone', 'experience' ,'profile_status', 'consultation_fee', 'rating', 'online_status', 'is_recommended','additional_qualification', 'medical_license', 'institution', 'graduation_year', 'dob', 'description', 'resume', 'medical_license_doc', 'certification', 'other', 'join_date', 'specialist' ]



# Serialize HospitalDoctors (nested doctor data)
class HospitalDoctorsSerializer(serializers.ModelSerializer):
    doctor = DoctorDetailsSerializer(read_only=True)

    class Meta:
        model = admin_models.HospitalDoctors
        fields = ['doctor']

# Serialize Hospital with nested HospitalDoctors
class HospitalSerializer(serializers.ModelSerializer):
    hospital_doctors = HospitalDoctorsSerializer(many=True, read_only=True)

    class Meta:
        model = account_models.Hospital
        fields = [ 'id', 'hospital_name', 'phone_number', 'website_url', 'address', 'latitude', 'longitude', 'open_time',  'close_time', 'description', 'overall_ratings', 'no_of_ratings', 'type', 'is_recommended', 'city', 'hospital_logo', 'hospital_image',  'hospital_doctors']


'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''
# getHospital_Details Serializer 
class HospitalFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = admin_models.HospitalFacility
        fields = ['hospital', 'facility', 'icon']

class HospitalServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = admin_models.HospitalService
        fields = ['hospital', 'service_name', 'service_icon', 'starting_from']

class HospitalImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = account_models.HospitalImage
        fields = ['image']

class HospitalDetailsSerializer(serializers.ModelSerializer):
    facilities = HospitalFacilitySerializer(many=True, read_only=True)
    services = HospitalServicesSerializer(many=True, read_only=True)
    images = HospitalImageSerializer(source='images.all', many=True, read_only=True)

    class Meta:
        model = account_models.Hospital
        fields = [ 'id', 'hospital_name', 'phone_number', 'website_url', 'address', 'latitude', 'longitude', 'open_time', 'close_time', 'description', 'overall_ratings','no_of_ratings', 'type', 'is_recommended', 'city', 'hospital_logo', 'hospital_image','facilities', 'services', 'images']
'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''

class SpecialistCategorySerializer(serializers.ModelSerializer):
    icon_url = serializers.SerializerMethodField()

    class Meta:
        model = admin_models.SpecialistCategory
        fields = ['id', 'category_name', 'category_image', 'icon_url']

    def get_icon_url(self, obj):
        request = self.context.get('request')
        if obj.category_image:
            return request.build_absolute_uri(obj.category_image.url)
        return None

'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''
# Symptom Serializer
class SymptomSerializer(serializers.ModelSerializer):
    icon_url = serializers.SerializerMethodField()

    class Meta:
        model = admin_models.Symptom
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
        model = admin_models.Ward
        fields = ['id', 'ward_name', 'status']
'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''


# Bed Booking 
class BedBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = admin_models.BedBooking
        fields = [ 'customer', 'hospital', 'ward_type', 'bed_type', 'booking_type', 'patient_name', 'email', 'age', 'contact_number', 'emergency_contact', 'blood_group', 
                'medical_history', 'booking_reason', 'insurance_info', 'admission_date', 'discharge_date', 'doctor_assigned', 'booking_date', 'time_slot', 'notes', 'status' ]

'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''

# class HospitalBedStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         pass

'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''
# class FeedbackCustomerSerializer(serializers.ModelSerializer):
#     profile_picture_url = serializers.SerializerMethodField()

#     class Meta:
#         model = account_models.Customer
#         fields = ['id', 'customer_name', 'profile_picture', 'profile_picture_url']

#     def get_profile_picture_url(self, obj):
#         request = self.context.get('request')
#         if obj.profile_picture:
#             return request.build_absolute_uri(obj.profile_picture.url)
#         return None


# class FeedbackSerializer(serializers.ModelSerializer):
#     customer = FeedbackCustomerSerializer()

#     class Meta:
#         model = account_models.Feedback
#         fields = ['id', 'customer_id', 'hospital_id', 'doctor_id', 'rating', 'feedback', 'lab_id', 'date', 'customer']


class DoctorSerializer(serializers.ModelSerializer):
    speciality = SpecialistCategorySerializer(source='specialist', read_only=True)
    # profile_image_url = serializers.SerializerMethodField()
    # feedbacks = FeedbackSerializer(many=True, read_only=True)

    class Meta:
        model = account_models.DoctorDetails
        fields = [
            'id', 'hospital_id', 'dr_name', 'qualification', 'profile_img', 'phone', 'gender', 
            'experience', 'rating', 'overall_ratings', 'profile_status', 'online_status', 'description', 'consultation_fee',  'speciality',
        ]

    def get_profile_image_url(self, obj):
        request = self.context.get('request')
        if obj.profile_img:
            return request.build_absolute_uri(obj.profile_img.url)
        return None
    

'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''
class ClinicCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = admin_models.ClinicCategory
        fields = ['id', 'name', 'status', 'created_at', 'updated_at']

'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''

class HospitalDoctorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = account_models.DoctorDetails
        fields = ['id', 'dr_name', 'dr_unique_code', 'qualification', 'phone', 'gender', 'experience', 'consultation_fee', 'profile_img', 'status', 'rating', 'online_status', 'description','join_date']

'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''
class ExpertTalkSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(source='doctor.dr_name', read_only=True)
    profile_image = serializers.ImageField(source='doctor.profile_img', read_only=True)
    qualification = serializers.CharField(source='doctor.qualification', read_only=True)
    profile_image_url = serializers.SerializerMethodField()

    class Meta:
        model = admin_models.ExpertTalk
        fields = ['id', 'comment', 'doctor_name', 'profile_image', 'qualification', 'profile_image_url']

    def get_profile_image_url(self, obj):
        if obj.doctor and obj.doctor.profile_img:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.doctor.profile_img.url)
        return None


'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''

class DoctorBannerSerializer(serializers.ModelSerializer):
    banner_url = serializers.SerializerMethodField()

    class Meta:
        model = admin_models.DoctorBanner
        fields = ['link', 'banner', 'position', 'banner_url']

    def get_banner_url(self, obj):
        request = self.context.get('request')
        if obj.banner and request:
            return request.build_absolute_uri(obj.banner.url)
        return None
    

'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''
class BannerSerializer(serializers.ModelSerializer):
    banner_url = serializers.SerializerMethodField()

    class Meta:
        model = admin_models.Banner
        fields = ['id', 'app_module', 'banner', 'link', 'position', 'banner_url']

    def get_banner_url(self, obj):
        request = self.context.get('request')
        if obj.banner and request:
            return request.build_absolute_uri(obj.banner.url)
        return None
'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''

class RecommentedHospitalImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = account_models.HospitalImage
        fields = ['image', 'image_url']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None

class RecommentedHospitalSerializer(serializers.ModelSerializer):
    images = RecommentedHospitalImageSerializer(many=True, read_only=True)
    hospital_image_url = serializers.SerializerMethodField()
    hospital_logo_url = serializers.SerializerMethodField()

    class Meta:
        model = account_models.Hospital
        fields = ['id', 'hospital_name', 'phone_number', 'latitude', 'longitude',  'type', 'address', 'city', 'description', 'hospital_image_url',  'hospital_logo_url', 'overall_ratings', 'no_of_ratings', 'is_recommended', 'images']

    def get_hospital_image_url(self, obj):
        request = self.context.get('request')
        if obj.hospital_image and request:
            return request.build_absolute_uri(obj.hospital_image.url)
        return None

    def get_hospital_logo_url(self, obj):
        request = self.context.get('request')
        if obj.hospital_logo and request:
            return request.build_absolute_uri(obj.hospital_logo.url)
        return None

'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = admin_models.Blog
        fields = [ "id", "title", "description","image", "video",  "created_at", "updated_at" ]


'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = admin_models.Service
        fields = ['id', 'service_name', 'status', 'created_at', 'updated_at']

'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = admin_models.Reminder
        fields = ['id', 'title', 'description', 'reminder_date', 'status', 'created_at', 'updated_at', 'category']

    

'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''
class AllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = admin_models.Allergy
        fields = ['id', 'name']

'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''
class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = admin_models.Medication
        fields = ['id', 'name'] 

'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''

class HelpDeskQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = admin_models.HelpDeskQuery
        fields = ['id', 'name', 'email', 'message', 'created_at', 'updated_at'] 

'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''
class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = account_models.Customer
        fields = ['id', 'customer_name', 'phone_number', 'profile_picture','pre_existing_disease', 'blood_group', 'gender', 'wallet','overall_ratings', 'no_of_ratings', 
        'status', 'dob', 'age','height', 'weight', 'emergency_contact_no', 'allergies','current_medications']

'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''
class markAs_Read_ReminderSerializer(serializers.ModelSerializer):
    status_label = serializers.SerializerMethodField()

    class Meta:
        model = admin_models.Reminder
        fields = ['id', 'customer_id', 'category_id', 'title', 'description', 'reminder_date', 'status', 'created_at', 'updated_at', 'status_label']

    def get_status_label(self, obj):
        return "Readed" if obj.status == 1 else "Unreaded"

'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''

class CustomerInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = admin_models.CustomerInsurance
        fields = ['insurance_company_id', 'insurance_company_name', 'insurance_type', 'start_date', 'end_date']
    
    def validate(self, data):
        if data['insurance_company_id'] is None and not data.get('insurance_company_name'):
            raise serializers.ValidationError("Insurance company name is required when company ID is null.")
        return data

'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''
class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = admin_models.FamilyMember
        fields = [ 'id', 'first_name', 'last_name', 'dob', 'age', 'relation', 'email', 'mobile_no', 'is_minor', 'gender', 'blood_group', 'medical_history']

'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''

class LaboratorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk')
    admin_user_id = serializers.IntegerField(source='user.id')
    lab_name = serializers.CharField()
    description = serializers.CharField()
    address = serializers.CharField()
    lab_image = serializers.SerializerMethodField()
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    phone_number = serializers.CharField(source='contact_number')
    password = serializers.CharField(source='user.password')
    latitude = serializers.DecimalField(max_digits=10, decimal_places=8, required=False)
    longitude = serializers.DecimalField(max_digits=10, decimal_places=8, required=False)
    state = serializers.CharField(source='state_province')
    city = serializers.CharField()
    postal_code = serializers.CharField()
    rating = serializers.DecimalField(max_digits=2, decimal_places=1, default=0)
    created_at = serializers.DateTimeField(source='user.created_at')
    updated_at = serializers.DateTimeField(source='user.updated_at')

    def get_lab_image(self, obj):
        if obj.lab_image:
            return obj.lab_image.url
        return None

    class Meta:
        model = account_models.Laboratory
        fields = [
            'id', 'admin_user_id', 'lab_name', 'description', 'address', 'lab_image', 'username', 'email', 'phone_number', 'password', 'latitude', 'longitude',
            'state', 'city', 'postal_code', 'rating', 'created_at', 'updated_at' ]

'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''

class LaboratoryDetailsSerializer(serializers.ModelSerializer):
    admin_user_id = serializers.IntegerField(source='user.id')
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    lab_image = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(source='user.created_at')
    updated_at = serializers.DateTimeField(source='user.updated_at')

    def get_lab_image(self, obj):
        request = self.context.get('request')
        if obj.lab_image and request:
            return request.build_absolute_uri(obj.lab_image.url)
        return None

    class Meta:
        model = account_models.Laboratory
        fields = [ 'id', 'admin_user_id','lab_name','username', 'email', 'address', 'contact_number', 'description', 'lab_image', 'city', 'postal_code', 'state_province', 'alternate_number', 'website', 
            'operating_hours', 'specializations', 'insurance_accepted', 'payment_methods', 'emergency_services', 'home_sample_collection', 'report_delivery_options', 
            'accreditations_certifications', 'latitude', 'longitude', 'lab_commission', 'promote','created_at','updated_at']

'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''

class LabPackageSerializer(serializers.ModelSerializer):
    relevance_name = serializers.CharField(source='lab_tag.tag_name', read_only=True)
    package_image = serializers.SerializerMethodField()

    class Meta:
        model = admin_models.LabPackage
        fields = [ 'id', 'lab_id', 'package_name', 'lab_specialization', 'lab_service', 'test_preparation','lab_tag', 'lab_price', 'sale_price','package_image', 'expected_delivery', 'promote','status','relevance_name',  'created_at', 'updated_at', ]

    def get_package_image(self, obj):
        request = self.context.get('request')
        if obj.package_img and request:
            return request.build_absolute_uri(obj.package_img.url)
        return None

'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''

class LabPackageDetailsSerializer(serializers.ModelSerializer):
    lab_name = serializers.CharField(source='lab.lab_name', read_only=True)
    relevance_name = serializers.CharField(source='lab_tag.tag_name', read_only=True)
    package_image = serializers.ImageField(source='package_img', read_only=True)

    class Meta:
        model = admin_models.LabPackage
        fields =  [ 'id', 'lab_id', 'package_name', 'lab_name', 'lab_specialization', 'lab_service', 'test_preparation','lab_tag', 'lab_price', 'sale_price','package_image', 'expected_delivery', 'promote','status','relevance_name',  'created_at', 'updated_at', ]


'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = admin_models.Address
        fields = ['id', 'customer', 'address', 'landmark', 'lat', 'lng', 'status', 'created_at', 'updated_at']
    
    def validate(self, data):
        try:
            account_models.Customer.objects.get(id=data['customer'].id)
        except account_models.Customer.DoesNotExist:
            raise serializers.ValidationError("Customer with the given ID does not exist.")
        return data

'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''


'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''


'''
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
'''