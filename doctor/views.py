from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import default_storage
from django.contrib.auth.hashers import make_password
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib import messages
from django.utils import timezone
from django.conf import settings
from doctor import models
import datetime
import random
import json
import os

# Doctor Auth
def doctors_dashboard(request):
    return render(request, "doctor/doctor_deshboard.html")


def doctor_register(request):
    if request.method=="GET":
        specialist_category = models.DoctorSpecialistCategory.objects.all()
        clinics_type = models.ClinicCategory.objects.all()
        context = {
            'specialist_category':specialist_category,
            'clinics_type':clinics_type
        }
        return render(request, "doctor/doctor_register.html",context)
    if request.method == "POST":
        # Basic Information
        dr_name = request.POST.get('dr_name')
        dr_username = request.POST.get('dr_username')
        password = request.POST.get('dr_password')
        hashed_password = make_password(password)
        phone = request.POST.get('dr_phone')
        email = request.POST.get('dr_email')
        gender = request.POST.get('dr_gender')
        dob = request.POST.get('dr_dob')
        consultation_fee = request.POST.get('dr_consultation_fees')
        
        # Professional Information
        medical_license = request.POST.get('dr_val_med_license_no')
        specialist_id = request.POST.get('dr_specialization')
        experience = request.POST.get('dr_experience')

        # Educational Background
        dr_degrees = request.POST.get('dr_degrees')
        dr_institutions = request.POST.get('dr_institutions')
        dr_graduation_years = request.POST.get('dr_graduation_years')
        dr_certification_fellowship = request.POST.get('dr_certification_fellowship')

        # Work Information
        dr_clinic_type = request.POST.get('dr_clinic_type')
        dr_current_work_address = request.POST.get('dr_current_work_address')
        dr_clinic_name = request.POST.get('dr_clinic_name')
        dr_work_number = request.POST.get('dr_work_number')
        dr_work_email_address = request.POST.get('dr_work_email_address')
        open_time = request.POST.get('open_time')
        close_time = request.POST.get('close_time')
        virtual_consultations = request.POST.get('virtual_consultations')
        dr_short_biography = request.POST.get('dr_short_biography')


        # Payment Information
        dr_beneficiary_name = request.POST.get('dr_beneficiary_name')
        dr_bank_name = request.POST.get('dr_bank_name')
        dr_bank_account_number = request.POST.get('dr_bank_account_number')
        dr_IFSC_code = request.POST.get('dr_IFSC_code')

        # Document Upload
        dr_certification_fellowship = request.POST.get('dr_work_email_address')
        dr_certification_fellowship = request.POST.get('open_time')
        dr_certification_fellowship = request.POST.get('close_time')
        dr_certification_fellowship = request.POST.get('virtual_consultations')
        dr_certification_fellowship = request.POST.get('dr_short_biography')



        # File handling (Profile Image)
        profile_img = request.FILES.get('profile_img')
        if not profile_img:
            # Load a default image if not provided
            default_image_path = os.path.join(settings.STATIC_ROOT, 'images', 'default_image.png')
            with open(default_image_path, 'rb') as f:
                profile_img = default_storage.save('profile_images/default_image.png', f)

        # Fetch the specialist category instance
        specialist_instance = get_object_or_404(models.DoctorSpecialistCategory, id=specialist_id)
        doctor=[dr_name,dr_username,password, hashed_password, phone, email, gender, dob, consultation_fee, specialist_id,
                medical_license, experience,dr_degrees, dr_institutions, dr_graduation_years, dr_certification_fellowship,
                dr_clinic_type, dr_current_work_address, dr_clinic_name, dr_work_number, dr_work_email_address, open_time, 
                close_time, virtual_consultations, dr_short_biography,dr_beneficiary_name, dr_bank_name , dr_bank_account_number,
                dr_IFSC_code,
                   ]
        
        print("DOCTOR : ",doctor)
        # Create the DoctorDetails instance
        doctor = models.DoctorDetails(
            dr_name=dr_name, dr_username=dr_username, password=hashed_password, phone=phone,
            email=email, gender=gender, dob=dob, consultation_fee=consultation_fee,
            profile_img=profile_img, experience=experience, medical_license=medical_license,
            specialist=specialist_instance, created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
        )
        
        # Save the doctor information
        # doctor.save()
        
        # Success message
        messages.success(request, 'Doctor Created Sccessfully!')
        return redirect('doctor_register')

