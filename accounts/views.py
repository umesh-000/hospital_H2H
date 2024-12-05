from django.shortcuts import render, redirect,get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password
from django.core.files.storage import default_storage
from django.contrib.auth import authenticate, login
from H2H_admin import models as admin_models
from django.contrib import messages
from django.db import transaction
from django.conf import settings
from accounts import models
from H2H_admin import utils
import datetime
import os

# Create your views here.
def index(request):
    return redirect('login')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.user_type == 'admin':
                request.session['admin_id'] = user.id
                messages.success(request, "Login Successful!")
                return redirect('admin_dashboard')
            elif user.user_type == 'hospital':
                messages.success(request, "Login Successful!")
                return redirect('hospital_dashboard')
            elif user.user_type == 'lab':
                messages.success(request, "Login Successful!")
                return redirect('lab_dashboard')
            elif user.user_type == 'doctor':
                messages.success(request, "Login Successful!")
                return redirect('doctors_dashboard')
            else:
                messages.error(request, "Unknown user type.")
                return redirect('login')
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('login')
    return render(request, 'accounts/login.html')


def admin_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if models.User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('admin_register')
        if models.User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('admin_register')
        user = models.User.objects.create( username=username, email=email, password=make_password(password),user_type="admin")
        models.Admin.objects.create(user=user)
        messages.success(request, "Admin registration successful!")
        return redirect('login')
    return render(request, 'accounts/admin_register.html')

def hospital_register(request):
    if request.method == "GET":
        return render(request, "accounts/hospital_register.html")

    if request.method == "POST":
        # User details
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if username or email already exists
        if models.User.objects.filter(username=user_name).exists():
            messages.error(request, "Username already exists!")
            return redirect('hospital_create')
        if models.User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('hospital_create')

        # Create User
        user = models.User.objects.create(
            username=user_name,
            email=email,
            password=make_password(password),
            user_type='hospital'
        )

        # Hospital details
        hospital_name = request.POST.get('hospital_name')
        phone_number = request.POST.get('phone_number')
        city = request.POST.get('city')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        open_time = request.POST.get('open_time')
        close_time = request.POST.get('close_time')
        website_url = request.POST.get('website_url')
        type_ = request.POST.get('type')
        status = request.POST.get('status')
        is_recommended = request.POST.get('isRecommended')
        address = request.POST.get('address')
        description = request.POST.get('description')
        # Create Hospital instance
        hospital = models.Hospital.objects.create(
            user=user,
            hospital_name=hospital_name,
            phone_number=phone_number,
            latitude=latitude,
            longitude=longitude,
            open_time=open_time,
            close_time=close_time,
            website_url=website_url,
            type=type_,
            status=status,
            is_recommended=is_recommended,
            address=address,
            description=description,
            city=city
        )
        messages.success(request, "Hospital Registration successfully!")
        return redirect('login')

    return render(request, "accounts/hospital_register.html")
    
