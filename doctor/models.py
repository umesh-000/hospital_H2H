from django.db import models


class DoctorSpecialistCategory(models.Model):
    STATUS_CHOICES = [
        (1, 'Active'),
        (0, 'Inactive'),
    ]
    
    category_name = models.CharField(max_length=255)
    category_image = models.ImageField(upload_to='doctors/doctor_specialist_category_images/', blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name

class Symptom(models.Model):
    STATUS_CHOICES = [
        (1, 'Active'),
        (0, 'Inactive'),
    ]

    specialist = models.ForeignKey(DoctorSpecialistCategory, on_delete=models.SET_NULL, related_name='symptoms', null=True, blank=True)
    symptom_name = models.CharField(max_length=255)
    symptom_image = models.ImageField(upload_to='doctors/symptom_images/', blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.symptom_name
    

class DoctorDetails(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    STATUS_CHOICES = [
        ('A', 'Active'),
        ('I', 'Inactive'),
    ]
    
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

    hospital = models.ForeignKey('hospital.Hospital', on_delete=models.SET_NULL, related_name='doctors', null=True, blank=True)
    dr_name = models.CharField(max_length=255)
    dr_unique_code = models.CharField(max_length=50, unique=True)
    qualification = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    dr_username = models.CharField(max_length=100, unique=True)
    experience = models.PositiveIntegerField(default=1)
    specialist = models.ForeignKey(DoctorSpecialistCategory, on_delete=models.SET_NULL, related_name='doctors', null=True, blank=True)
    sub_specialist = models.CharField(max_length=100, null=True, blank=True)
    additional_qualification = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    overall_ratings = models.FloatField(default=0)
    document_update_status = models.IntegerField(default=0)
    document_approve_status = models.CharField(max_length=1, choices=PROFILE_STATUS_CHOICES, default='P')
    profile_status = models.CharField(max_length=1, choices=PROFILE_STATUS_CHOICES, default='P')
    online_status = models.CharField(max_length=1, choices=ONLINE_STATUS_CHOICES, default='F')
    medical_license = models.CharField(max_length=100, unique=True)
    institution = models.CharField(max_length=255)
    graduation_year = models.PositiveIntegerField()
    dob = models.DateField()
    join_date = models.DateField(auto_now_add=True)
    c_id = models.IntegerField(default=0)
    c_stat = models.IntegerField(default=0)
    wallet = models.FloatField(default=0)
    earnings = models.FloatField(default=0)
    description = models.TextField(blank=True, null=True)
    fcm_token = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')
    is_recommended = models.CharField(max_length=1, choices=RECOMMENDATION_CHOICES, default='N')
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    profile_img = models.ImageField(upload_to='doctors/doctor_profiles/', blank=True, null=True)
    resume = models.ImageField(upload_to='doctors/doctor_documents/', blank=True, null=True)  
    medical_license_doc = models.ImageField(upload_to='doctors/doctor_documents/', blank=True, null=True)  
    certification = models.ImageField(upload_to='doctors/doctor_documents/', blank=True, null=True)  
    other = models.ImageField(upload_to='doctors/doctor_documents/', blank=True, null=True)  


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.dr_name

class DoctorBanner(models.Model):
    POSITION_CHOICES = [
        ('T', 'Top'),
        ('B', 'Bottom'),
    ]

    STATUS_CHOICES = [
        (0, 'Inactive'),
        (1, 'Active'),
    ]

    doctor = models.ForeignKey(DoctorDetails, on_delete=models.CASCADE, related_name='banners')
    link = models.URLField(max_length=255, null=True, blank=True)
    banner = models.ImageField(upload_to='doctors/banners/')
    position = models.CharField(max_length=50, choices=POSITION_CHOICES, default='B')
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.doctor.dr_name} - {self.position}"



class ClinicCategory(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class DoctorClinics(models.Model):
    doctor = models.ForeignKey(DoctorDetails, on_delete=models.CASCADE, related_name='clinics')
    clinic_category = models.ForeignKey(ClinicCategory, on_delete=models.SET_NULL, null=True, blank=True)
    clinic_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    consultation_minutes = models.CharField(max_length=10, default='0')
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    status = models.IntegerField(default=0)
    latitude = models.FloatField(null=True, blank=True) 
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.clinic_name} - {self.doctor.dr_name}'    