def doctor_login(request):
    return render(request, "doctor/doctor_login.html")

# Doctors
def doctors_list(request):
    doctors = models.DoctorDetails.objects.all()
    return render(request, "doctor/doctors_list.html", {'doctors': doctors})

def generate_unique_code():
    prefix = 'Dr'
    unique_number = f"{random.randint(1, 99999):05d}"
    return f"{prefix}{unique_number}"

def doctor_create(request):
    if request.method == "GET":
        specialist_categories = models.DoctorSpecialistCategory.objects.all()
        context = {
            'specialist_categories': specialist_categories,
        }
        return render(request, "doctor/doctor_create.html", context)

    if request.method == 'POST':
        # Basic Information
        dr_name = request.POST.get('dr_name')
        dr_username = request.POST.get('dr_username')
        password = request.POST.get('dr_password')
        hashed_password = make_password(password)
        phone = request.POST.get('dr_phone')
        email = request.POST.get('dr_email')
        gender = request.POST.get('dr_gender')
        dob = request.POST.get('dr_dob')
        consultation_fee = request.POST.get('dr_consultation_fees')
        description = request.POST.get('description')
        status = request.POST.get('status')
        is_recommended = request.POST.get('is_recommended')

        # Professional Information
        medical_license = request.POST.get('dr_val_med_license_no')
        specialist_id = request.POST.get('dr_specialization')
        experience = request.POST.get('dr_experience')
        join_date = request.POST.get('join_date')

        # Educational Background
        dr_degrees = request.POST.get('dr_degrees')
        dr_institutions = request.POST.get('dr_institutions')
        dr_graduation_years = request.POST.get('dr_graduation_years')
        dr_certification_fellowship = request.POST.get('dr_certification_fellowship')

        # Document Uploads
        profile_img = request.FILES.get('profile_picture')  # updated field name
        resume = request.FILES.get('resume')  # new field
        medical_license_document = request.FILES.get('medical_license_document')  # new field
        certification_documents = request.FILES.get('certification_documents')  # new field
        other_relevant_documents = request.FILES.get('other_relevant_documents')  # new field

        # Fallback to default image if not provided
        if not profile_img:
            default_image_path = os.path.join(settings.STATIC_ROOT, 'images', 'default_image.png')
            with open(default_image_path, 'rb') as f:
                profile_img = default_storage.save('profile_images/default_image.png', f)

        specialist_instance = get_object_or_404(models.DoctorSpecialistCategory, id=specialist_id)

        # Create DoctorDetails instance
        doctor = models.DoctorDetails(
            dr_name=dr_name, 
            dr_username=dr_username, 
            password=hashed_password, 
            phone=phone,
            email=email, 
            gender=gender, 
            dob=dob, 
            dr_unique_code=generate_unique_code(), 
            profile_img=profile_img, 
            description=description, 
            consultation_fee=consultation_fee,
            join_date=join_date, 
            status=status,  
            is_recommended=is_recommended, 
            qualification=dr_degrees,
            experience=experience, 
            specialist=specialist_instance, 
            medical_license=medical_license,
            institution=dr_institutions, 
            graduation_year=dr_graduation_years,
            additional_qualification=dr_certification_fellowship,
            resume=resume,
            medical_license_doc = medical_license_document, 
            certification=certification_documents,  
            other=other_relevant_documents
        )
        try:
            doctor.save()
            messages.success(request, 'Created successfully!')
            return redirect('doctors_list')
        except Exception as e:
            messages.error(request, f'Error saving doctor: {e}')
            print(e)

