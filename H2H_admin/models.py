from django.core.validators import MinValueValidator
from accounts.models import Laboratory
from django.utils import timezone
from django.db import models

# Create your models here.
STATUS_CHOICES = [
    (1, 'Active'),
    (0, 'Inactive'),
]
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]


class AppModule(models.Model):
    id = models.AutoField(primary_key=True)
    module_name = models.CharField(max_length=150)
    status = models.IntegerField(choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'app_module'

    def __str__(self):
        return self.module_name


class Banner(models.Model):
    POSITION_CHOICES = [ ('top', 'Top'), ('bottom', 'Bottom'),]
    app_module = models.ForeignKey(AppModule, on_delete=models.CASCADE, related_name='banners')
    banner = models.ImageField(upload_to='banners/', blank=True, null=True)
    link = models.CharField(max_length=250, null=True, blank=True)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES, default='top')
    status = models.IntegerField(choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'banners'

    def __str__(self):
        return f"Banner {self.id} - {self.position}"

class ModuleOfferBanner(models.Model):
    app_module = models.ForeignKey(AppModule, on_delete=models.CASCADE, related_name='offer_banners')
    banner = models.ImageField(upload_to='banners/', blank=True, null=True)
    link = models.CharField(max_length=250, null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'module_offer_banners'

    def __str__(self):
        return f"Offer Banner {self.id}"

class ExpertTalk(models.Model):
    doctor = models.ForeignKey( 'accounts.DoctorDetails', on_delete=models.CASCADE,  null=True, blank=True, related_name='expert_talks' )
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'expert_talks'
        verbose_name = 'Expert Talk'
        verbose_name_plural = 'Expert Talks'
    
    def __str__(self):
        return f"Expert Talk by {self.doctor} at {self.created_at}"

class Ward(models.Model):
    hospital = models.ForeignKey('accounts.Hospital', on_delete=models.SET_NULL, related_name='wards', null=True, blank=True)
    ward_name = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'wards'

    def __str__(self):
        return self.ward_name

class Bed(models.Model):
    hospital = models.ForeignKey('accounts.Hospital', on_delete=models.SET_NULL, related_name='beds',null=True, blank=True)
    ward = models.ForeignKey(Ward, on_delete=models.SET_NULL, related_name='beds',null=True, blank=True)
    bed_type = models.CharField(max_length=100)
    bed_count = models.IntegerField(validators=[MinValueValidator(0)])
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_bed_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'beds'

    def __str__(self):
        return f'{self.bed_type} - {self.ward.ward_name}'

class BedStatus(models.Model):
    STATUS_CHOICES = [
        (1, 'Assigned'),
        (0, 'Empty'),
    ]
    
    hospital = models.ForeignKey('accounts.Hospital', on_delete=models.SET_NULL, related_name='bed_statuses', null=True, blank=True)
    bed = models.ForeignKey(Bed, on_delete=models.SET_NULL, related_name='bed_statuses', null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bed_status'

    def __str__(self):
        return f'{self.bed.bed_type} - {self.get_status_display()}'


 
class HospitalService(models.Model):
    hospital = models.ForeignKey('accounts.Hospital', on_delete=models.SET_NULL, related_name='services', null=True, blank=True)
    service_name = models.CharField(max_length=255)
    service_icon = models.ImageField(upload_to='hospital/service_icons/', null=True, blank=True)
    starting_from = models.CharField(max_length=100,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'hospital_service'

    def __str__(self):
        return self.service_name

class HospitalDepartment(models.Model):
    hospital = models.ForeignKey('accounts.Hospital', on_delete=models.SET_NULL, null=True, blank=True, related_name='departments')
    image = models.ImageField(upload_to='hospital/department_images', null=True, blank=True)
    department_name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'hospital_department'

    def __str__(self):
        return self.department_name

class HospitalFacility(models.Model):
    hospital = models.ForeignKey('accounts.Hospital', on_delete=models.SET_NULL, null=True, blank=True, related_name='facilities')
    icon = models.ImageField(upload_to='hospital/facility_icons/', blank=True, null=True)
    facility = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'hospital_facility'

    def __str__(self):
        return f"{self.facility} at {self.hospital}"


class BedBooking(models.Model):
    STATUS_CHOICES = [ 
        ('confirmed', 'Confirmed'),
        ('checked_in', 'Checked In'),
        ('checked_out', 'Checked Out'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
         ]


    # ForeignKey fields referencing new models
    customer = models.ForeignKey('accounts.Customer', on_delete=models.SET_NULL, null=True, blank=True, related_name='bed_bookings')
    hospital = models.ForeignKey('accounts.Hospital', on_delete=models.SET_NULL, null=True, blank=True, related_name='bed_bookings')
    doctor_assigned = models.ForeignKey('accounts.DoctorDetails', on_delete=models.SET_NULL, null=True, blank=True, related_name='bed_bookings')

    # Booking details
    ward_type = models.CharField(max_length=255)
    bed_type = models.CharField(max_length=255)
    booking_type = models.CharField(max_length=255)

    # Patient information
    patient_name = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    contact_number = models.CharField(max_length=20)
    emergency_contact = models.CharField(max_length=20, null=True, blank=True)
    blood_group = models.CharField(max_length=10)
    medical_history = models.TextField(null=True, blank=True)
    booking_reason = models.CharField(max_length=255)
    insurance_info = models.TextField(null=True, blank=True)

    # Dates and times
    admission_date = models.DateField()
    discharge_date = models.DateField(null=True, blank=True)
    booking_date = models.DateTimeField(default=timezone.now)
    time_slot = models.TimeField(null=True, blank=True)

    # Additional details
    notes = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='in_progress')

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bed_bookings'

    def __str__(self):
        return f"Booking for {self.patient_name} at {self.hospital}"


class SpecialistCategory(models.Model):
    category_name = models.CharField(max_length=255)
    category_image = models.ImageField(upload_to='specialist_category_images/', blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'specialist_categories'

    def __str__(self):
        return self.category_name

class Symptom(models.Model):
    specialist = models.ForeignKey(SpecialistCategory, on_delete=models.SET_NULL, related_name='symptoms', null=True, blank=True)
    symptom_name = models.CharField(max_length=255)
    symptom_image = models.ImageField(upload_to='symptoms_images/', blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'symptoms'

    def __str__(self):
        return self.symptom_name

class HospitalDoctors(models.Model):
    STATUS_CHOICES = [
        (1, 'Active'),
        (0, 'Inactive'),
    ]
    hospital = models.ForeignKey('accounts.Hospital', on_delete=models.SET_NULL, null=True, blank=True, related_name='hospital_doctors')
    doctor = models.ForeignKey('accounts.DoctorDetails', on_delete=models.SET_NULL, null=True, blank=True, related_name='doctor_hospitals')
    unique_code = models.CharField(max_length=100)
    join_date = models.DateField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'hospital_doctors'

    def __str__(self):
        return f"{self.unique_code} - {self.hospital} - {self.doctor}"

class ClinicCategory(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'clinic_category'

    def __str__(self):
        return self.name

class DoctorClinics(models.Model):
    doctor = models.ForeignKey('accounts.DoctorDetails', on_delete=models.CASCADE, related_name='clinics')
    clinic_category = models.ForeignKey(ClinicCategory, on_delete=models.SET_NULL, null=True, blank=True)
    clinic_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    consultation_minutes = models.CharField(max_length=10, default='0')
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    latitude = models.FloatField(null=True, blank=True) 
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'doctor_clinics'

    def __str__(self):
        return f'{self.clinic_name} - {self.doctor.dr_name}'

class DoctorBanner(models.Model):
    POSITION_CHOICES = [ ('T', 'Top'),('B', 'Bottom'),]
    doctor = models.ForeignKey('accounts.DoctorDetails', on_delete=models.CASCADE, related_name='banners')
    link = models.URLField(max_length=255, null=True, blank=True)
    banner = models.ImageField(upload_to='doctors/banners/')
    position = models.CharField(max_length=50, choices=POSITION_CHOICES, default='B')
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'dr_banners'

    def __str__(self):
        return f"{self.doctor.dr_name} - {self.position}"
   
class LabTag(models.Model):
    tag_name = models.CharField(max_length=150) 
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        db_table = 'lab_tags'
        verbose_name = 'Lab Tag'
        verbose_name_plural = 'Lab Tags'

    def __str__(self):
        return self.tag_name
    
class Service(models.Model):
    service_name = models.CharField(max_length=150)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.service_name
    
    class Meta:
        db_table = 'services'

class LabService(models.Model):
    laboratory = models.ForeignKey('accounts.Laboratory', on_delete=models.CASCADE, related_name='lab_services')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='lab_services')
    is_emergency_service = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'lab_services'

    def __str__(self):
        return f"{self.laboratory.lab_name} - {self.service.service_name}"
    
class LabBanner(models.Model):
    laboratory = models.ForeignKey('accounts.Laboratory', on_delete=models.CASCADE, related_name='banners')
    link = models.URLField(max_length=250, blank=True, null=True)
    banner = models.ImageField(upload_to='laboratory/lab_banners/', verbose_name="Banner Image")
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'lab_banners'

    def __str__(self):
        return f"Banner for {self.laboratory.lab_name}"
    
class LabStaff(models.Model):
    STAFF_TYPE_CHOICES = [
        ('technician', 'Technician'),
        ('pathologist', 'Pathologist'),
        ('radiologist', 'Radiologist'),
        ('sample_collector', 'Sample Collector'),
    ]

    laboratory = models.ForeignKey('accounts.Laboratory',on_delete=models.CASCADE,related_name='lab_staff',verbose_name="Laboratory")
    name = models.CharField(max_length=150, verbose_name="Staff Name")
    phone = models.CharField(max_length=15, verbose_name="Phone Number")
    email = models.EmailField(max_length=150, unique=True, verbose_name="Email Address")
    profile_img = models.ImageField(upload_to='laboratory/staff_profiles/',blank=True,null=True,verbose_name="Profile Image")
    qualification = models.CharField(max_length=255, verbose_name="Qualification")
    experience = models.PositiveIntegerField(verbose_name="Years of Experience")
    staff_type = models.CharField(max_length=20,choices=STAFF_TYPE_CHOICES,verbose_name="Staff Type")
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        db_table = 'lab_staff'
        verbose_name = 'Lab Staff'
        verbose_name_plural = 'Lab Staff'

    def __str__(self):
        return f"{self.name} - {self.get_staff_type_display()} at {self.laboratory.lab_name}"

class LabPackage(models.Model):
    PROMOTE_CHOICES = [
        (1, 'Yes'),
        (0, 'No'),
    ]

    lab = models.ForeignKey('accounts.Laboratory', on_delete=models.CASCADE, related_name='lab_packages', verbose_name="Lab Center")
    lab_specialization = models.CharField(max_length=100, choices=Laboratory.SPECIALIZATION_CHOICES, blank=True, null=True, verbose_name="Lab Specialization")
    package_name = models.CharField(max_length=150, verbose_name="Package Name")
    lab_service = models.ForeignKey(LabService, on_delete=models.CASCADE, related_name='lab_packages', verbose_name="Lab Service")
    test_preparation = models.TextField(blank=True, null=True, verbose_name="Test Preparation Instructions")
    package_img = models.ImageField(upload_to='laboratory/packages/', blank=True, null=True, verbose_name="Package Image")
    expected_delivery = models.CharField(max_length=50, verbose_name="Expected Delivery")
    lab_tag = models.ForeignKey(LabTag, on_delete=models.CASCADE, related_name='lab_packages', verbose_name="Lab Tag")
    lab_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Lab Price")
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Sale Price")
    promote = models.IntegerField(choices=PROMOTE_CHOICES, default=0, verbose_name="Promote")
    status = models.IntegerField(choices=STATUS_CHOICES, default=0, verbose_name="Status")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'lab_packages'

    def __str__(self):
        return f"{self.package_name} - {self.lab.lab_name}"

class LabOrders(models.Model):
    STATUS_CHOICES = [
        (1, 'Order Placed'),
        (2, 'Confirmed'),
        (3, 'Collective Person Assigned'),
        (4, 'On Progress'),
        (5, 'Report Ready To Dispatch'),
        (6, 'Completed'),
    ]

    # Choices for booking type
    BOOKING_TYPE_CHOICES = [
        (1, 'Collect From Home'),
        (2, 'Lab Visit'),
    ]
    customer = models.ForeignKey('accounts.Customer', on_delete=models.CASCADE, related_name='lab_orders')
    lab = models.ForeignKey('accounts.Laboratory', on_delete=models.CASCADE, related_name='lab_orders')
    lab_staff = models.ForeignKey(LabStaff, on_delete=models.CASCADE, null=True, blank=True, related_name='lab_orders', verbose_name="Collective Person")
    patient_name = models.CharField(max_length=150)
    patient_dob = models.DateField()
    patient_gender = models.CharField(max_length=10)
    address_id = models.IntegerField() 
    promo_id = models.IntegerField()
    discount = models.FloatField()
    tax = models.FloatField()
    sub_total = models.FloatField()
    total = models.FloatField()
    special_instruction = models.CharField(max_length=250, null=True, blank=True)
    payment_mode = models.IntegerField()
    booking_type = models.IntegerField(choices=BOOKING_TYPE_CHOICES, default=1)
    items = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_by = models.IntegerField(null=True, blank=True)
    updated_by = models.IntegerField(null=True, blank=True)
    appointment_time = models.TimeField(null=True, blank=True)
    report = models.FileField(upload_to='lab/reports/', null=True, blank=True)
    appointment_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'lab_orders'
        verbose_name = 'Lab Order'
        verbose_name_plural = 'Lab Orders'

    def __str__(self):
        return f"Order {self.id} for Patient {self.patient_name}"
    
class LabOrderItems(models.Model):
    order = models.ForeignKey(LabOrders, on_delete=models.CASCADE, related_name='lab_order_items')
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=150)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'lab_order_items'
        verbose_name = 'Lab Order Item'
        verbose_name_plural = 'Lab Order Items'

    def __str__(self):
        return f"Item {self.item_name} for Order {self.order.id}"




class Blog(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    video = models.URLField(max_length=500, blank=True, null=True)  
    status = models.IntegerField(choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'blogs'

    def __str__(self):
        return self.title

class HelpDeskQuery(models.Model):
    customer = models.ForeignKey('accounts.Customer', on_delete=models.SET_NULL, null=True, blank=True, related_name='queries')
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'help_desk_queries'
        verbose_name = "Help Desk Query"
        verbose_name_plural = "Help Desk Queries"

    def __str__(self):
        return f"{self.name} - {self.email}"

class ReminderCategory(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES,default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reminder_categories'

    def __str__(self):
        return self.name


class Reminder(models.Model):
    customer = models.ForeignKey( 'accounts.Customer', on_delete=models.CASCADE, related_name='reminders')
    category = models.ForeignKey( ReminderCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='reminders' )
    title = models.CharField(max_length=255) 
    description = models.TextField(null=True, blank=True)
    reminder_date = models.DateTimeField()  
    status = models.IntegerField(choices=STATUS_CHOICES,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reminders'
        ordering = ['-created_at'] 

    def __str__(self):
        return self.title

class Allergy(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='allergies_images/', blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES,default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'allergies'

    def __str__(self):
        return self.name


class Medication(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='medications_images/', blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES,default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'medications'

    def __str__(self):
        return self.name


class Feedback(models.Model):
    customer = models.ForeignKey( 'accounts.Customer',  on_delete=models.SET_NULL,  null=True, blank=True, related_name='feedbacks')
    doctor = models.ForeignKey( 'accounts.DoctorDetails',  on_delete=models.SET_NULL,  null=True, blank=True, related_name='feedbacks')
    hospital = models.ForeignKey('accounts.Hospital', on_delete=models.SET_NULL, null=True, blank=True, related_name='feedbacks')
    lab = models.ForeignKey('accounts.Laboratory', on_delete=models.SET_NULL, null=True, blank=True, related_name='feedbacks')
    feedback = models.TextField()
    rating = models.FloatField(null=True, blank=True)
    admin_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'feedback'
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

    def __str__(self):
        return f"Feedback by {self.customer} - Rating: {self.rating}"

class CustomerInsurance(models.Model):
    customer = models.ForeignKey('accounts.Customer', on_delete=models.CASCADE, related_name='insurances')
    insurance_company_id = models.IntegerField(null=True, blank=True)
    insurance_company_name = models.CharField(max_length=255, null=True, blank=True)
    insurance_type = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'customer_insurances'

    def __str__(self):
        return f"Insurance for {self.customer.customer_name} with {self.insurance_company_name}"


class FamilyMember(models.Model):
    customer = models.ForeignKey('accounts.Customer', on_delete=models.CASCADE, related_name="family_members", null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    relation = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    mobile_no = models.CharField(max_length=15, null=True, blank=True)
    is_minor = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    blood_group = models.CharField(max_length=20, null=True, blank=True)
    medical_history = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'family_members'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.relation})"

class Address(models.Model):
    customer = models.ForeignKey('accounts.Customer',on_delete=models.CASCADE, related_name='addresses')
    address = models.TextField()
    landmark = models.CharField(max_length=150)
    lat = models.CharField(max_length=250)
    lng = models.CharField(max_length=250)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'addresses'

    def __str__(self):
        return f"{self.address} ({self.customer.user.email})"


# Choices for transaction type and type
TRANSACTION_TYPE_CHOICES = [('customer added amount', 'Customer added amount'),('refund amount', 'Refund amount'),('deducted amount', 'Deducted amount')]
TYPE_CHOICES = [('credit', 'Credit'),('debit', 'Debit'),]
class CustomerWalletHistory(models.Model):
    customer = models.ForeignKey('accounts.Customer', on_delete=models.CASCADE, related_name='wallet_histories')
    message = models.TextField()
    transaction_type = models.CharField(max_length=20,choices=TYPE_CHOICES)
    transaction_type_choices = models.CharField(max_length=30,choices=TRANSACTION_TYPE_CHOICES)
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'customer_wallet_histories'

    def __str__(self):
        return f'{self.customer.user.email} - {self.get_transaction_type_display()} - {self.amount}'

class DoctorBooking(models.Model):
    STATUS_CHOICES = [
        ('confirm', 'Confirm'),
        ('complete', 'Complete'),
        ('cancelled', 'Cancelled'),
        ('pending', 'Pending'),
    ]
    booking_number = models.CharField(max_length=50, null=True, blank=True)
    doctor = models.ForeignKey('accounts.DoctorDetails', on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings')
    clinic = models.ForeignKey(DoctorClinics, on_delete=models.SET_NULL, null=True, blank=True, related_name='clinic_bookings')
    customer = models.ForeignKey('accounts.Customer', on_delete=models.CASCADE, related_name='doctor_bookings')
    booking_for = models.CharField(max_length=10, null=True, blank=True)
    patient_name = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.IntegerField(null=True, blank=True)
    contact_number = models.CharField(max_length=255, null=True, blank=True)
    emergency_contact = models.CharField(max_length=255, null=True, blank=True)
    blood_group = models.CharField(max_length=255)
    medical_history = models.TextField(null=True, blank=True)
    current_symptoms = models.CharField(max_length=255, null=True, blank=True)
    booking_date = models.DateField(null=True, blank=True)
    time_slot = models.TimeField(null=True, blank=True)
    consultation_charge = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    base_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    additional_charges = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    final_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payment_mode = models.CharField(max_length=50, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=255,choices=STATUS_CHOICES,default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'doctor_bookings'
        verbose_name = "Doctor Booking"
        verbose_name_plural = "Doctor Bookings"

    def __str__(self):
        return f"Booking {self.booking_number} - {self.patient_name}"

class FcmNotification(models.Model):
    slug = models.CharField(max_length=50, unique=True)
    customer_title = models.CharField(max_length=100)
    customer_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'fcm_notifications'
        verbose_name = 'FCM Notification'
        verbose_name_plural = 'FCM Notifications'

    def __str__(self):
        return f"Notification: {self.slug} (Customer: {self.customer_title})"
    

class Notification(models.Model):
    STATUS_CHOICES = [(0, 'Active'),(1, 'Inactive'),]
    customer = models.ForeignKey('accounts.Customer', on_delete=models.SET_NULL, null=True, blank=True, related_name='notifications')
    app_module = models.ForeignKey('AppModule',on_delete=models.CASCADE,related_name='notifications', null=True, blank=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='notifications_images/', blank=True, null=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=0)
    meta = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'notifications'
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    def __str__(self):
        return f"Notification: {self.title} (Status: {'Active' if self.status else 'Inactive'})"
