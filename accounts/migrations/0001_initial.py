# Generated by Django 4.2.16 on 2024-11-18 12:12

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
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
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('admin', 'Admin'), ('customer', 'Customer'), ('hospital', 'Hospital'), ('lab', 'Lab'), ('doctor', 'Doctor')], max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'all_users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
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
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hospital_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'hospitals',
            },
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_name', models.CharField(max_length=150)),
                ('address', models.TextField()),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=150)),
                ('description', models.TextField()),
                ('lab_image', models.ImageField(blank=True, null=True, upload_to='laboratory/images/')),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('state_province', models.CharField(max_length=100)),
                ('alternate_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Alternate Number')),
                ('website', models.URLField(blank=True, null=True)),
                ('operating_hours', models.CharField(max_length=100)),
                ('specializations', models.CharField(blank=True, choices=[('pediatric_diagnostics', 'Pediatric Diagnostics'), ('cardiac_diagnostics', 'Cardiac Diagnostics'), ('general_practice', 'General Practice')], max_length=100, null=True)),
                ('insurance_accepted', models.TextField(blank=True, null=True)),
                ('payment_methods', models.CharField(choices=[('Credit Card', 'Credit Card'), ('Debit Card', 'Debit Card'), ('Cash', 'Cash')], max_length=50)),
                ('emergency_services', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
                ('home_sample_collection', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
                ('report_delivery_options', models.CharField(choices=[('Online', 'Online'), ('Email', 'Email'), ('Physical Copy', 'Physical Copy')], max_length=20)),
                ('accreditations_certifications', models.TextField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('lab_commission', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('promote', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0, verbose_name='Promote')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lab_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'laboratories',
            },
        ),
        migrations.CreateModel(
            name='HospitalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='hospital/hospital_images/')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='accounts.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dr_name', models.CharField(max_length=255)),
                ('dr_unique_code', models.CharField(max_length=50, unique=True)),
                ('qualification', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('experience', models.PositiveIntegerField(default=1)),
                ('profile_status', models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('R', 'Rejected')], default='P', max_length=1)),
                ('consultation_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('profile_img', models.ImageField(blank=True, null=True, upload_to='doctors/doctor_profiles/')),
                ('status', models.CharField(choices=[(1, 'Active'), (0, 'Inactive')], default=1, max_length=1)),
                ('sub_specialist', models.CharField(blank=True, max_length=100, null=True)),
                ('additional_qualification', models.TextField(blank=True, null=True)),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
                ('overall_ratings', models.FloatField(default=0)),
                ('document_update_status', models.IntegerField(default=0)),
                ('document_approve_status', models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('R', 'Rejected')], default='P', max_length=1)),
                ('online_status', models.CharField(choices=[('O', 'Online'), ('F', 'Offline')], default='F', max_length=1)),
                ('medical_license', models.CharField(max_length=100, unique=True)),
                ('institution', models.CharField(max_length=255)),
                ('graduation_year', models.PositiveIntegerField()),
                ('dob', models.DateField()),
                ('wallet', models.FloatField(default=0)),
                ('earnings', models.FloatField(default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_recommended', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('resume', models.ImageField(blank=True, null=True, upload_to='doctors/doctor_documents/')),
                ('medical_license_doc', models.ImageField(blank=True, null=True, upload_to='doctors/doctor_documents/')),
                ('certification', models.ImageField(blank=True, null=True, upload_to='doctors/doctor_documents/')),
                ('other', models.ImageField(blank=True, null=True, upload_to='doctors/doctor_documents/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctors', to='accounts.hospital')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'doctors',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('customer_name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('profile_picture', models.ImageField(blank=True, default='hospital/customer_profile/avatar.png', null=True, upload_to='customers/profiles/')),
                ('pre_existing_disease', models.TextField(blank=True, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True)),
                ('wallet', models.FloatField(default=0)),
                ('overall_ratings', models.FloatField(default=0)),
                ('no_of_ratings', models.IntegerField(default=0)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=1)),
                ('dob', models.DateField(blank=True, null=True)),
                ('age', models.FloatField(blank=True, null=True)),
                ('height', models.CharField(blank=True, max_length=20, null=True)),
                ('weight', models.CharField(blank=True, max_length=20, null=True)),
                ('emergency_contact_no', models.CharField(blank=True, max_length=255, null=True)),
                ('allergies', models.CharField(blank=True, max_length=255, null=True)),
                ('current_medications', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='admin/profiles/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'admin',
            },
        ),
    ]