def doctor_edit(request, id):
    doctor = get_object_or_404(models.DoctorDetails, id=id)
    specialist_categories = models.DoctorSpecialistCategory.objects.all()

    if request.method == 'GET':
        context = {
            'doctor': doctor,
            'specialist_categories': specialist_categories,
        }
        return render(request, "doctor/doctor_edit.html", context)

    if request.method == 'POST':
        # Basic Information
        dr_name = request.POST.get('dr_name')
        dr_username = request.POST.get('dr_username')
        
        phone = request.POST.get('dr_phone')
        email = request.POST.get('dr_email')
        gender = request.POST.get('dr_gender')
        dob = request.POST.get('dr_dob')
        consultation_fee = request.POST.get('dr_consultation_fees')
        description = request.POST.get('description')
        status = request.POST.get('status')
        is_recommended = request.POST.get('is_recommended')

        # Professional Information
        medical_license = request.POST.get('dr_val_med_license_no')
        specialist_id = request.POST.get('dr_specialization')
        experience = request.POST.get('dr_experience')
        join_date = request.POST.get('join_date')

        # Educational Background
        dr_degrees = request.POST.get('dr_degrees')
        dr_institutions = request.POST.get('dr_institutions')
        dr_graduation_years = request.POST.get('dr_graduation_years')
        dr_certification_fellowship = request.POST.get('dr_certification_fellowship')

        # Document Uploads
        profile_img = request.FILES.get('profile_picture')  # updated field name
        resume = request.FILES.get('resume')  # new field
        medical_license_document = request.FILES.get('medical_license_document')  # new field
        certification_documents = request.FILES.get('certification_documents')  # new field
        other_relevant_documents = request.FILES.get('other_relevant_documents')  # new field

        specialist_instance = get_object_or_404(models.DoctorSpecialistCategory, id=specialist_id)

       # Update the fields of the existing doctor instance
        doctor.dr_name = dr_name
        doctor.dr_username = dr_username
        doctor.phone = phone
        doctor.email = email
        doctor.gender = gender
        doctor.dob = dob
        doctor.profile_img = profile_img if profile_img else doctor.profile_img  # Update only if new image is uploaded
        doctor.description = description
        doctor.consultation_fee = consultation_fee
        doctor.join_date = join_date
        doctor.status = status
        doctor.is_recommended = is_recommended
        doctor.qualification = dr_degrees
        doctor.experience = experience
        doctor.specialist = specialist_instance
        doctor.medical_license = medical_license
        doctor.institution = dr_institutions
        doctor.graduation_year = dr_graduation_years
        doctor.additional_qualification = dr_certification_fellowship
        doctor.resume = resume if resume else doctor.resume  # Update only if new resume is uploaded
        doctor.medical_license_doc = medical_license_document if medical_license_document else doctor.medical_license_doc
        doctor.certification = certification_documents if certification_documents else doctor.certification
        doctor.other = other_relevant_documents if other_relevant_documents else doctor.other

        try:
            doctor.save()
            messages.success(request, 'Updated successfully!')
            return redirect('doctors_list')
        except Exception as e:
            messages.error(request, f'Error updating doctor: {e}')
            print(e)

def doctor_delete(request, id):
    if request.method == 'POST':
        try:
            DoctorDetails = get_object_or_404(models.DoctorDetails, id=id)
            DoctorDetails.delete()
            messages.success(request, 'Deleted Successfully!')
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})



def doctor_clinic_categories(request):
    categories = models.ClinicCategory.objects.all()
    context = {
        'categories':categories,
    }
    return render(request, 'doctor/clinic_category_list.html', context)

def clinic_category_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        status = request.POST.get('status')
        # Create a new ClinicCategory object and save it
        print(name)
        print(status)
        models.ClinicCategory.objects.create(name=name, status=status)
        messages.success(request, 'Created successfully!')
        return redirect('doctor_clinic_categories')
    return render(request, 'doctor/clinic_category_create.html')

def clinic_category_edit(request, id):
    clinic_category = get_object_or_404(models.ClinicCategory, id=id)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        status = request.POST.get('status')
        clinic_category.name = name
        clinic_category.status = int(status)
        clinic_category.save()
        messages.success(request, 'Updated successfully!')
        return redirect('doctor_clinic_categories')

    # If the request is GET, show the form with the prefilled data
    context = {
        'clinic_category': clinic_category,
        'categories' : models.ClinicCategory.objects.all()
    }
    return render(request, 'doctor/clinic_category_edit.html', context)

