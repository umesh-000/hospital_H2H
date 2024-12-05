from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.db import models
import os

# Choices
STATUS_CHOICES = [(1, 'Active'),(0, 'Inactive'),]
USER_TYPE_CHOICES = (('admin', 'Admin'),('customer', 'Customer'),('hospital', 'Hospital'),('lab', 'Lab'),('doctor', 'Doctor'),)
GENDER_CHOICES = [ ('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ]

# Custom User model
class User(AbstractUser):
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'all_users'

# Admin model
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_profile')
    profile_image = models.ImageField(upload_to='admin/profiles/', blank=True, null=True)

    class Meta:
        db_table = 'admin'


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    profile_picture = models.ImageField(default='hospital/customer_profile/avatar.png', upload_to='customers/profiles/', blank=True, null=True)
    pre_existing_disease = models.TextField(null=True, blank=True)
    blood_group = models.CharField(max_length=10, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,null=True, blank=True)
    wallet = models.FloatField(default=0)
    overall_ratings = models.FloatField(default=0)
    no_of_ratings = models.IntegerField(default=0)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    dob = models.DateField(null=True, blank=True)
    age = models.FloatField(null=True, blank=True)
    height = models.CharField(max_length=20, null=True, blank=True)
    weight = models.CharField(max_length=20, null=True, blank=True)
    emergency_contact_no = models.CharField(max_length=255, null=True, blank=True)
    allergies = models.CharField(max_length=255, null=True, blank=True)
    current_medications = models.CharField(max_length=255, null=True, blank=True)
    class Meta:
        db_table = 'customers'

    def __str__(self):
        return self.user.email

# Hospital model
class Hospital(models.Model):
    HOSPITAL_TYPE_CHOICES = [ ('hospital', 'Hospital'), ('clinic', 'Clinic'), ]
    RECOMMENDATION_CHOICES = [ (0, 'No'), (1, 'Yes'), ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hospital_profile')
    hospital_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    latitude = models.CharField(max_length=50,null=True, blank=True)
    longitude = models.CharField(max_length=50,null=True, blank=True)
    open_time = models.TimeField(null=True, blank=True)  
    close_time = models.TimeField(null=True, blank=True) 
    website_url = models.URLField(null=True, blank=True) 
    type = models.CharField(max_length=20, choices=HOSPITAL_TYPE_CHOICES)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    is_recommended = models.IntegerField(choices=RECOMMENDATION_CHOICES, default=0)
    address = models.TextField(null=True, blank=True) 
    city = models.CharField(max_length=50,null=True, blank=True) 
    description = models.TextField(null=True, blank=True)
    hospital_image = models.ImageField(upload_to='hospital/hospital_images/', null=True, blank=True)
    hospital_logo = models.ImageField(upload_to='hospital/hospital_logos/', null=True, blank=True)
    overall_ratings = models.FloatField(default=0)
    no_of_ratings = models.IntegerField(default=0)
    wallet = models.FloatField(default=0)
    class Meta:
        db_table = 'hospitals'
    def __str__(self):
        return self.hospital_name

class HospitalImage(models.Model):
    hospital = models.ForeignKey(Hospital, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hospital/hospital_images/')

    class Meta:
        db_table = 'hospital_images'
        
    def get_upload_to(self, filename):
        hospital_name_slug = slugify(self.hospital.hospital_name)
        return os.path.join('hospital', 'hospital_images', hospital_name_slug)
    def save(self, *args, **kwargs):
        self._meta.get_field('image').upload_to = self.get_upload_to(self.image.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return f"Image for {self.hospital.hospital_name}"

# Laboratory model
class Laboratory(models.Model):
    PROMOTE_CHOICES = [
        (1, 'Yes'),
        (0, 'No'),
    ]

    SPECIALIZATION_CHOICES = [
        ('pediatric_diagnostics', 'Pediatric Diagnostics'),
        ('cardiac_diagnostics', 'Cardiac Diagnostics'),
        ('general_practice', 'General Practice'),
    ]

    REPORT_DELIVERY_CHOICES = [
        ('Online', 'Online'),
        ('Email', 'Email'),
        ('Physical Copy', 'Physical Copy'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('Credit Card', 'Credit Card'),
        ('Debit Card', 'Debit Card'),
        ('Cash', 'Cash'),
    ]

    EMERGENCY_SERVICE_CHOICES = [
        (1, 'Yes'),
        (0, 'No'),
    ]

    HOME_SAMPLE_COLLECTION_CHOICES = [
        (1, 'Yes'),
        (0, 'No'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='lab_profile')
    lab_name = models.CharField(max_length=150)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    description = models.TextField()
    lab_image = models.ImageField(upload_to='laboratory/images/', blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    state_province = models.CharField(max_length=100)
    alternate_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Alternate Number")
    website = models.URLField(max_length=200, blank=True, null=True)
    operating_hours = models.CharField(max_length=100)
    specializations = models.CharField(max_length=100, choices=SPECIALIZATION_CHOICES, blank=True, null=True)
    insurance_accepted = models.TextField(blank=True, null=True)
    payment_methods = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES)
    emergency_services = models.IntegerField(choices=EMERGENCY_SERVICE_CHOICES, default=0)
    home_sample_collection = models.IntegerField(choices=HOME_SAMPLE_COLLECTION_CHOICES, default=0)
    report_delivery_options = models.CharField(max_length=20, choices=REPORT_DELIVERY_CHOICES)
    accreditations_certifications = models.TextField(blank=True, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    lab_commission = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    promote = models.IntegerField(choices=PROMOTE_CHOICES, default=0, verbose_name="Promote")

    class Meta:
        db_table = 'laboratories'

    def __str__(self):
        return self.lab_name

# Doctor model
class DoctorDetails(models.Model):
    PROFILE_STATUS_CHOICES = [
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('R', 'Rejected'),
    ]
    
    ONLINE_STATUS_CHOICES = [
        ('O', 'Online'),
        ('F', 'Offline'),
    ]
    
    RECOMMENDATION_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, related_name='doctors', null=True, blank=True)
    dr_name = models.CharField(max_length=255)
    dr_unique_code = models.CharField(max_length=50, unique=True)
    qualification = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    experience = models.PositiveIntegerField(default=1)
    profile_status = models.CharField(max_length=1, choices=PROFILE_STATUS_CHOICES, default='P')
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    profile_img = models.ImageField(upload_to='doctors/doctor_profiles/', blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=1)

    specialist = models.ForeignKey('H2H_admin.SpecialistCategory', on_delete=models.SET_NULL, related_name='doctors', null=True, blank=True)
    sub_specialist = models.CharField(max_length=100, null=True, blank=True)
    additional_qualification = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    overall_ratings = models.FloatField(default=0)
    document_update_status = models.IntegerField(default=0)
    document_approve_status = models.CharField(max_length=1, choices=PROFILE_STATUS_CHOICES, default='P')

    online_status = models.CharField(max_length=1, choices=ONLINE_STATUS_CHOICES, default='F')
    medical_license = models.CharField(max_length=100, unique=True)
    institution = models.CharField(max_length=255)
    graduation_year = models.PositiveIntegerField()
    dob = models.DateField()
    wallet = models.FloatField(default=0)
    earnings = models.FloatField(default=0)
    description = models.TextField(blank=True, null=True)
    is_recommended = models.CharField(max_length=1, choices=RECOMMENDATION_CHOICES, default='N')
    resume = models.ImageField(upload_to='doctors/doctor_documents/', blank=True, null=True)  
    medical_license_doc = models.ImageField(upload_to='doctors/doctor_documents/', blank=True, null=True)  
    certification = models.ImageField(upload_to='doctors/doctor_documents/', blank=True, null=True)  
    other = models.ImageField(upload_to='doctors/doctor_documents/', blank=True, null=True)  
    join_date= models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'doctors'
    def __str__(self):
        return self.dr_name