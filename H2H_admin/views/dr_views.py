from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.contrib.auth.hashers import make_password
from django.views.decorators.http import require_POST
from accounts import models as account_module
from django.core.paginator import Paginator
from H2H_admin import models as adminModel
from django.http import JsonResponse
from django.contrib import messages
from django.db import transaction
from django.conf import settings
from H2H_admin import utils
from datetime import time
import traceback
import logging
import json
import os

logger = logging.getLogger(__name__)

# Doctors
@login_required
def doctors_list(request):
    doctors = account_module.DoctorDetails.objects.all()
    paginator = Paginator(doctors, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "admin/doctor/doctors_list.html", {'doctors': page_obj})

@login_required
def doctor_create(request):
    if request.method == "GET":
        specialist_categories = adminModel.SpecialistCategory.objects.all()
        context = {'specialist_categories': specialist_categories}
        return render(request, "admin/doctor/doctor_create.html", context)

    if request.method == "POST":
        try:
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
            profile_img = request.FILES.get('profile_picture')
            resume = request.FILES.get('resume')
            medical_license_document = request.FILES.get('medical_license_document')
            certification_documents = request.FILES.get('certification_documents')
            other_relevant_documents = request.FILES.get('other_relevant_documents')

            # Fallback to default image if not provided
            if not profile_img:
                default_image_path = os.path.join(settings.STATIC_ROOT, 'images', 'default_image.png')
                with open(default_image_path, 'rb') as f:
                    profile_img = default_storage.save('profile_images/default_image.png', f)

            specialist = get_object_or_404(adminModel.SpecialistCategory, id=specialist_id)

            # Create the User object
            user = account_module.User.objects.create(
                username=dr_username,
                password=hashed_password,
                email=email,
                first_name=dr_name,
                user_type='doctor'
            )

            # Create DoctorDetails instance
            doctor = account_module.DoctorDetails(
                user=user,
                dr_name=dr_name,
                dr_unique_code=utils.generate_unique_code(),
                phone=phone,
                gender=gender,
                dob=dob,
                consultation_fee=consultation_fee,
                description=description,
                status=status,
                is_recommended=is_recommended,
                
                qualification=dr_degrees,
                institution=dr_institutions,
                additional_qualification=dr_certification_fellowship,
                graduation_year=dr_graduation_years,

                experience=experience,
                specialist=specialist,
                medical_license=medical_license,
                profile_img=profile_img,
                resume=resume,
                medical_license_doc=medical_license_document,
                certification=certification_documents,
                other=other_relevant_documents,
                join_date=join_date
            )
            doctor.save()
            messages.success(request, "Doctor created successfully!")
            return redirect("doctors_list")

        except Exception as e:
            traceback.print_exc()
            messages.error(request, f"Error creating doctor: {e}")
            return redirect("doctor_create")

    messages.error(request, "Invalid request method.")
    return redirect("doctor_create")

