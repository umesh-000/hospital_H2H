from django.contrib.auth.hashers import make_password,check_password
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage
from django.views.decorators.http import require_POST
from django.core.files.base import ContentFile
from H2H_admin import models as adminModel
import doctor.models as doctor_module
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from django.conf import settings
from hospital import models
import datetime
import json
import os

# Hospital
def hospital_list(request):
    hospital_list = models.Hospital.objects.all()
    return render(request,"admin/hospital_list.html",{"hospital_list":hospital_list})

def hospital_create(request):
    if request.method == "GET":
        return render(request, "admin/hospital_add.html")
    
    if request.method == 'POST':
        hospital_name = request.POST.get('hospital_name')
        user_name = request.POST.get('user_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
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

        # Handle file uploads
        hospital_image_files = request.FILES.getlist('hospital_images')
        hospital_logo = request.FILES.get('hospital_logo')

        # Create the Hospital instance
        hospital = models.Hospital(
            hospital_name=hospital_name,
            user_name=user_name,
            phone_number=phone_number,
            email=email,
            password=make_password(password),
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
            hospital_image=hospital_image_files[0] if hospital_image_files else None,  # Handling only the first image for hospital_image
            hospital_logo=hospital_logo,
            overall_ratings=0,
            no_of_ratings=0,
            wallet=0,
            city=city,
        )
        hospital.save()

        # Save additional images
        for image_file in hospital_image_files:
            models.HospitalImage.objects.create(hospital=hospital, image=image_file)
        
        messages.success(request, 'Created successfully!')
        return redirect('/admin/hospital/')
    
def hospital_edit(request, id):
    hospital = get_object_or_404(models.Hospital, id=id)
    
    if request.method == "GET":
        # Render the form with existing hospital details
        context = {
            'hospital': hospital,
            'hospital_images': hospital.images.all(),
        }
        return render(request, 'admin/hospital_edit.html', context)
    
    if request.method == "POST":
        hospital.hospital_name = request.POST.get('hospital_name')
        hospital.user_name = request.POST.get('user_name')
        hospital.phone_number = request.POST.get('phone_number')
        hospital.email = request.POST.get('email')
        hospital.city = request.POST.get('city')
        hospital.latitude = request.POST.get('latitude')
        hospital.longitude = request.POST.get('longitude')
        hospital.open_time = request.POST.get('open_time')
        hospital.close_time = request.POST.get('close_time')
        hospital.website_url = request.POST.get('website_url')
        hospital.type = request.POST.get('type')
        hospital.status = request.POST.get('status')
        hospital.is_recommended = request.POST.get('isRecommended')
        hospital.address = request.POST.get('address')
        hospital.description = request.POST.get('description')

        # Handle file uploads
        hospital_image_files = request.FILES.getlist('hospital_images')
        hospital_logo = request.FILES.get('hospital_logo')

        # Update the main hospital instance
        if hospital_logo:
            hospital.hospital_logo = hospital_logo
        hospital.save()

        # Save additional images
        for image_file in hospital_image_files:
            models.HospitalImage.objects.create(hospital=hospital, image=image_file)

        messages.success(request, 'Updated successfully!')
        return redirect('/admin/hospital/')

def hospital_delete(request, id):
    if request.method == 'POST':
        try:
            hospital = get_object_or_404(models.Hospital, id=id)
            hospital.delete()
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})



# Ward
def ward_list(request):
    if request.method == "GET":
        ward_list = models.Ward.objects.all()
        context ={
            "ward_list":ward_list,
        }
        return render(request,"admin/ward_list.html",context)

def ward_create(request):
    if request.method == "GET":
        hospitals = models.Hospital.objects.all()
        ward_list = models.Ward.objects.all()
        context ={
            "ward_list":ward_list,
            "hospitals":hospitals,
        }
        return render(request,"admin/add_ward.html",context)


    if request.method == 'POST':
        hospital_id = request.POST.get('hospital_id')
        ward_name = request.POST.get('ward_name')
        status = request.POST.get('status')

        hospital = models.Hospital.objects.get(id=hospital_id)

        # Create a new Ward instance
        ward = models.Ward(
            hospital=hospital,
            ward_name=ward_name,
            status=status,
            created_at= datetime.datetime.now(),
            updated_at = datetime.datetime.now(),
        )
        ward.save()
        messages.success(request, 'Ward Created successfully!')
        return redirect('ward_list')

def ward_edit(request,id):
    ward = get_object_or_404(models.Ward, id=id)
    hospitals = models.Hospital.objects.all()
    if request.method=="GET":
        return render(request, 'admin/edit_ward.html', {'ward': ward,"hospitals":hospitals})

    if request.method == 'POST':
        hospital_id = request.POST.get('hospital_id')
        ward_name = request.POST.get('ward_name')
        status = request.POST.get('status')
        ward.hospital_id = hospital_id if hospital_id else None
        ward.ward_name = ward_name
        ward.status = int(status)
        ward.save()
        messages.success(request, 'Ward Updated successfully!')
        return redirect('ward_list')
    
