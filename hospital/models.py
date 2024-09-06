from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.db import models

class admin(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class CustomerManager(BaseUserManager):
    def create_user(self, phone_number, email=None, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The Phone Number must be set')
        email = self.normalize_email(email)
        user = self.model(phone_number=phone_number, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone_number, email, password, **extra_fields)
    
       
class Customer(AbstractBaseUser):
    email = models.EmailField(unique=True, null=True, blank=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=100, unique=True)
    remember_token = models.CharField(max_length=100, null=True, blank=True)
    profile_picture = models.ImageField(default='hospital/customer_profile//avatar.png',upload_to='hospital/customer_profile/')
    pre_existing_disease = models.TextField(null=True, blank=True)
    blood_group = models.CharField(max_length=10, null=True, blank=True)
    gender = models.IntegerField(null=True, blank=True)
    wallet = models.FloatField(default=0)
    overall_ratings = models.FloatField(default=0)
    no_of_ratings = models.IntegerField(default=0)
    status = models.IntegerField(default=1)
    fcm_token = models.TextField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    age = models.FloatField(null=True, blank=True)
    family_members = models.TextField(null=True, blank=True)
    last_active_address = models.IntegerField(default=0)
    height = models.CharField(max_length=20, null=True, blank=True)
    weight = models.CharField(max_length=20, null=True, blank=True)
    emergency_contact_no = models.CharField(max_length=255, null=True, blank=True)
    allergies = models.CharField(max_length=255, null=True, blank=True)
    current_medications = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    provider_id = models.CharField(max_length=255, null=True, blank=True)
    firebase_user_id = models.CharField(max_length=100, null=True, blank=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']

    objects = CustomerManager()

    def __str__(self):
        return self.phone_number




class Hospital(models.Model):
    HOSPITAL_TYPE_CHOICES = [
        ('hospital', 'Hospital'),
        ('clinic', 'Clinic'),
    ]

    STATUS_CHOICES = [
        (1, 'Active'),
        (0, 'Inactive'),
    ]

    RECOMMENDATION_CHOICES = [
        (0, 'No'),
        (1, 'Yes'),
    ]

    hospital_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    open_time = models.TimeField(null=True, blank=True)  
    close_time = models.TimeField(null=True, blank=True) 
    website_url = models.URLField(null=True, blank=True) 
    type = models.CharField(max_length=20, choices=HOSPITAL_TYPE_CHOICES)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    is_recommended = models.IntegerField(choices=RECOMMENDATION_CHOICES, default=0)
    address = models.TextField(null=True, blank=True) 
    description = models.TextField(null=True, blank=True)
    hospital_image = models.ImageField(upload_to='hospital/hospital_images/', null=True, blank=True)
    hospital_logo = models.ImageField(upload_to='hospital/hospital_logos/', null=True, blank=True)
    overall_ratings = models.FloatField(default=0)
    no_of_ratings = models.IntegerField(default=0)
    wallet = models.FloatField(default=0)
    city = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hospital_name


class Ward(models.Model):
    STATUS_CHOICES = [
        (1, 'Active'),
        (0, 'Inactive'),
    ]

    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, related_name='wards', null=True, blank=True)
    ward_name = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ward_name


class Bed(models.Model):
    STATUS_CHOICES = [
        (1, 'Active'),
        (0, 'Inactive'),
    ]

    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, related_name='beds',null=True, blank=True)
    ward = models.ForeignKey(Ward, on_delete=models.SET_NULL, related_name='beds',null=True, blank=True)
    bed_type = models.CharField(max_length=100)
    bed_count = models.IntegerField(validators=[MinValueValidator(0)])
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_bed_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.bed_type} - {self.ward.ward_name}'


class BedStatus(models.Model):
    STATUS_CHOICES = [
        (1, 'Assigned'),
        (0, 'Empty'),
    ]
    
    hospital = models.ForeignKey('Hospital', on_delete=models.SET_NULL, related_name='bed_statuses', null=True, blank=True)
    bed = models.ForeignKey('Bed', on_delete=models.SET_NULL, related_name='bed_statuses', null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.bed.bed_type} - {self.get_status_display()}'


