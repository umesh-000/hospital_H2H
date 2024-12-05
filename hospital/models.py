# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.contrib.auth.hashers import make_password
# from django.core.validators import MinValueValidator
# from django.utils import timezone
# from django.db import models
# from django.utils.text import slugify
# import os 



# class BedBooking(models.Model):
#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('reject', 'Reject'),
#         ('accepted', 'Accepted'),
#     ]

#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name='customer')
#     hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True, blank=True, related_name='bed_bookings')
#     ward_type = models.CharField(max_length=255)
#     bed_type = models.CharField(max_length=255)
#     booking_type = models.CharField(max_length=255)

#     patient_name = models.CharField(max_length=255)
#     email = models.EmailField()
#     age = models.IntegerField(validators=[MinValueValidator(0)])
#     contact_number = models.CharField(max_length=255)
#     emergency_contact = models.CharField(max_length=255, null=True, blank=True)
#     blood_group = models.CharField(max_length=255)
#     medical_history = models.TextField(null=True, blank=True)
#     booking_reason = models.CharField(max_length=255)
#     insurance_info = models.TextField(null=True, blank=True)
#     admission_date = models.DateField()
#     discharge_date = models.DateField(null=True, blank=True)
#     doctor_assigned = models.ForeignKey('doctor.DoctorDetails', on_delete=models.SET_NULL, null=True, blank=True, related_name='bed_bookings')
#     booking_date = models.DateTimeField(default=timezone.now)
#     time_slot = models.TimeField(null=True, blank=True)
#     notes = models.TextField(null=True, blank=True)
#     status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='pending')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'bed_bookings'

#     def __str__(self):
#         return f"Booking for {self.patient_name} at {self.hospital}"   

# class HospitalFeeSettings(models.Model):
#     hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, related_name='fee_settings', null=True, blank=True)
#     appointment_fee = models.DecimalField(max_digits=10, decimal_places=2)
#     consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
#     waiting_time = models.CharField(max_length=25)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f'{self.hospital} Fee Settings'


# class HospitalDoctors(models.Model):
#     STATUS_CHOICES = [
#         (1, 'Active'),
#         (0, 'Inactive'),
#     ]
#     hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True, blank=True, related_name='hospital_doctors')
#     doctor = models.ForeignKey('doctor.DoctorDetails', on_delete=models.SET_NULL, null=True, blank=True, related_name='doctor_hospitals')
#     unique_code = models.CharField(max_length=100)
#     join_date = models.DateField()
#     status = models.IntegerField(choices=STATUS_CHOICES, default=1)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'hospital_doctors'

#     def __str__(self):
#         return f"{self.unique_code} - {self.hospital} - {self.doctor}"


# class Insurance(models.Model):
#     STATUS_CHOICES = [
#         (1, 'Active'),
#         (0, 'Inactive'),
#     ]
    
#     insurance_name = models.CharField(max_length=150)
#     insurance_logo = models.ImageField(upload_to='hospital/insurance_logos/')
#     insurance_link = models.CharField(max_length=500)
#     status = models.IntegerField(choices=STATUS_CHOICES, default=1)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'insurances'

#     def __str__(self):
#         return self.insurance_name 


# class HospitalInsurance(models.Model):
#     STATUS_CHOICES = [
#         (1, 'Active'),
#         (0, 'Inactive'),
#     ]

#     hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True, blank=True, related_name='hospital_insurances')
#     insurance = models.ForeignKey(Insurance, on_delete=models.SET_NULL, null=True, blank=True, related_name='insurance_hospitals')
#     status = models.IntegerField(choices=STATUS_CHOICES, default=1)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'hospital_insurance'
#         unique_together = ('hospital', 'insurance')

#     def __str__(self):
#         return f"{self.hospital.hospital_name} - {self.insurance.insurance_name}"

# class HospitalPatient(models.Model):
#     hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
#     patient_name = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=20)   