def ward_delete(request, id):
    if request.method == 'POST':
        try:
            ward = get_object_or_404(models.Ward, id=id)
            ward.delete()
            return JsonResponse({'success': True, 'message': 'Ward deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})



# Bed
def bed_list(request):
    if request.method == "GET":
        bed_list = models.Bed.objects.all()
        context ={
            "bed_list":bed_list,
        }
        return render(request,"admin/list_bed.html",context)
    
def bed_create(request):
    if request.method == "GET":
        hospitals = models.Hospital.objects.all()
        wards = models.Ward.objects.all()
        context = {
            "hospitals": hospitals,
            "wards": wards,
        }
        return render(request, "admin/add_bed.html", context)
    
    if request.method == "POST":
        hospital_id = request.POST.get('hospital_id')
        ward_id = request.POST.get('ward_id')
        bed_type = request.POST.get('bed_type')
        bed_count = request.POST.get('bed_count')
        sale_price = request.POST.get('sale_price')
        sale_bed_price = request.POST.get('sale_bed_price')
        status = request.POST.get('status')

        hospital = models.Hospital.objects.get(id=hospital_id)
        ward = models.Ward.objects.get(id=ward_id)

        # Creating a new Bed object
        bed = models.Bed(
            hospital=hospital,
            ward=ward,
            bed_type=bed_type,
            bed_count=bed_count,
            sale_price=sale_price,
            sale_bed_price=sale_bed_price,
            status=status
        )
        bed.save()
        messages.success(request, 'Bed added successfully!')
        return redirect('bed_list')
    
def bed_edit(request, id):
    bed = get_object_or_404(models.Bed, id=id)
    if request.method == "GET":
        hospitals = models.Hospital.objects.all()
        wards = models.Ward.objects.all()
        context = {
            'bed': bed,
            'hospitals': hospitals,
            'wards': wards,
        }
        return render(request, 'admin/edit_bed.html', context)
    
    if request.method == "POST":
        hospital_id = request.POST.get('hospital_id')
        ward_id = request.POST.get('ward_id')
        bed_type = request.POST.get('bed_type')
        bed_count = request.POST.get('bed_count')
        sale_price = request.POST.get('sale_price')
        sale_bed_price = request.POST.get('sale_bed_price')
        status = request.POST.get('status')

        # Update the bed object with the new data
        bed.hospital_id = hospital_id
        bed.ward_id = ward_id
        bed.bed_type = bed_type
        bed.bed_count = bed_count
        bed.sale_price = sale_price
        bed.sale_bed_price = sale_bed_price
        bed.status = status
        bed.updated_at = datetime.datetime.now()

        bed.save()
        messages.success(request, 'Bed updated successfully!')
        return redirect('bed_list')
    
def bed_delete(request, id):
    if request.method == 'POST':
        try:
            bed = get_object_or_404(models.Bed, id=id)
            bed.delete()
            return JsonResponse({'success': True, 'message': 'Bed deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})



# Bed Status
def bed_status_list(request):
    bed_statuses = models.BedStatus.objects.select_related('hospital', 'bed').all()
    context = {
        "bed_statuses": bed_statuses,
    }
    return render(request, 'admin/bed_status_list.html', context)

def bed_status_create(request):
    if request.method == "POST":
        hospital_id = request.POST.get('hospital_id')
        bed_id = request.POST.get('bed_id')
        status = request.POST.get('status')

        hospital = models.Hospital.objects.get(id=hospital_id)
        bed = models.Bed.objects.get(id=bed_id)

        # Creating a new Bed object
        bed_status = models.BedStatus(
            hospital=hospital,
            bed=bed,
            status=status
        )
        bed_status.save()
        messages.success(request, 'Bed Status Added Successfully!')
        
        return redirect('bed_status_list')

    if request.method == "GET":
        hospitals = models.Hospital.objects.all()
        beds = models.Bed.objects.all()

        context = {
            "hospitals": hospitals,
            "beds": beds,
        }
        return render(request, 'admin/create_bed_status.html', context)

def bed_status_edit(request, id):
    bed_status = get_object_or_404(models.BedStatus, id=id)  # Fetch the bed status by ID

    if request.method == "POST":
        # Get form data
        hospital_id = request.POST.get('hospital_id')
        bed_id = request.POST.get('bed_id')
        status = request.POST.get('status')

        # Fetch the hospital and bed objects based on the selected IDs
        hospital = models.Hospital.objects.get(id=hospital_id)
        bed = models.Bed.objects.get(id=bed_id)

        # Update the bed status object
        bed_status.hospital = hospital
        bed_status.bed = bed
        bed_status.status = status
        bed_status.save()  # Save the changes to the database

        # Display a success message and redirect to the bed status list
        messages.success(request, 'Bed Status Updated Successfully!')
        return redirect('bed_status_list')

    else:
        # On GET request, retrieve the list of hospitals and beds to populate the form
        hospitals = models.Hospital.objects.all()
        beds = models.Bed.objects.all()

        # Pass the data to the template for rendering the form
        context = {
            "hospitals": hospitals,
            "beds": beds,
            "bed_status": bed_status
        }
        return render(request, 'admin/bed_status_update.html', context)

def bed_status_delete(request, id):
    if request.method == 'POST':
        try:
            bed_status = get_object_or_404(models.BedStatus, id=id)
            bed_status.delete()
            return JsonResponse({'success': True, 'message': 'Bed Status deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})



# bed booking 
def bed_requests(request):
    bed_list = models.BedBooking.objects.all()
    context = {
        "bed_list": bed_list,
    }
    return render(request, 'admin/bed_booking_requests_list.html', context)

@require_POST
def update_booking_status(request):
    data = json.loads(request.body)
    booking_id = data.get('booking_id')
    new_status = data.get('status')
    try:
        booking = models.BedBooking.objects.get(id=booking_id)
        booking.status = new_status
        booking.save()
        return JsonResponse({'success': True, 'message': 'Status updated successfully.'})
    except models.BedBooking.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Booking not found.'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})


# # Fee Setting
# def hospital_fee_setting_list(request):
#     fee_settings = models.HospitalFeeSettings.objects.all()
#     context = {
#         'fee_settings': fee_settings,
#     }
#     return render(request, 'admin/hospital_fee_setting_list.html', context)

# def hospital_fee_setting_list_create(request):
#     if request.method == "GET":
#         hospitals = models.Hospital.objects.all()
#         fee_settings = models.HospitalFeeSettings.objects.all()
#         context = {
#             "hospitals": hospitals,
#             "fee_settings": fee_settings,
#         }
#         return render(request, "admin/hospital_fee_setting_create.html", context)
    
#     if request.method == "POST":
#         hospital_id = request.POST.get('hospital_id')
#         appointment_fee = request.POST.get('appointment_fee')
#         consultation_fee = request.POST.get('consultation_fee')
#         waiting_time = request.POST.get('waiting_time')
#         # Fetch the hospital object
#         hospital = models.Hospital.objects.get(id=hospital_id)
#         print(hospital_id)

#         # Create a new HospitalFeeSetting object
#         fee_setting = models.HospitalFeeSettings(
#             hospital=hospital,
#             appointment_fee=appointment_fee,
#             consultation_fee=consultation_fee,
#             waiting_time=waiting_time,
#             created_at= datetime.datetime.now(),
#             updated_at = datetime.datetime.now(),
#         )
#         print(fee_setting)
#         fee_setting.save()
#         messages.success(request, 'Hospital Fee Setting added successfully!')
#         return redirect('/admin/hospital/fee_settings/')


# Hospital services
def hospital_service_list(request):
    hospital_service = models.HospitalService.objects.all()
    context = {
        'hospital_service': hospital_service,
    }
    return render(request, 'admin/hospital_services_list.html', context)

def hospital_service_create(request):
    if request.method == "GET":
        hospitals = models.Hospital.objects.all()
        context ={
            "hospitals":hospitals,
        }
        return render(request,"admin/hospital_services_create.html",context)

    if request.method == 'POST':
        hospital_id = request.POST.get('hospital')
        service_name = request.POST.get('service_name')
        starting_from = request.POST.get('starting_from')
        service_icon = request.FILES.get('service_icon')

        
        # Handling the default image fallback
        if not service_icon:
            # If no image is uploaded, use a default image
            default_image_path = os.path.join(settings.STATIC_ROOT, 'images', 'default_image.png')
            with open(default_image_path, 'rb') as f:
                service_icon = default_storage.save('service_icons/default_image.png', f)

        
        hospital_service = models.HospitalService(
            hospital_id=hospital_id,
            service_name=service_name,
            starting_from=starting_from,
            service_icon=service_icon,
            created_at = datetime.datetime.now(),
            updated_at = datetime.datetime.now(),
        )
        hospital_service.save()
        messages.success(request, 'Service Added Successfully!')
        return redirect('hospital_service_list')

def hospital_service_edit(request, id):
    service = get_object_or_404(models.HospitalService, id=id)

    if request.method == 'GET':
        hospitals = models.Hospital.objects.all()
        context = {
            'service': service,
            'hospitals': hospitals,
        }
        return render(request, "admin/hospital_service_edit.html", context)

    if request.method == 'POST':
        hospital_id = request.POST.get('hospital')
        service_name = request.POST.get('service_name')
        starting_from = request.POST.get('starting_from')
        service_icon = request.FILES.get('service_icon')

        # Handling the default image fallback
        if not service_icon:
            if service.service_icon:
                service_icon = service.service_icon
            else:
                default_image_path = os.path.join(settings.STATIC_ROOT, 'images', 'default_image.png')
                with open(default_image_path, 'rb') as f:
                    service_icon = default_storage.save('service_icons/default_image.png', f)

        service.hospital_id = hospital_id
        service.service_name = service_name
        service.starting_from = starting_from
        service.service_icon = service_icon
        service.updated_at = datetime.datetime.now()
        service.save()
        messages.success(request, 'Service Updated Successfully!')
        return redirect('hospital_service_list')

def hospital_service_delete(request, id):
    if request.method == 'POST':
        try:
            service = get_object_or_404(models.HospitalService, id=id)
            service.delete()
            return JsonResponse({'success': True, 'message': 'Service Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


# Hospital Department
def hospital_department_list(request):
    hospital_department = models.HospitalDepartment.objects.all()
    context = {
        'hospital_departments': hospital_department,
    }
    return render(request, 'admin/hospital_departments_list.html',context)

def hospital_department_create(request):
    if request.method == "GET":
        hospitals = models.Hospital.objects.all()
        context = {
            "hospitals": hospitals,
        }
        return render(request, "admin/hospital_department_create.html", context)

    if request.method == 'POST':
        hospital_id = request.POST.get('hospital')
        department_name = request.POST.get('department_name')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        if not image:
            default_image_path = os.path.join(settings.STATIC_ROOT, 'images', 'default_image.png')
            with open(default_image_path, 'rb') as f:
                image = default_storage.save('department_images/default_image.png', f)

        hospital_department = models.HospitalDepartment(
            hospital_id=hospital_id,
            department_name=department_name,
            description=description,
            image=image,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
        )
        hospital_department.save()
        messages.success(request, 'Department Added Successfully!')
        return redirect('hospital_department_list')

def hospital_department_edit(request, id):
    department = get_object_or_404(models.HospitalDepartment, id=id)
    hospitals = models.Hospital.objects.all()
    if request.method == "GET":
        context = {
            "hospitals": hospitals,
            "department": department,
        }
        return render(request, "admin/hospital_department_edit.html", context)

    if request.method == 'POST':
        hospital_id = request.POST.get('hospital')
        department_name = request.POST.get('department_name')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        # Handling the default image fallback
        if not image:
            # If no new image is uploaded, keep the existing one
            image = department.image

        department.hospital_id=hospital_id
        department.department_name = department_name
        department.description = description
        department.image = image
        department.updated_at = datetime.datetime.now()
        department.save()
        messages.success(request, 'Updated Successfully!')
        return redirect('hospital_department_list')

def hospital_department_delete(request, id):
    if request.method == 'POST':
        try:
            department = get_object_or_404(models.HospitalDepartment, id=id)
            department.delete()
            return JsonResponse({'success': True, 'message': 'Department Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


# Hospital Facilities
def hospital_facilities_list(request):
    hospital_facilities = models.HospitalFacility.objects.all()
    context = {
        'hospital_facilities': hospital_facilities,
    }
    return render(request, 'admin/hospital_facilities_list.html', context)

def hospital_facility_create(request):
    if request.method == "GET":
        hospitals = models.Hospital.objects.all()
        context = {
            "hospitals": hospitals,
        }
        return render(request, "admin/hospital_facility_create.html", context)

    if request.method == 'POST':
        hospital_id = request.POST.get('hospital')
        facility_name = request.POST.get('facility_name')
        facility_icon = request.FILES.get('facility_icon')

        if not facility_icon:
            default_icon_path = os.path.join(settings.STATIC_URL, 'images', 'default_icon.png')
            if os.path.exists(default_icon_path):
                with open(default_icon_path, 'rb') as f:
                    icon = ContentFile(f.read(), 'default_icon.png')
            else:
                icon = None

        hospital_facility = models.HospitalFacility(
            hospital_id=hospital_id,
            facility=facility_name,
            icon=facility_icon,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
        )
        hospital_facility.save()
        messages.success(request, 'Added Successfully!')
        return redirect('hospital_facilities_list')

def hospital_facility_edit(request, id):
    facility = get_object_or_404(models.HospitalFacility, id=id)
    hospitals = models.Hospital.objects.all()

    if request.method == "GET":
        context = {
            "hospitals": hospitals,
            "facility": facility,
        }
        return render(request, "admin/hospital_facility_edit.html", context)

    if request.method == 'POST':
        hospital_id = request.POST.get('hospital')
        facility_name = request.POST.get('facility_name')
        icon = request.FILES.get('facility_icon')

        if not icon:
            icon = facility.icon

        facility.hospital_id = hospital_id
        facility.facility = facility_name
        facility.icon = icon
        facility.updated_at = datetime.datetime.now()
        facility.save()
        messages.success(request, 'Updated Successfully!')
        return redirect('hospital_facilities_list')   

def hospital_facility_delete(request, id):
    if request.method == 'POST':
        try:
            facility = get_object_or_404(models.HospitalFacility, id=id)
            facility.delete()
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})



# Hospital Doctors
def hospital_doctors_list(request):
    hospital_doctors = models.HospitalDoctors.objects.all()
    context = {
        "hospital_doctors":hospital_doctors,
    }
    return render(request,"admin/hospital_doctors_list.html",context)

def hospital_doctor_create(request):
    if request.method == "GET":
        hospitals = models.Hospital.objects.all()
        doctors = doctor_module.DoctorDetails.objects.all()
        context = {
            "hospitals": hospitals,
            "doctors": doctors,
        }
        return render(request, "admin/hospital_doctor_create.html", context) 
    
    if request.method == "POST":
        hospital_id = request.POST.get('hospital')
        doctor_id = request.POST.get('doctor')
        join_date = request.POST.get('join_date')
        status = request.POST.get('status')

        hospital = models.Hospital.objects.get(id=hospital_id)
        doctor = doctor_module.DoctorDetails.objects.get(id=doctor_id)
        # Save the new HospitalDoctors entry
        models.HospitalDoctors.objects.create(
            hospital=hospital,
            doctor=doctor,
            unique_code=doctor.dr_unique_code,
            join_date=join_date,
            status=status,
        )
        messages.success(request, 'Added Successfully!')
        return redirect('hospital_doctors_list')

def hospital_doctor_edit(request, id):
    doctor_assignment = get_object_or_404(models.HospitalDoctors, id=id)

    if request.method == 'GET':
        hospitals = models.Hospital.objects.all()
        doctors = doctor_module.DoctorDetails.objects.all()
        context = {
            'doctor_assignment': doctor_assignment,
            'hospitals': hospitals,
            'doctors': doctors,
        }
        return render(request, "admin/hospital_doctor_edit.html", context)

    if request.method == 'POST':
        hospital_id = request.POST.get('hospital')
        doctor_id = request.POST.get('doctor')
        join_date = request.POST.get('join_date')
        status = request.POST.get('status')

        doctor = doctor_module.DoctorDetails.objects.get(id=doctor_id)
        # Updating the HospitalDoctors object
        doctor_assignment.hospital_id = hospital_id
        doctor_assignment.doctor_id = doctor_id
        doctor_assignment.unique_code = doctor.dr_unique_code
        doctor_assignment.join_date = join_date
        doctor_assignment.status = status
        doctor_assignment.updated_at = datetime.datetime.now()
        doctor_assignment.save()
        
        messages.success(request, 'Updated Successfully!')
        return redirect('hospital_doctors_list')

def hospital_doctor_delete(request, id):
    if request.method == 'POST':
        try:
            hospital_doctor = get_object_or_404(models.HospitalDoctors, id=id)
            hospital_doctor.delete()
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


# Insurances
def insurances_list(request):
    insurances = models.Insurance.objects.all()
    context = {
        "insurances":insurances,
    }
    return render(request,"admin/insurances_list.html",context)

def insurance_create(request):
    if request.method == "GET":
        return render(request, "admin/insurance_create.html")
    
    if request.method == "POST":
        # Insurance details
        insurance_name = request.POST.get('insurance_name')
        insurance_link = request.POST.get('insurance_link')
        status = request.POST.get('status')

        # File handling
        insurance_logo = request.FILES.get('insurance_logo')
        if not insurance_logo:
            default_image_path = os.path.join(settings.STATIC_ROOT, 'images', 'default_image.png')
            with open(default_image_path, 'rb') as f:
                insurance_logo = default_storage.save('insurance_logos/default_image.png', ContentFile(f.read()))
        
        
        
        # Create Insurance instance
        insurance = models.Insurance(
            insurance_name=insurance_name,
            insurance_logo=insurance_logo,
            insurance_link=insurance_link,
            status=status,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
        )
        insurance.save()
        messages.success(request, 'Added Successfully!')
        return redirect('insurances_list')

def insurance_edit(request, id):
    insurance = get_object_or_404(models.Insurance, id=id)
    if request.method == 'GET':
        context = {
            'insurance': insurance,
        }
        return render(request, "admin/insurance_edit.html", context)
    
    if request.method == 'POST':
        insurance_name = request.POST.get('insurance_name')
        insurance_link = request.POST.get('insurance_link')
        status = request.POST.get('status')
        insurance_logo = request.FILES.get('insurance_logo')

        # Handling the default image fallback
        if not insurance_logo:
            if insurance.insurance_logo:
                insurance_logo = insurance.insurance_logo
            else:
                default_image_path = os.path.join(settings.STATIC_ROOT, 'images', 'default_image.png')
                with open(default_image_path, 'rb') as f:
                    insurance_logo = default_storage.save('insurance_logos/default_image.png', f)

        # Update the fields
        insurance.insurance_name = insurance_name
        insurance.insurance_link = insurance_link
        insurance.status = status
        insurance.insurance_logo = insurance_logo

        # Save the updated insurance
        insurance.save()

        # Success message
        messages.success(request, 'Details Dpdated successfully!')

        return redirect('insurances_list')

def insurance_delete(request, id):
    insurance = get_object_or_404(models.Insurance, id=id)
    insurance.delete()
    messages.success(request, 'Deleted successfully!')
    return redirect('insurances_list')


# Hospital Insurances
def hospital_insurance_list(request):
    hospital_insurances = models.HospitalInsurance.objects.all()
    context = {
        "hospital_insurances": hospital_insurances,
    }
    return render(request, "admin/hospital_insurance_list.html", context)

def hospital_insurance_create(request):
    if request.method == "GET":
        hospitals = models.Hospital.objects.all()
        insurances = models.Insurance.objects.all()
        context = {
            "hospitals":hospitals,
            "insurances":insurances,
        }
        return render(request, "admin/hospital_insurance_create.html",context)
    
    if request.method == "POST":
        hospital_id = request.POST.get('hospital')
        insurance_id = request.POST.get('insurance')
        status = request.POST.get('status')
        
        if hospital_id and insurance_id:
            try:
                hospital = models.Hospital.objects.get(id=hospital_id)
                insurance = models.Insurance.objects.get(id=insurance_id)
                models.HospitalInsurance.objects.create(
                    hospital=hospital,
                    insurance=insurance,
                    status=status
                )
                messages.success(request, 'Added Successfully!')
                return redirect('hospital_insurance_list')  # Redirect to the list page or another view
            except models.Hospital.DoesNotExist:
                return HttpResponse("Hospital not found.", status=404)
            except models.Insurance.DoesNotExist:
                return HttpResponse("Insurance not found.", status=404)
        
        return HttpResponse("Invalid data submitted.", status=400)

def hospital_insurance_edit(request, id):
    hospital_insurance = get_object_or_404(models.HospitalInsurance, id=id)
    hospitals = models.Hospital.objects.all()
    insurances = models.Insurance.objects.all()
    if request.method == 'GET':
        context = {
            'hospital_insurance': hospital_insurance,
            "hospitals":hospitals,
            "insurances":insurances,
        }
        return render(request, "admin/hospital_insurance_edit.html", context)
    
    if request.method == "POST":
        hospital_id = request.POST.get("hospital")
        insurance_id = request.POST.get("insurance")
        status = request.POST.get("status")

        # Updating the hospital insurance record
        hospital_insurance.hospital_id = hospital_id
        hospital_insurance.insurance_id = insurance_id
        hospital_insurance.status = status
        hospital_insurance.save()
        messages.success(request, 'Updated successfully!')
        return redirect("hospital_insurance_list")

def hospital_insurance_delete(request, id):
    hospital_insurance = get_object_or_404(models.HospitalInsurance, id=id)
    hospital_insurance.delete()
    messages.success(request, 'Deleted successfully!')
    return redirect('hospital_insurance_list')


# Lab 
def laboratories(request):
    laboratories = adminModel.Laboratory.objects.all()
    context = {
        "laboratories": laboratories,
    }
    return render(request, "lab/laboratories_list.html", context)

def laboratories_create(request):
    if request.method == "GET":
        return render(request, "lab/laboratories_create.html")

    if request.method == "POST":
        lab_name = request.POST.get('lab_name')
        username = request.POST.get('username')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state_province = request.POST.get('state_province')
        postal_code = request.POST.get('postal_code')
        contact_number = request.POST.get('contact_number')
        alternate_number = request.POST.get('alternate_number')
        email = request.POST.get('email')
        website = request.POST.get('website')
        operating_hours = request.POST.get('operating_hours')
        password = request.POST.get('password')
        specializations = request.POST.get('specializations')
        lab_commission = request.POST.get('lab_commission')
        description = request.POST.get('description')
        insurance_accepted = request.POST.get('insurance_accepted')
        payment_methods = request.POST.get('payment_methods')
        emergency_services = request.POST.get('emergency_services')
        home_sample_collection = request.POST.get('home_sample_collection')
        report_delivery_options = request.POST.get('report_delivery_options')
        promote = request.POST.get('promote')
        status = request.POST.get('status')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        # Handle file upload
        lab_image = request.FILES.get('lab_image')
        print(lab_image)
        lab_image_url = None
        if lab_image:
            fs = FileSystemStorage()
            lab_image_url = fs.save(lab_image.name, lab_image)

        # Create a laboratory object (assuming you have a model defined)
        adminModel.Laboratory.objects.create(
            lab_name=lab_name, username=username, address=address, city=city,
            state_province=state_province, postal_code=postal_code, contact_number=contact_number,
            alternate_number=alternate_number, email=email, website=website, operating_hours=operating_hours,
            password=make_password(password), specializations=specializations, lab_commission=lab_commission,
            description=description, insurance_accepted=insurance_accepted, payment_methods=payment_methods,
            emergency_services=emergency_services, home_sample_collection=home_sample_collection,
            report_delivery_options=report_delivery_options, promote=promote, status=status,
            latitude=latitude, longitude=longitude, lab_image=lab_image_url 
        )
        messages.success(request, 'Create Successfully!')
        return redirect('laboratories_list')

    return render(request, "lab/laboratories_create.html")
    
def laboratories_delete(request, id):
    if request.method == 'POST':
        try:
            laboratory = get_object_or_404(adminModel.Laboratory, id=id)
            laboratory.delete()
            messages.success(request, 'Deleted Successfully!')
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


def laboratories_edit(request, id):
    try:
        lab = adminModel.Laboratory.objects.get(id=id)
    except adminModel.Laboratory.DoesNotExist:
        return HttpResponse("Laboratory not found.", status=404)

    if request.method == "GET":
        context = {
            'lab': lab,
        }
        return render(request, "lab/laboratories_edit.html", context)

    if request.method == "POST":
        lab.lab_name = request.POST.get('lab_name')
        lab.description = request.POST.get('description')
        lab.address = request.POST.get('address')
        lab.city = request.POST.get('city')  # New field
        lab.state_province = request.POST.get('state_province')  # New field
        lab.postal_code = request.POST.get('postal_code')  # New field
        lab.contact_number = request.POST.get('contact_number')  # New field
        lab.alternate_number = request.POST.get('alternate_number')  # New field
        
        lab.website = request.POST.get('website')  # New field
        lab.operating_hours = request.POST.get('operating_hours')  # New field
        lab.specializations = request.POST.get('specializations')  # New field
        lab.lab_commission = request.POST.get('lab_commission')
        lab.insurance_accepted = request.POST.get('insurance_accepted')  # New field
        lab.payment_methods = request.POST.get('payment_methods')  # New field
        lab.emergency_services = request.POST.get('emergency_services')  # New field
        lab.home_sample_collection = request.POST.get('home_sample_collection')  # New field
        lab.report_delivery_options = request.POST.get('report_delivery_options')  # New field
        lab.promote = request.POST.get('promote')  # New field
        lab.latitude = request.POST.get('latitude')
        lab.longitude = request.POST.get('longitude')
        lab.status = request.POST.get('status')

        if 'lab_image' in request.FILES:
            lab.lab_image = request.FILES.get('lab_image')
        
        if lab.lab_name and lab.email and lab.contact_number:
            try:
                lab.save()
                messages.success(request, 'Updated successfully!')
                return redirect('laboratories_list')
            except Exception as e:
                messages.error(request,f"An error occurred: {str(e)}", status=500)
                return redirect('laboratories_list')
        else:
            messages.error(request,"Invalid data submitted.", status=400)
            return redirect('laboratories_list')
        

def lab_tags(request):
    lab_tags = adminModel.LabTag.objects.all()
    context = {
        "lab_tags": lab_tags,
    }
    return render(request, "lab/lab_tags_list.html", context)


def lab_tags_create(request):
    if request.method == 'POST':
        tag_name = request.POST.get('tag_name')
        status = request.POST.get('status')

        # Create a new LabTag object and save it
        adminModel.LabTag.objects.create(tag_name=tag_name, status=status)
        messages.success(request, 'Lab Tag created successfully!')
        return redirect('lab_tags_list')
    return render(request, 'lab/lab_tags_create.html')


def lab_tags_delete(request, id):
    if request.method == 'POST':
        try:
            LabTag = get_object_or_404(adminModel.LabTag, id=id)
            LabTag.delete()
            messages.success(request, 'Deleted Successfully!')
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
        
def lab_tags_edit(request, id):
    lab_tag = get_object_or_404(adminModel.LabTag, id=id)
    
    if request.method == 'POST':
        tag_name = request.POST.get('tag_name')
        status = request.POST.get('status')

        # Update the LabTag object with the new data
        lab_tag.tag_name = tag_name
        lab_tag.status = status
        lab_tag.save()

        messages.success(request, 'Lab Tag updated successfully!')
        return redirect('lab_tags_list')
    return render(request, 'lab/lab_tags_edit.html', {'lab_tag': lab_tag})


def services_list(request):
    services = adminModel.Service.objects.all()
    context = {
        'services':services,
    }
    return render(request, "lab/services_list.html", context)

def services_create(request):
    if request.method == 'POST':
        service_name = request.POST.get('service_name')
        status = request.POST.get('status')

        # Create a new Service object and save it
        adminModel.Service.objects.create(service_name=service_name, status=status)
        messages.success(request, 'Service created successfully!')
        return redirect('services_list')

    return render(request, 'lab/services_create.html')


def services_edit(request, id):
    service = get_object_or_404(adminModel.Service, id=id)

    if request.method == 'POST':
        service_name = request.POST.get('service_name')
        status = request.POST.get('status')
        service.service_name = service_name
        service.status = status
        service.save()

        messages.success(request, 'Service updated successfully!')
        return redirect('services_list')

    return render(request, 'lab/services_edit.html', {'service': service})


def services_delete(request, id):
    if request.method == 'POST':
        try:
            service = get_object_or_404(adminModel.Service, id=id)
            service.delete()
            messages.success(request, 'Deleted Successfully!')
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
        
# Lab Service List
def lab_services_list(request):
    lab_services = adminModel.LabService.objects.all()
    context = {
        'lab_services': lab_services,
    }
    return render(request, "lab/lab_services_list.html", context)

# Lab Service Create
def lab_services_create(request):
    if request.method == 'POST':
        lab_id = request.POST.get('lab_id')
        service_id = request.POST.get('service_id')
        status = request.POST.get('status')

        lab = get_object_or_404(adminModel.Laboratory, id=lab_id)
        service = get_object_or_404(adminModel.Service, id=service_id)

        # Create a new LabService object and save it
        adminModel.LabService.objects.create(
            laboratory=lab,
            service=service,
            status=status
        )
        messages.success(request, 'Lab service created successfully!')
        return redirect('lab_services_list')

    # Get labs and services to display in the form
    labs = adminModel.Laboratory.objects.all()
    services = adminModel.Service.objects.all()
    context = {
        'labs': labs,
        'services': services,
    }
    return render(request, 'lab/lab_services_create.html', context)

# Lab Service Edit
def lab_services_edit(request, id):
    lab_service = get_object_or_404(adminModel.LabService, id=id)

    if request.method == 'POST':
        lab_service.laboratory_id = request.POST.get('lab_id')
        lab_service.service_id = request.POST.get('service_id')
        lab_service.is_emergency_service = request.POST.get('is_emergency_service') == 'on'  # Correctly handle boolean
        lab_service.status = request.POST.get('status')
        lab_service.save()

        messages.success(request, 'Lab service updated successfully!')
        return redirect('lab_services_list')

    # Get labs and services to display in the form
    labs = adminModel.Laboratory.objects.all()
    services = adminModel.Service.objects.all()
    context = {
        'lab_service': lab_service,
        'labs': labs,
        'services': services,
    }
    return render(request, 'lab/lab_services_edit.html', context)

# Lab Service Delete
def lab_services_delete(request, id):
    if request.method == 'POST':
        try:
            lab_service = get_object_or_404(adminModel.LabService, id=id)
            lab_service.delete()
            messages.success(request, 'Lab service deleted successfully!')
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
        
# List Lab Banners
def lab_banners_list(request):
    lab_banners = adminModel.LabBanner.objects.all()
    context = {
        'lab_banners': lab_banners,
    }
    return render(request, 'lab/lab_banners_list.html', context)

# Create Lab Banner
def lab_banners_create(request):
    if request.method == 'POST':
        lab_id = request.POST.get('laboratory_id')
        link = request.POST.get('link')
        banner = request.FILES.get('banner')
        status = request.POST.get('status')
        lab = get_object_or_404(adminModel.Laboratory, id=lab_id)
        lab_banner = adminModel.LabBanner(
            laboratory=lab,
            link=link,
            banner=banner,
            status=status,
        )
        lab_banner.save()
        messages.success(request, 'Lab banner created successfully!')
        return redirect('lab_banners_list')
    laboratories = adminModel.Laboratory.objects.all()
    context = {
        'laboratories': laboratories,
    }
    return render(request, 'lab/lab_banners_create.html', context)

# Edit Lab Banner
def lab_banners_edit(request, id):
    lab_banner = get_object_or_404(adminModel.LabBanner, id=id)

    if request.method == 'POST':
        lab_banner.laboratory_id = request.POST.get('laboratory_id')
        lab_banner.link = request.POST.get('link')
        if request.FILES.get('banner'):
            lab_banner.banner = request.FILES['banner']
        lab_banner.status = request.POST.get('status')
        lab_banner.save()

        messages.success(request, 'Lab banner updated successfully!')
        return redirect('lab_banners_list')

    laboratories = adminModel.Laboratory.objects.all()
    context = {
        'lab_banner': lab_banner,
        'laboratories': laboratories,
    }
    return render(request, 'lab/lab_banners_edit.html', context)

# Delete Lab Banner
def lab_banners_delete(request, id):
    if request.method == 'POST':
        try:
            lab_banner = get_object_or_404(adminModel.LabBanner, id=id)
            lab_banner.delete()
            messages.success(request, 'Lab banner deleted successfully!')
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
        