@login_required
def doctor_edit(request, id):
    doctor = get_object_or_404(account_module.DoctorDetails, id=id)
    specialist_categories = adminModel.SpecialistCategory.objects.all()
    if request.method == 'GET':
        context = {
            'doctor': doctor,
            'specialist_categories': specialist_categories,
        }
        return render(request, "admin/doctor/doctor_edit.html", context)

    if request.method == 'POST':
        try:
            # Extract and validate form data
            dr_name = request.POST.get('dr_name')
            dr_username = request.POST.get('dr_username')
            dr_password = request.POST.get('dr_password')
            phone = request.POST.get('dr_phone')
            email = request.POST.get('dr_email')
            gender = request.POST.get('dr_gender')
            dob = request.POST.get('dr_dob')
            consultation_fee = request.POST.get('dr_consultation_fees')
            description = request.POST.get('description')
            status = request.POST.get('status')
            is_recommended = request.POST.get('is_recommended')
            medical_license = request.POST.get('dr_val_med_license_no')
            specialist_id = request.POST.get('dr_specialization')
            experience = request.POST.get('dr_experience')
            join_date = request.POST.get('join_date')
            dr_degrees = request.POST.get('dr_degrees')
            dr_institutions = request.POST.get('dr_institutions')
            dr_graduation_years = request.POST.get('dr_graduation_years')
            dr_certification_fellowship = request.POST.get('dr_certification_fellowship')

            # Get uploaded files
            profile_img = request.FILES.get('profile_picture')
            resume = request.FILES.get('resume')
            medical_license_document = request.FILES.get('medical_license_document')
            certification_documents = request.FILES.get('certification_documents')
            other_relevant_documents = request.FILES.get('other_relevant_documents')

            # Fetch specialist instance
            specialist_instance = get_object_or_404(adminModel.SpecialistCategory, id=specialist_id) if specialist_id else None

            # Transaction block
            with transaction.atomic():
                doctor.dr_name = dr_name
                doctor.user.first_name = dr_name
                doctor.user.username = dr_username
                doctor.user.email = email
                doctor.phone = phone
                if dr_password:
                    doctor.user.password = make_password(dr_password)
                doctor.gender = gender
                doctor.dob = dob
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

                # Update document fields if new files are uploaded
                doctor.profile_img = profile_img or doctor.profile_img
                doctor.resume = resume or doctor.resume
                doctor.medical_license_doc = medical_license_document or doctor.medical_license_doc
                doctor.certification = certification_documents or doctor.certification
                doctor.other = other_relevant_documents or doctor.other

                # Save the doctor instance
                doctor.save()
                doctor.user.save()

            messages.success(request, 'Doctor updated successfully!')
            return redirect('doctors_list')

        except Exception as e:
            logger.error(f"Error updating doctor (ID: {id}): {e}")
            messages.error(request, 'An error occurred while updating the doctor details.')
            return redirect('doctor_edit', id=id)

@login_required
def doctor_delete(request, id):
    if request.method == 'POST':
        try:
            doctor = get_object_or_404(account_module.DoctorDetails, id=id)
            if doctor.user.user_type != 'doctor':
                return JsonResponse({'success': False, 'message': 'Invalid user type for deletion.'})
            doctor.delete()
            doctor.user.delete()
            messages.success(request, 'Doctor deleted successfully!')
            return JsonResponse({'success': True, 'message': 'Doctor deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Error occurred: {str(e)}'})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


# Hospital Doctors Clinic Categ
@login_required
def doctor_clinic_categories(request):
    categories = adminModel.ClinicCategory.objects.all()
    paginator = Paginator(categories, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'categories':page_obj,
    }
    return render(request, 'admin/doctor/clinic_category_list.html', context)

@login_required
def clinic_category_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        status = request.POST.get('status')
        # Create a new ClinicCategory object and save it
        print(name)
        print(status)
        adminModel.ClinicCategory.objects.create(name=name, status=status)
        messages.success(request, 'Created successfully!')
        return redirect('doctor_clinic_categories')
    return render(request, 'admin/doctor/clinic_category_create.html')

@login_required
def clinic_category_edit(request, id):
    clinic_category = get_object_or_404(adminModel.ClinicCategory, id=id)
    
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
        'categories' : adminModel.ClinicCategory.objects.all()
    }
    return render(request, 'admin/doctor/clinic_category_edit.html', context)

@login_required
def clinic_category_delete(request, id):
    if request.method == 'POST':
        try:
            ClinicCategory = get_object_or_404(adminModel.ClinicCategory, id=id)
            ClinicCategory.delete()
            messages.success(request, 'Deleted Successfully!')
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


# Doctor Clinics :
@login_required
def doctor_clinics(request):
    clinics = adminModel.DoctorClinics.objects.all()
    paginator = Paginator(clinics, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'clinic_list': page_obj
    }
    return render(request, 'admin/doctor/doctor_clinics_list.html', context)

