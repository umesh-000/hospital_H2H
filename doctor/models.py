# from django.db import models





    
    
# class DoctorBooking(models.Model):
#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('accepted', 'Accept'),
#         ('rejected', 'Reject'),
#         ('cancelled', 'Cancelled'),
#         ('successful', 'Successful'),
#     ]

#     booking_number = models.CharField(max_length=50, null=True, blank=True)
#     doctor = models.ForeignKey('accounts.DoctorDetails', on_delete=models.SET_NULL, null=True, blank=True)
#     clinic = models.ForeignKey(DoctorClinics, on_delete=models.SET_NULL, null=True, blank=True)
#     customer = models.ForeignKey('hospital.Customer', on_delete=models.CASCADE)

#     booking_for = models.CharField(max_length=10, null=True, blank=True)
#     patient_name = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255)
#     age = models.IntegerField(null=True, blank=True)
#     contact_number = models.CharField(max_length=255, null=True, blank=True)
#     emergency_contact = models.CharField(max_length=255, null=True, blank=True)
#     blood_group = models.CharField(max_length=255)
#     medical_history = models.TextField(null=True, blank=True)
#     current_symptoms = models.CharField(max_length=255, null=True, blank=True)

#     booking_date = models.DateField(null=True, blank=True)
#     time_slot = models.TimeField(null=True, blank=True)
#     consultation_charge = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     base_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     additional_charges = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     final_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

#     payment_mode = models.CharField(max_length=50, null=True, blank=True)
#     notes = models.TextField(null=True, blank=True)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"Booking {self.booking_number} for {self.patient_name}"
    
#     def get_status_display(self):
#         return dict(self.STATUS_CHOICES).get(self.status, 'Unknown')