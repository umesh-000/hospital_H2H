from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password
from django.core.files.storage import default_storage
from django.conf import settings
from doctor import models
import datetime
import random
import os


# Doctors
def doctors_list(request):
    doctors = models.DoctorDetails.objects.all()
    return render(request, "doctors_list.html", {'doctors': doctors})

def generate_unique_code():
    prefix = 'Dr'
    unique_number = f"{random.randint(1, 99999):05d}"
    return f"{prefix}{unique_number}"
def doctor_create(request):
    if request.method == "GET":
        specialist_categories = models.DoctorSpecialistCategory.objects.all()
        return render(request, "doctor_create.html", {'specialist_categories': specialist_categories})

    if request.method == 'POST':
        # Doctor details
        dr_name = request.POST.get('dr_name')
        dr_username = request.POST.get('dr_username')
        password = request.POST.get('password')
        hashed_password = make_password(password)
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        dr_unique_code = generate_unique_code()
        description = request.POST.get('description')
        consultation_fee = request.POST.get('consultation_fee')
        recommendation = request.POST.get('recommendation')
        status = request.POST.get('status')

        # Doctor Qualifications details
        qualification = request.POST.get('qualification')
        experience = request.POST.get('experience')
        specialist_id = request.POST.get('specialist')
        medical_license = request.POST.get('medical_license')
        institution = request.POST.get('institution')
        graduation_year = request.POST.get('graduation_year')
        additional_qualification = request.POST.get('additional_qualification')

        # File handling
        profile_img = request.FILES.get('profile_img')
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
            dr_unique_code=dr_unique_code,
            profile_img=profile_img,
            description=description,
            consultation_fee=consultation_fee,
            join_date=datetime.datetime.now(),
            status=status,
            is_recommended=recommendation,
            qualification=qualification,
            experience=experience,
            specialist=specialist_instance, 
            medical_license=medical_license,
            institution=institution,
            graduation_year=graduation_year,
            additional_qualification=additional_qualification,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
        )
        doctor.save()
        return redirect('/admin/doctors/')

def doctor_edit(request, id):
    doctor = get_object_or_404(models.DoctorDetails, id=id)
    specialist_categories = models.DoctorSpecialistCategory.objects.all()

    if request.method == 'GET':
        context = {
            'doctor': doctor,
            'specialist_categories': specialist_categories,
        }
        return render(request, "doctor_edit.html", context)

    if request.method == 'POST':
        # Extract form data
        dr_name = request.POST.get('dr_name')
        dr_username = request.POST.get('dr_username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        description = request.POST.get('description')
        consultation_fee = request.POST.get('consultation_fee')
        recommendation = request.POST.get('recommendation')
        status = request.POST.get('status')
        profile_img = request.FILES.get('profile_img')

        specialist_id = request.POST.get('specialist')
         # Update qualifications if provided
        qualification = request.POST.get('qualification')
        experience = request.POST.get('experience')
        medical_license = request.POST.get('medical_license')
        institution = request.POST.get('institution')
        graduation_year = request.POST.get('graduation_year')
        additional_qualification = request.POST.get('additional_qualification')


        # Handle profile image
        if not profile_img:
            if doctor.profile_img:
                profile_img = doctor.profile_img
            else:
                default_image_path = os.path.join(settings.STATIC_ROOT, 'images', 'default_profile.png')
                with open(default_image_path, 'rb') as f:
                    profile_img = default_storage.save('doctor_images/default_profile.png', f)

        # Update doctor details
        doctor.dr_name = dr_name
        doctor.dr_username = dr_username
        doctor.password = password
        doctor.phone = phone
        doctor.email = email
        doctor.gender = gender
        doctor.dob = dob
        doctor.description = description
        doctor.consultation_fee = consultation_fee
        doctor.is_recommended = recommendation
        doctor.status = status
        doctor.profile_img = profile_img

        doctor.qualification=qualification
        doctor.experience=experience
        doctor.medical_license=medical_license
        doctor.institution=institution
        doctor.graduation_year=graduation_year
        doctor.additional_qualification=additional_qualification
        doctor.updated_at = datetime.datetime.now()
        doctor.save()


        return redirect('/admin/doctors/')

# Symptoms
def symptoms_list(request):
    symptoms = models.Symptom.objects.all()
    return render(request, "symptom_list.html", {'symptoms': symptoms})

def symptom_create(request):
    if request.method == "GET":
        specialists = models.DoctorSpecialistCategory.objects.all()
        return render(request, "symptom_create.html", {'specialists': specialists})

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
        return redirect('/admin/symptoms/')

def symptom_edit(request, id):
    symptom = get_object_or_404(models.Symptom, id=id)
    specialists = models.DoctorSpecialistCategory.objects.all()

    if request.method == 'GET':
        context = {
            'symptom': symptom,
            'specialists': specialists,
        }
        return render(request, "symptom_edit.html", context)

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

        return redirect('/admin/symptoms/')

def symptom_delete(request, id):
    symptom = get_object_or_404(models.Symptom, id=id)
    symptom.delete()
    return redirect('/admin/symptoms/')


# Specialist
def specialist_list(request):
    specialist_categories = models.DoctorSpecialistCategory.objects.all()
    return render(request, "specialist_list.html", {'specialist_categories': specialist_categories})

def specialist_create(request):
    if request.method == "GET":
        return render(request, "specialist_create.html")

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
        return redirect('/admin/specialists/')

def specialist_edit(request, id):
    specialist_category = get_object_or_404(models.DoctorSpecialistCategory, id=id)

    if request.method == 'GET':
        context = {
            'specialist_category': specialist_category,
        }
        return render(request, "specialist_edit.html", context)

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

        return redirect('/admin/specialists/')

def specialist_delete(request, id):
    specialist_category = get_object_or_404(models.DoctorSpecialistCategory, id=id)
    specialist_category.delete()
    return redirect('/admin/specialists/')