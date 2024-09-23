# Generated by Django 4.2.14 on 2024-09-21 06:43

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('customer_name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('remember_token', models.CharField(blank=True, max_length=100, null=True)),
                ('profile_picture', models.ImageField(default='hospital/customer_profile/avatar.png', upload_to='hospital/customer_profile/')),
                ('pre_existing_disease', models.TextField(blank=True, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.IntegerField(blank=True, null=True)),
                ('wallet', models.FloatField(default=0)),
                ('overall_ratings', models.FloatField(default=0)),
                ('no_of_ratings', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=1)),
                ('fcm_token', models.TextField(blank=True, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('age', models.FloatField(blank=True, null=True)),
                ('family_members', models.TextField(blank=True, null=True)),
                ('last_active_address', models.IntegerField(default=0)),
                ('height', models.CharField(blank=True, max_length=20, null=True)),
                ('weight', models.CharField(blank=True, max_length=20, null=True)),
                ('emergency_contact_no', models.CharField(blank=True, max_length=255, null=True)),
                ('allergies', models.CharField(blank=True, max_length=255, null=True)),
                ('current_medications', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('provider_id', models.CharField(blank=True, max_length=255, null=True)),
                ('firebase_user_id', models.CharField(blank=True, max_length=100, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed_type', models.CharField(max_length=100)),
                ('bed_count', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sale_bed_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=255)),
                ('user_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('latitude', models.CharField(blank=True, max_length=50, null=True)),
                ('longitude', models.CharField(blank=True, max_length=50, null=True)),
                ('open_time', models.TimeField(blank=True, null=True)),
                ('close_time', models.TimeField(blank=True, null=True)),
                ('website_url', models.URLField(blank=True, null=True)),
                ('type', models.CharField(choices=[('hospital', 'Hospital'), ('clinic', 'Clinic')], max_length=20)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=1)),
                ('is_recommended', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0)),
                ('address', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('hospital_image', models.ImageField(blank=True, null=True, upload_to='hospital/hospital_images/')),
                ('hospital_logo', models.ImageField(blank=True, null=True, upload_to='hospital/hospital_logos/')),
                ('overall_ratings', models.FloatField(default=0)),
                ('no_of_ratings', models.IntegerField(default=0)),
                ('wallet', models.FloatField(default=0)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_name', models.CharField(max_length=150)),
                ('insurance_logo', models.ImageField(upload_to='hospital/insurance_logos/')),
                ('insurance_link', models.CharField(max_length=500)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'insurances',
            },
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward_name', models.CharField(max_length=255)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wards', to='hospital.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='HospitalService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=255)),
                ('service_icon', models.ImageField(blank=True, null=True, upload_to='hospital/service_icons/')),
                ('starting_from', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services', to='hospital.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='HospitalPatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='HospitalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='hospital/hospital_images/')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='hospital.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='HospitalFeeSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('consultation_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('waiting_time', models.CharField(max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fee_settings', to='hospital.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='HospitalFacility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='hospital/facility_icons/')),
                ('facility', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='facilities', to='hospital.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='HospitalDoctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_code', models.CharField(max_length=100)),
                ('join_date', models.DateField()),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hospital_doctors', to='hospital.hospital')),
            ],
            options={
                'db_table': 'hospital_doctors',
            },
        ),
        migrations.CreateModel(
            name='HospitalDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='hospital/department_images')),
                ('department_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='departments', to='hospital.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='BedStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Assigned'), (0, 'Empty')], default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bed_statuses', to='hospital.bed')),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bed_statuses', to='hospital.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='BedBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward_type', models.CharField(max_length=255)),
                ('bed_type', models.CharField(max_length=255)),
                ('booking_type', models.CharField(max_length=255)),
                ('patient_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('contact_number', models.CharField(max_length=255)),
                ('emergency_contact', models.CharField(blank=True, max_length=255, null=True)),
                ('blood_group', models.CharField(max_length=255)),
                ('medical_history', models.TextField(blank=True, null=True)),
                ('booking_reason', models.CharField(max_length=255)),
                ('insurance_info', models.TextField(blank=True, null=True)),
                ('admission_date', models.DateField()),
                ('discharge_date', models.DateField(blank=True, null=True)),
                ('booking_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('time_slot', models.TimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('reject', 'Reject'), ('accepted', 'Accepted')], default='pending', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer', to=settings.AUTH_USER_MODEL)),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bed_bookings', to='hospital.hospital')),
            ],
            options={
                'db_table': 'bed_bookings',
            },
        ),
        migrations.AddField(
            model_name='bed',
            name='hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='beds', to='hospital.hospital'),
        ),
        migrations.AddField(
            model_name='bed',
            name='ward',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='beds', to='hospital.ward'),
        ),
        migrations.CreateModel(
            name='HospitalInsurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hospital_insurances', to='hospital.hospital')),
                ('insurance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='insurance_hospitals', to='hospital.insurance')),
            ],
            options={
                'db_table': 'hospital_insurance',
                'unique_together': {('hospital', 'insurance')},
            },
        ),
    ]