def doctor_register(request):
    if request.method == "GET":
        specialist_category = admin_models.SpecialistCategory.objects.all()
        clinics_type = admin_models.ClinicCategory.objects.all()
        context = {'specialist_category': specialist_category, 'clinics_type': clinics_type}
        return render(request, "accounts/doctor_register.html", context)

    if request.method == "POST":
        try:
            with transaction.atomic():
                # Collect Basic Information
                dr_name = request.POST.get('dr_name')
                dr_username = request.POST.get('dr_username')
                password = request.POST.get('dr_password')
                hashed_password = make_password(password)
                phone = request.POST.get('dr_phone')
                email = request.POST.get('dr_email')
                gender = request.POST.get('dr_gender')
                dob = request.POST.get('dr_dob')
                consultation_fee = request.POST.get('dr_consultation_fees')

                # Collect Professional Information
                medical_license = request.POST.get('dr_val_med_license_no')
                specialist_id = request.POST.get('dr_specialization')
                experience = int(request.POST.get('dr_experience', 0))

                # Educational Background
                dr_degrees = request.POST.get('dr_degrees')
                dr_institutions = request.POST.get('dr_institutions')
                dr_graduation_years = request.POST.get('dr_graduation_years')
                dr_certification_fellowship = request.POST.get('dr_certification_fellowship')

                # Work Information
                dr_clinic_type = request.POST.get('dr_clinic_type')
                clinic_type = get_object_or_404(admin_models.ClinicCategory, id=dr_clinic_type)
                dr_current_work_address = request.POST.get('dr_current_work_address')
                dr_clinic_name = request.POST.get('dr_clinic_name')
                dr_work_number = request.POST.get('dr_work_number')
                dr_work_email_address = request.POST.get('dr_work_email_address')
                open_time = request.POST.get('open_time')
                close_time = request.POST.get('close_time')
                dr_short_biography = request.POST.get('dr_short_biography')

                # Handle Document Uploads
                profile_picture = request.FILES.get('profile_picture')
                resume = request.FILES.get('resume')
                medical_license_document = request.FILES.get('medical_license_document')
                certification_documents = request.FILES.get('certification_documents')
                other_relevant_documents = request.FILES.get('other_relevant_rocuments')

                if not profile_picture:
                    default_image_path = os.path.join(settings.STATIC_ROOT, 'images', 'default_image.png')
                    with open(default_image_path, 'rb') as f:
                        profile_picture = default_storage.save('doctors/default_image.png', f)

                print(profile_picture)
                print(resume)
                print(medical_license_document)
                print(certification_documents)
                print(other_relevant_documents)
                # Fetch Specialist Category instance
                specialist_instance = get_object_or_404(admin_models.SpecialistCategory, id=specialist_id)

                # Create User instance for Doctor
                user = models.User.objects.create(username=dr_username,password=hashed_password,email=email,user_type='doctor')

                # Create DoctorDetails instance
                doctor = models.DoctorDetails.objects.create(
                    # Basic Information
                    user=user,
                    dr_name=dr_name,phone=phone,gender=gender,
                    dob=dob,consultation_fee=consultation_fee,
                    description=dr_short_biography,
                    dr_unique_code=utils.generate_unique_code(),

                    # Professional Information
                    medical_license=medical_license,experience=experience,specialist=specialist_instance,

                    # Educational Background
                    qualification=dr_degrees,institution=dr_institutions,
                    additional_qualification=dr_certification_fellowship,
                    graduation_year=dr_graduation_years,

                    # Document Uploads
                    profile_img=profile_picture,
                    resume=resume,medical_license_doc=medical_license_document,certification=certification_documents,other=other_relevant_documents,
                )

                # Create DoctorClinics instance
                admin_models.DoctorClinics.objects.create(doctor=doctor,
                    clinic_category=clinic_type,address=dr_current_work_address,clinic_name=dr_clinic_name,
                    phone=dr_work_number,email=dr_work_email_address,start_time=open_time,end_time=close_time,)

                messages.success(request, 'Doctor Registration successfully!')
                return redirect('doctor_register')

        except Exception as e:
            # Handle errors and provide feedback
            messages.error(request, f"Error creating doctor: {str(e)}")
            return redirect('doctor_register')

def lab_register(request):
    if request.method == "POST":
        try:
            print("POST")
            with transaction.atomic():
                user = models.User.objects.create( username=request.POST.get('username'), email=request.POST.get('email'), user_type='lab', password=make_password(request.POST.get('password')))
                lab_image = request.FILES.get('lab_image')
                lab_image_url = None
                if lab_image:
                    fs = FileSystemStorage()
                    lab_image_url = fs.save(lab_image.name, lab_image)

                models.Laboratory.objects.create(user=user,
                    lab_name=request.POST.get('lab_name'), address=request.POST.get('address'), city=request.POST.get('city'),
                    state_province=request.POST.get('state_province'), postal_code=request.POST.get('postal_code'),
                    contact_number=request.POST.get('contact_number'), alternate_number=request.POST.get('alternate_number'),
                    website=request.POST.get('website'), operating_hours=request.POST.get('operating_hours'),
                    specializations=request.POST.get('specializations'), lab_commission=request.POST.get('lab_commission'),
                    description=request.POST.get('description'), insurance_accepted=request.POST.get('insurance_accepted'),
                    payment_methods=request.POST.get('payment_methods'), emergency_services=request.POST.get('emergency_services'),
                    home_sample_collection=request.POST.get('home_sample_collection'), report_delivery_options=request.POST.get('report_delivery_options'),
                    promote=request.POST.get('promote'), status=request.POST.get('status'),lab_image=lab_image_url,
                )
                messages.success(request, 'Laboratory Registration successfully!')
                return redirect('login')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('lab_register')
    return render(request, "accounts/lab_register.html")