class BedBooking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reject', 'Reject'),
        ('accepted', 'Accepted'),
    ]

    customer = models.IntegerField(default=1)
    hospital = models.ForeignKey('Hospital', on_delete=models.SET_NULL, null=True, blank=True, related_name='bed_bookings')
    ward_type = models.CharField(max_length=255)
    bed_type = models.CharField(max_length=255)
    booking_type = models.CharField(max_length=255)

    patient_name = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.IntegerField(validators=[MinValueValidator(0)])
    contact_number = models.CharField(max_length=255)
    emergency_contact = models.CharField(max_length=255, null=True, blank=True)
    blood_group = models.CharField(max_length=255)
    medical_history = models.TextField(null=True, blank=True)
    booking_reason = models.CharField(max_length=255)
    insurance_info = models.TextField(null=True, blank=True)
    admission_date = models.DateField()
    discharge_date = models.DateField(null=True, blank=True)
    doctor_assigned = models.ForeignKey("doctor.DoctorDetails", on_delete=models.SET_NULL, null=True, blank=True, related_name='bed_bookings')
    booking_date = models.DateTimeField(default=timezone.now)
    time_slot = models.TimeField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bed_bookings'

    def __str__(self):
        return f"Booking for {self.patient_name} at {self.hospital}"   

class HospitalFeeSettings(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, related_name='fee_settings', null=True, blank=True)
    appointment_fee = models.DecimalField(max_digits=10, decimal_places=2)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    waiting_time = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.hospital} Fee Settings'


class HospitalService(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, related_name='services', null=True, blank=True)
    service_name = models.CharField(max_length=255)
    service_icon = models.ImageField(upload_to='hospital/service_icons/', null=True, blank=True)
    starting_from = models.CharField(max_length=100,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.service_name

class HospitalDepartment(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True, blank=True, related_name='departments')
    image = models.ImageField(upload_to='hospital/department_images', null=True, blank=True)
    department_name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department_name


class HospitalFacility(models.Model):
    hospital = models.ForeignKey('Hospital', on_delete=models.SET_NULL, null=True, blank=True, related_name='facilities')
    icon = models.ImageField(upload_to='hospital/facility_icons/', blank=True, null=True)
    facility = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.facility} at {self.hospital}"

class HospitalDoctors(models.Model):
    STATUS_CHOICES = [
        (1, 'Active'),
        (0, 'Inactive'),
    ]
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True, blank=True, related_name='hospital_doctors')
    doctor = models.ForeignKey("doctor.DoctorDetails", on_delete=models.SET_NULL, null=True, blank=True, related_name='doctor_hospitals')
    unique_code = models.CharField(max_length=100)
    join_date = models.DateField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'hospital_doctors'

    def __str__(self):
        return f"{self.unique_code} - {self.hospital} - {self.doctor}"


class Insurance(models.Model):
    STATUS_CHOICES = [
        (1, 'Active'),
        (0, 'Inactive'),
    ]
    
    insurance_name = models.CharField(max_length=150)
    insurance_logo = models.ImageField(upload_to='hospital/insurance_logos/')
    insurance_link = models.CharField(max_length=500)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'insurances'

    def __str__(self):
        return self.insurance_name 


class HospitalInsurance(models.Model):
    STATUS_CHOICES = [
        (1, 'Active'),
        (0, 'Inactive'),
    ]

    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True, blank=True, related_name='hospital_insurances')
    insurance = models.ForeignKey(Insurance, on_delete=models.SET_NULL, null=True, blank=True, related_name='insurance_hospitals')
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'hospital_insurance'
        unique_together = ('hospital', 'insurance')

    def __str__(self):
        return f"{self.hospital.hospital_name} - {self.insurance.insurance_name}"

class HospitalPatient(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)   