@login_required
def doctor_clinics_create(request):
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

        doctor = account_module.DoctorDetails.objects.get(id=doctor_id)
        clinic_category = adminModel.ClinicCategory.objects.get(id=clinic_category_id) if clinic_category_id else None

        adminModel.DoctorClinics.objects.create( doctor=doctor, clinic_category=clinic_category, clinic_name=clinic_name, phone=phone,
            email=email, address=address, consultation_minutes=consultation_minutes, status=status, start_time=start_time,
            end_time=end_time, latitude=latitude, longitude=longitude
        )

        messages.success(request, 'Created Successfully!')
        return redirect('doctor_clinic_list')

    # On GET request, render the form
    doctors = account_module.DoctorDetails.objects.all()
    clinic_categories = adminModel.ClinicCategory.objects.all()
    context={
        'doctors': doctors,
        'clinic_categories': clinic_categories
    }
    return render(request, 'admin/doctor/doctor_clinic_create.html', context)

@login_required
def doctor_clinics_edit(request, id):
    clinic = adminModel.DoctorClinics.objects.get(id=id)

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

        doctor = account_module.DoctorDetails.objects.get(id=doctor_id)
        clinic_category = adminModel.ClinicCategory.objects.get(id=clinic_category_id) if clinic_category_id else None

        clinic.doctor = doctor; clinic.clinic_category = clinic_category; clinic.clinic_name = clinic_name
        clinic.phone = phone; clinic.email = email; clinic.address = address; clinic.consultation_minutes = consultation_minutes
        clinic.status = status; clinic.start_time = start_time; clinic.end_time = end_time; clinic.latitude = latitude
        clinic.longitude = longitude

        # Save the updated clinic object
        clinic.save()

        messages.success(request, 'Updated Successfully!')
        return redirect('doctor_clinic_list')

    # On GET request, render the form with existing clinic data
    doctors = account_module.DoctorDetails.objects.all()
    clinic_categories = adminModel.ClinicCategory.objects.all()
    context = {
        'clinic': clinic,
        'doctors': doctors,
        'clinic_categories': clinic_categories
    }
    return render(request, 'admin/doctor/doctor_clinic_edit.html', context)

@login_required
def doctor_clinics_delete(request, id):
    if request.method == 'POST':
        try:
            DoctorClinics = get_object_or_404(adminModel.DoctorClinics, id=id)
            DoctorClinics.delete()
            messages.success(request, 'Deleted Successfully!')
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})



# Doctor Documents :
@login_required
def doctor_documents(request):
    doctor_doc_list = account_module.DoctorDetails.objects.all()
    paginator = Paginator(doctor_doc_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'doctor_doc_list': page_obj,
    }
    return render(request, "admin/doctor/doctor_doc_list.html", context)

@login_required
def change_doc_status(request):
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor_id')
        status = request.POST.get('status')

        try:
            doctor = account_module.DoctorDetails.objects.get(id=doctor_id)
            doctor.document_approve_status = status
            doctor.save()
            return JsonResponse({'success': True})
        except account_module.DoctorDetails.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Doctor not found'})
    
    return JsonResponse({'success': False, 'error': 'Invalid request'})


# Doctor Banner
@login_required
def dr_banner_list(request):
    dr_banner_list = adminModel.DoctorBanner.objects.all()
    paginator = Paginator(dr_banner_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'dr_banner_list': page_obj,
    }
    return render(request, "admin/doctor/dr_banner_list.html", context)

@login_required
def doctor_banner_create(request):
    if request.method == "GET":
        doctors_list = account_module.DoctorDetails.objects.all()
        return render(request, "admin/doctor/dr_banner_create.html", {'doctors_list': doctors_list})

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
            doctor = account_module.DoctorDetails.objects.get(id=doctor_id)
        except account_module.DoctorDetails.DoesNotExist:
            messages.error(request, "Selected doctor does not exist.")
            return redirect('doctor_banner_create')

        doctor_banner = adminModel.DoctorBanner(doctor=doctor,banner=banner_image,link=banner_link,position=position,status=status,)
        doctor_banner.save()
        messages.success(request, "Created successfully!")
        return redirect('dr_banner_list') 
    