def clinic_category_delete(request, id):
    if request.method == 'POST':
        try:
            ClinicCategory = get_object_or_404(models.ClinicCategory, id=id)
            ClinicCategory.delete()
            messages.success(request, 'Deleted Successfully!')
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


def doctor_clinics(request):
    clinics = models.DoctorClinics.objects.all()
    context = {
        'clinic_list': clinics
    }
    return render(request, 'doctor/doctor_clinics_list.html', context)

def doctor_clinics_create(request):
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor')  # Assuming you're sending the doctor's ID
        clinic_category_id = request.POST.get('clinic_category')  # Assuming you're sending the clinic category ID
        clinic_name = request.POST.get('clinic_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        consultation_minutes = request.POST.get('consultation_minutes')
        status = request.POST.get('status')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        # Fetch doctor and clinic category from the database
        doctor = models.DoctorDetails.objects.get(id=doctor_id)
        clinic_category = models.ClinicCategory.objects.get(id=clinic_category_id) if clinic_category_id else None

        # Create a new DoctorClinics object and save it
        models.DoctorClinics.objects.create( doctor=doctor, clinic_category=clinic_category, clinic_name=clinic_name, phone=phone,
            email=email, address=address, consultation_minutes=consultation_minutes, status=status, start_time=start_time,
            end_time=end_time, latitude=latitude, longitude=longitude
        )

        messages.success(request, 'Created Successfully!')
        return redirect('doctor_clinic_list')

    # On GET request, render the form
    doctors = models.DoctorDetails.objects.all()
    clinic_categories = models.ClinicCategory.objects.all()
    context={
        'doctors': doctors,
        'clinic_categories': clinic_categories
    }
    return render(request, 'doctor/doctor_clinic_create.html', context)

def doctor_clinics_edit(request, id):
    clinic = models.DoctorClinics.objects.get(id=id)

    if request.method == 'POST':
        doctor_id = request.POST.get('doctor')
        clinic_category_id = request.POST.get('clinic_category')
        clinic_name = request.POST.get('clinic_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        consultation_minutes = request.POST.get('consultation_minutes')
        status = request.POST.get('status')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        doctor = models.DoctorDetails.objects.get(id=doctor_id)
        clinic_category = models.ClinicCategory.objects.get(id=clinic_category_id) if clinic_category_id else None

        clinic.doctor = doctor; clinic.clinic_category = clinic_category; clinic.clinic_name = clinic_name
        clinic.phone = phone; clinic.email = email; clinic.address = address; clinic.consultation_minutes = consultation_minutes
        clinic.status = status; clinic.start_time = start_time; clinic.end_time = end_time; clinic.latitude = latitude
        clinic.longitude = longitude

        # Save the updated clinic object
        clinic.save()

        messages.success(request, 'Updated Successfully!')
        return redirect('doctor_clinic_list')

    # On GET request, render the form with existing clinic data
    doctors = models.DoctorDetails.objects.all()
    clinic_categories = models.ClinicCategory.objects.all()
    context = {
        'clinic': clinic,
        'doctors': doctors,
        'clinic_categories': clinic_categories
    }
    return render(request, 'doctor/doctor_clinic_edit.html', context)

def doctor_clinics_delete(request, id):
    if request.method == 'POST':
        try:
            DoctorClinics = get_object_or_404(models.DoctorClinics, id=id)
            DoctorClinics.delete()
            messages.success(request, 'Deleted Successfully!')
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

# Symptoms
def symptoms_list(request):
    symptoms = models.Symptom.objects.all()
    return render(request, "doctor/symptom_list.html", {'symptoms': symptoms})

def symptom_create(request):
    if request.method == "GET":
        specialists = models.DoctorSpecialistCategory.objects.all()
        return render(request, "doctor/symptom_create.html", {'specialists': specialists})

    if request.method == 'POST':
        specialist_id = request.POST.get('specialist')
        symptom_name = request.POST.get('symptom_name')
        symptom_image = request.FILES.get('symptom_image')
        status = request.POST.get('status')

        if not symptom_image:
            default_image_path = os.path.join(settings.STATIC_ROOT, 'images', 'default_image.png')
            with open(default_image_path, 'rb') as f:
                symptom_image = default_storage.save('symptom_images/default_image.png', f)

        symptom = models.Symptom(
            specialist_id=specialist_id,
            symptom_name=symptom_name,
            symptom_image=symptom_image,
            status=status,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
        )
        symptom.save()
        messages.success(request, 'Created successfully!')
        return redirect('symptoms_list')

def symptom_edit(request, id):
    symptom = get_object_or_404(models.Symptom, id=id)
    specialists = models.DoctorSpecialistCategory.objects.all()

    if request.method == 'GET':
        context = {
            'symptom': symptom,
            'specialists': specialists,
        }
        return render(request, "doctor/symptom_edit.html", context)

    if request.method == 'POST':
        specialist_id = request.POST.get('specialist')
        symptom_name = request.POST.get('symptom_name')
        symptom_image = request.FILES.get('symptom_image')
        status = request.POST.get('status')

        if not symptom_image:
            if symptom.symptom_image:
                symptom_image = symptom.symptom_image
            else:
                default_image_path = os.path.join(settings.STATIC_ROOT, 'images', 'default_image.png')
                with open(default_image_path, 'rb') as f:
                    symptom_image = default_storage.save('symptom_images/default_image.png', f)

        symptom.specialist_id = specialist_id
        symptom.symptom_name = symptom_name
        symptom.symptom_image = symptom_image
        symptom.status = status
        symptom.updated_at = datetime.datetime.now()
        symptom.save()
        messages.success(request, 'Updated Successfully!')
        return redirect('symptoms_list')
    
def symptom_delete(request, id):
    if request.method == 'POST':
        try:
            symptom = get_object_or_404(models.Symptom, id=id)
            symptom.delete()
            messages.success(request, 'Deleted Successfully!')
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

# Specialist
def specialist_list(request):
    specialist_categories = models.DoctorSpecialistCategory.objects.all()
    return render(request, "doctor/specialist_list.html", {'specialist_categories': specialist_categories})

def specialist_create(request):
    if request.method == "GET":
        return render(request, "doctor/specialist_create.html")

    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        category_image = request.FILES.get('category_image')
        status = request.POST.get('status')
        if not category_image:
            default_image_path = os.path.join(settings.STATIC_ROOT, 'images', 'default_image.png')
            with open(default_image_path, 'rb') as f:
                category_image = default_storage.save('category_images/default_image.png', f)

        specialist_category = models.DoctorSpecialistCategory(
            category_name=category_name,
            category_image=category_image,
            status=status,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
        )
        specialist_category.save()
        messages.success(request, 'Created Successfully!')
        return redirect('specialist_list')

def specialist_edit(request, id):
    specialist_category = get_object_or_404(models.DoctorSpecialistCategory, id=id)

    if request.method == 'GET':
        context = {
            'specialist_category': specialist_category,
        }
        return render(request, "doctor/specialist_edit.html", context)

    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        category_image = request.FILES.get('category_image')
        status = request.POST.get('status')

        # Handling the default image fallback
        if not category_image:
            if specialist_category.category_image:
                category_image = specialist_category.category_image
            else:
                default_image_path = os.path.join(settings.STATIC_ROOT, 'images', 'default_image.png')
                with open(default_image_path, 'rb') as f:
                    category_image = default_storage.save('category_images/default_image.png', f)

        specialist_category.category_name = category_name
        specialist_category.category_image = category_image
        specialist_category.status = status
        specialist_category.updated_at = datetime.datetime.now()
        specialist_category.save()
        messages.success(request, 'Updated Successfully!')
        return redirect('specialist_list')


def specialist_delete(request, id):
    if request.method == 'POST':
        try:
            specialist_category = get_object_or_404(models.DoctorSpecialistCategory, id=id)
            specialist_category.delete()
            messages.success(request, 'Deleted Successfully!')
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


# Doctor Banner
def dr_banner_list(request):
    dr_banner_list = models.DoctorBanner.objects.all()
    context = {
        'dr_banner_list': dr_banner_list,
    }
    return render(request, "doctor/dr_banner_list.html", context)

def doctor_banner_create(request):
    if request.method == "GET":
        doctors_list = models.DoctorDetails.objects.all()
        return render(request, "doctor/dr_banner_create.html", {'doctors_list': doctors_list})

    if request.method == "POST":
        doctor_id = request.POST.get('doctor')
        banner_image = request.FILES.get('banner')
        banner_link = request.POST.get('link', '')
        position = request.POST.get('position', 'B')
        status = request.POST.get('status', 1) 

        if not banner_image:
            default_image_path = os.path.join(settings.STATIC_ROOT, 'images', 'default_image.png')
            with open(default_image_path, 'rb') as f:
                banner_image = default_storage.save('doctors/banners/default_image.png', f)

        try:
            doctor = models.DoctorDetails.objects.get(id=doctor_id)
        except models.DoctorDetails.DoesNotExist:
            messages.error(request, "Selected doctor does not exist.")
            return redirect('doctor_banner_create')

        doctor_banner = models.DoctorBanner(
            doctor=doctor,
            banner=banner_image,
            link=banner_link,
            position=position,
            status=status,
        )
        doctor_banner.save()
        messages.success(request, "Created successfully!")
        return redirect('dr_banner_list') 
    
def doctor_banner_edit(request, id):
    banner = get_object_or_404(models.DoctorBanner, id=id)

    if request.method == 'GET':
        doctors_list = models.DoctorDetails.objects.all()
        context = {
            'banner': banner,
            'doctors_list': doctors_list,
        }
        return render(request, "doctor/dr_banner_edit.html", context)

    if request.method == 'POST':
        doctor_id = request.POST.get('doctor')
        banner_image = request.FILES.get('banner')
        link = request.POST.get('link')
        position = request.POST.get('position')
        status = request.POST.get('status')

        # Find the selected doctor
        try:
            doctor = models.DoctorDetails.objects.get(id=doctor_id)
        except models.DoctorDetails.DoesNotExist:
            messages.error(request, "Selected doctor does not exist.")
            return redirect('doctor_banner_edit', id=id)

        # Update banner details
        banner.doctor = doctor
        if banner_image:
            banner.banner = banner_image
        banner.link = link
        banner.position = position
        banner.status = status
        banner.updated_at = datetime.datetime.now()
        banner.save()

        messages.success(request, 'Banner Updated successfully!')
        return redirect('dr_banner_list')

def doctor_banner_delete(request, id):
    if request.method == 'POST':
        try:
            doctor_banner = get_object_or_404(models.DoctorBanner, id=id)
            doctor_banner.delete()
            messages.success(request, 'Deleted Successfully!')
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


def doctor_documents(request):
    doctor_doc_list = models.DoctorDetails.objects.all()
    context = {
        'doctor_doc_list': doctor_doc_list,
    }
    return render(request, "doctor/doctor_doc_list.html", context)

def change_doc_status(request):
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor_id')
        status = request.POST.get('status')

        try:
            doctor = models.DoctorDetails.objects.get(id=doctor_id)
            doctor.document_approve_status = status
            doctor.save()
            return JsonResponse({'success': True})
        except models.DoctorDetails.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Doctor not found'})
    
    return JsonResponse({'success': False, 'error': 'Invalid request'})


# Doctor booking list view
def doctor_booking_requests(request):
    doctor_booking_list = models.DoctorBooking.objects.all()
    context = {
        "doctor_booking_list": doctor_booking_list,
    }
    return render(request, 'doctor/doctor_booking_requests_list.html', context)


@require_POST
def update_doctor_booking_status(request):
    data = json.loads(request.body)
    booking_id = data.get('booking_id')
    new_status = data.get('status')
    try:
        booking = models.DoctorBooking.objects.get(id=booking_id)
        booking.status = new_status
        booking.save()
        return JsonResponse({'success': True, 'message': 'Status updated successfully.'})
    except models.DoctorBooking.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Booking not found.'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})