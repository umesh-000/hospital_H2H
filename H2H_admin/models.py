from django.db import models

# Create your models here.
class Laboratory(models.Model):
    STATUS_CHOICES = [
        (1, 'Active'),
        (0, 'Inactive'),
    ]

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

    lab_name = models.CharField(max_length=150, verbose_name="Center Name (or Lab Name)")
    address = models.TextField()
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=15, verbose_name="Contact Number (or Phone Number)")
    alternate_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Alternate Number")
    email = models.EmailField(max_length=150, verbose_name="Email (or Email Address)")
    website = models.URLField(max_length=200, blank=True, null=True)
    operating_hours = models.CharField(max_length=100)
    specializations = models.CharField(max_length=100, choices=SPECIALIZATION_CHOICES, blank=True, null=True)
    description = models.TextField(verbose_name="About the Center (or Description)")
    insurance_accepted = models.TextField(blank=True, null=True)
    payment_methods = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES)
    emergency_services = models.IntegerField(choices=EMERGENCY_SERVICE_CHOICES, default=0)
    home_sample_collection = models.IntegerField(choices=HOME_SAMPLE_COLLECTION_CHOICES, default=0)
    report_delivery_options = models.CharField(max_length=20, choices=REPORT_DELIVERY_CHOICES)
    lab_image = models.ImageField(upload_to='laboratory/images/', blank=True, null=True, verbose_name="Photos of Lab Center (or Lab Image)")
    accreditations_certifications = models.TextField(blank=True, null=True)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    lab_commission = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    promote = models.IntegerField(choices=PROMOTE_CHOICES, default=0, verbose_name="Promote")
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'laboratories'

    def __str__(self):
        return self.lab_name
    


class LabTag(models.Model):
    STATUS_CHOICES = [
        (1, 'Active'),
        (0, 'Inactive'),
    ]
    
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
    STATUS_CHOICES = [
        (1, 'Active'),
        (0, 'Inactive'),
    ]
    service_name = models.CharField(max_length=150)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.service_name
    
    class Meta:
        db_table = 'services'


class LabService(models.Model):
    STATUS_CHOICES = [
        (1, 'Active'),
        (0, 'Inactive'),
    ]
    
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE, related_name='lab_services')
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
    STATUS_CHOICES = [
        (1, 'Active'),
        (0, 'Inactive'),
    ]
    laboratory = models.ForeignKey('Laboratory', on_delete=models.CASCADE, related_name='banners')
    link = models.URLField(max_length=250, blank=True, null=True)
    banner = models.ImageField(upload_to='laboratory/lab_banners/', verbose_name="Banner Image")
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'lab_banners'

    def __str__(self):
        return f"Banner for {self.laboratory.lab_name}"