@login_required
def doctor_banner_edit(request, id):
    banner = get_object_or_404(adminModel.DoctorBanner, id=id)

    if request.method == 'GET':
        doctors_list = account_module.DoctorDetails.objects.all()
        context = {
            'banner': banner,
            'doctors_list': doctors_list,
        }
        return render(request, "admin/doctor/dr_banner_edit.html", context)

    if request.method == 'POST':
        doctor_id = request.POST.get('doctor')
        banner_image = request.FILES.get('banner')
        link = request.POST.get('link')
        position = request.POST.get('position')
        status = request.POST.get('status')

        # Find the selected doctor
        try:
            doctor = account_module.DoctorDetails.objects.get(id=doctor_id)
        except account_module.DoctorDetails.DoesNotExist:
            messages.error(request, "Selected doctor does not exist.")
            return redirect('doctor_banner_edit', id=id)

        # Update banner details
        banner.doctor = doctor
        if banner_image:
            banner.banner = banner_image
        banner.link = link
        banner.position = position
        banner.status = status
        banner.save()

        messages.success(request, 'Banner Updated successfully!')
        return redirect('dr_banner_list')

@login_required
def doctor_banner_delete(request, id):
    if request.method == 'POST':
        try:
            doctor_banner = get_object_or_404(adminModel.DoctorBanner, id=id)
            doctor_banner.delete()
            messages.success(request, 'Deleted Successfully!')
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

# Doctor Booking
@login_required
def dr_booking_list(request):
    dr_booking_list = adminModel.DoctorBooking.objects.all()
    paginator = Paginator(dr_booking_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'dr_booking_list': page_obj,
        'status_choices': adminModel.DoctorBooking.STATUS_CHOICES,
    }
    return render(request, "admin/doctor/dr_booking_list.html", context)


@login_required
def doctor_booking_show(request,id):
    dr_booking = get_object_or_404(adminModel.DoctorBooking, id=id)
    context = {'booking': dr_booking}
    return render(request, "admin/doctor/dr_booking_show.html", context)


@login_required
def doctor_booking_edit(request, id):
    dr_booking = get_object_or_404(adminModel.DoctorBooking, id=id)
    if request.method == 'POST':
        dr_booking.booking_number = request.POST.get('booking_number')
        dr_booking.booking_for = request.POST.get('booking_for')
        dr_booking.patient_name = request.POST.get('patient_name')
        dr_booking.contact_number = request.POST.get('contact_number')
        dr_booking.age = request.POST.get('age')
        dr_booking.blood_group = request.POST.get('blood_group')
        dr_booking.medical_history = request.POST.get('medical_history')
        dr_booking.booking_date = request.POST.get('booking_date')
        time_slot = request.POST.get('time_slot')

        dr_booking.status = request.POST.get('status')
        if time_slot:
            try:
                hours, minutes = map(int, time_slot.split(':'))
                dr_booking.time_slot = time(hour=hours, minute=minutes)
            except ValueError:
                messages.error(request, 'Invalid time format. Please enter a valid time in HH:MM format.')
                return redirect('doctor_booking_edit', id=id)
        else:
            dr_booking.time_slot = None
        dr_booking.save()
        messages.success(request, 'Booking updated successfully!')
        return redirect('doctor_booking_requests')
    context = {
            'booking': dr_booking,
            'status_choices': adminModel.DoctorBooking.STATUS_CHOICES,
        }
    return render(request, "admin/doctor/dr_booking_edit.html", context)


@require_POST
def update_doctor_booking_status(request):
    data = json.loads(request.body)
    booking_id = data.get('booking_id')
    new_status = data.get('status')
    print(booking_id)
    try:
        booking = adminModel.DoctorBooking.objects.get(id=booking_id)  
        booking.status = new_status
        booking.save()
        return JsonResponse({'success': True, 'message': 'Status updated successfully.'})
    except adminModel.DoctorBooking.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Booking not found.'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})