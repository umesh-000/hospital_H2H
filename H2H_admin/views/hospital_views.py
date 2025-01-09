from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.core.files.storage import default_storage
from django.views.decorators.http import require_POST
from django.core.files.base import ContentFile
from django.core.paginator import Paginator
from H2H_admin import models as adminModel
from django.http import JsonResponse
from django.contrib import messages
from django.conf import settings
import logging
import json
import os


logger = logging.getLogger(__name__)

# Hospital
@login_required
def hospital_list(request):
    hospitals = adminModel.Hospital.objects.select_related('user').all()
    paginator = Paginator(hospitals, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"admin/hospital/hospital_list.html",{"hospital_list":page_obj})

@login_required
def hospital_create(request):
    if request.method == "GET":
        return render(request, "admin/hospital/hospital_add.html")

    if request.method == "POST":
        # User details
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if username or email already exists
        if adminModel.User.objects.filter(username=user_name).exists():
            messages.error(request, "Username already exists!")
            return redirect('hospital_create')
        if adminModel.User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('hospital_create')

        # Create User
        user = adminModel.User.objects.create(
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

        # Handle file uploads
        hospital_image_files = request.FILES.getlist('hospital_images')
        hospital_logo = request.FILES.get('hospital_logo')

        # Create Hospital instance
        hospital = adminModel.Hospital.objects.create(
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
            hospital_image=hospital_image_files[0] if hospital_image_files else None,  # First image as hospital_image
            hospital_logo=hospital_logo,
            city=city
        )

        # Save additional images
        for image_file in hospital_image_files:
            adminModel.HospitalImage.objects.create(hospital=hospital, image=image_file)

        messages.success(request, "Hospital created successfully!")
        return redirect('hospital_list')

    return render(request, "admin/hospital/hospital_add.html")
    
@login_required    
def hospital_edit(request, id):
    hospital = get_object_or_404(adminModel.Hospital, id=id)
    
    if request.method == "GET":
        # Render the form with existing hospital details
        context = {
            'hospital': hospital,
            'hospital_images': hospital.images.all(),
        }
        return render(request, 'admin/hospital/hospital_edit.html', context)
    
    if request.method == "POST":
        try:
            # Update hospital fields
            hospital.hospital_name = request.POST.get('hospital_name', hospital.hospital_name)
            hospital.user.username = request.POST.get('user_name', hospital.user.username)
            hospital.phone_number = request.POST.get('phone_number', hospital.phone_number)
            hospital.user.email = request.POST.get('email', hospital.user.email)
            hospital.city = request.POST.get('city', hospital.city)
            hospital.latitude = request.POST.get('latitude', hospital.latitude)
            hospital.longitude = request.POST.get('longitude', hospital.longitude)
            hospital.open_time = request.POST.get('open_time', hospital.open_time)
            hospital.close_time = request.POST.get('close_time', hospital.close_time)
            hospital.website_url = request.POST.get('website_url', hospital.website_url)
            hospital.type = request.POST.get('type', hospital.type)
            hospital.status = request.POST.get('status', hospital.status)
            hospital.is_recommended = request.POST.get('isRecommended', hospital.is_recommended)
            hospital.address = request.POST.get('address', hospital.address)
            hospital.description = request.POST.get('description', hospital.description)

            # Handle file uploads
            hospital_logo = request.FILES.get('hospital_logo')
            if hospital_logo:
                hospital.hospital_logo = hospital_logo
            hospital.save()

            # Save additional images
            hospital_image_files = request.FILES.getlist('hospital_images')
            for image_file in hospital_image_files:
                adminModel.HospitalImage.objects.create(hospital=hospital, image=image_file)

            messages.success(request, 'Hospital details updated successfully!')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")

        return redirect('hospital_list')

@login_required
def hospital_delete(request, id):
    if request.method == 'POST':
        try:
            hospital = get_object_or_404(adminModel.Hospital, id=id)
            user = hospital.user
            user.delete()
            hospital.delete()
            messages.success(request, 'Hospital Deleted successfully!')
            return JsonResponse({'success': True, 'message': 'Hospital and associated user deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f"Error: {str(e)}"})
    return JsonResponse({'success': False, 'message': 'Invalid request method. Use POST.'})



# Ward
@login_required
def ward_list(request):
    if request.method == "GET":
        ward_list = adminModel.Ward.objects.all()
        paginator = Paginator(ward_list, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context ={
            "ward_list":page_obj,
        }
        return render(request,"admin/hospital//ward_list.html",context)

@login_required
def ward_create(request):
    if request.method == "GET":
        hospitals = adminModel.Hospital.objects.all()
        context ={
            "hospitals":hospitals,
        }
        return render(request,"admin/hospital//add_ward.html",context)


    if request.method == 'POST':
        hospital_id = request.POST.get('hospital_id')
        ward_name = request.POST.get('ward_name')
        status = request.POST.get('status')
        hospital = adminModel.Hospital.objects.get(id=hospital_id)
        ward = adminModel.Ward(hospital=hospital,ward_name=ward_name,status=status)
        ward.save()
        messages.success(request, 'Ward Created successfully!')
        return redirect('ward_list')

@login_required
def ward_edit(request,id):
    ward = get_object_or_404(adminModel.Ward, id=id)
    hospitals = adminModel.Hospital.objects.all()
    if request.method=="GET":
        return render(request, 'admin/hospital//edit_ward.html', {'ward': ward,"hospitals":hospitals})

    if request.method == 'POST':
        hospital_id = request.POST.get('hospital_id')
        ward_name = request.POST.get('ward_name')
        status = request.POST.get('status')
        hospital = get_object_or_404(adminModel.Hospital, id=hospital_id)
        ward.hospital = hospital
        ward.ward_name = ward_name
        ward.status = int(status)
        ward.save()
        messages.success(request, 'Ward Updated successfully!')
        return redirect('ward_list')
    
@login_required
def ward_delete(request, id):
    if request.method == 'POST':
        try:
            ward = get_object_or_404(adminModel.Ward, id=id)
            ward.delete()
            messages.success(request, 'Ward Deleted successfully!')
            return JsonResponse({'success': True, 'message': 'Ward deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})



# Bed
@login_required
def bed_list(request):
    if request.method == "GET":
        bed_list = adminModel.Bed.objects.all()
        paginator = Paginator(bed_list, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context ={
            "bed_list":page_obj,
        }
        return render(request,"admin/hospital/list_bed.html",context)
    
@login_required
def bed_create(request):
    if request.method == "GET":
        hospitals = adminModel.Hospital.objects.all()
        wards = adminModel.Ward.objects.all()
        context = {
            "hospitals": hospitals,
            "wards": wards,
        }
        return render(request, "admin/hospital/add_bed.html", context)
    
    if request.method == "POST":
        hospital_id = request.POST.get('hospital_id')
        ward_id = request.POST.get('ward_id')
        bed_type = request.POST.get('bed_type')
        bed_count = request.POST.get('bed_count')
        sale_price = request.POST.get('sale_price')
        sale_bed_price = request.POST.get('sale_bed_price')
        status = request.POST.get('status')
        hospital = adminModel.Hospital.objects.get(id=hospital_id)
        ward = adminModel.Ward.objects.get(id=ward_id)
        # Creating a new Bed object
        bed = adminModel.Bed(
            hospital=hospital, ward=ward, bed_type=bed_type,
            bed_count=bed_count, sale_price=sale_price,
            sale_bed_price=sale_bed_price, status=status
        )
        bed.save()
        messages.success(request, 'Bed added successfully!')
        return redirect('bed_list')
    
@login_required
def bed_edit(request, id):
    bed = get_object_or_404(adminModel.Bed, id=id)
    if request.method == "GET":
        hospitals = adminModel.Hospital.objects.all()
        wards = adminModel.Ward.objects.all()
        context = {
            'bed': bed,
            'hospitals': hospitals,
            'wards': wards,
        }
        return render(request, 'admin/hospital/edit_bed.html', context)
    
    if request.method == "POST":
        hospital_id = request.POST.get('hospital_id')
        ward_id = request.POST.get('ward_id')
        bed_type = request.POST.get('bed_type')
        bed_count = request.POST.get('bed_count')
        sale_price = request.POST.get('sale_price')
        sale_bed_price = request.POST.get('sale_bed_price')
        status = request.POST.get('status')

        hospital = adminModel.Hospital.objects.get(id=hospital_id)
        ward = adminModel.Ward.objects.get(id=ward_id)
        # Update the bed object with the new data
        bed.hospital = hospital
        bed.ward = ward
        bed.bed_type = bed_type
        bed.bed_count = bed_count
        bed.sale_price = sale_price
        bed.sale_bed_price = sale_bed_price
        bed.status = status
        bed.save()
        messages.success(request, 'Bed updated successfully!')
        return redirect('bed_list')

@login_required
def bed_delete(request, id):
    if request.method == 'POST':
        try:
            bed = get_object_or_404(adminModel.Bed, id=id)
            bed.delete()
            messages.success(request, 'Bed Deleted successfully!')
            return JsonResponse({'success': True, 'message': 'Bed deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})



# Bed Status
@login_required
def bed_status_list(request):
    bed_statuses = adminModel.BedStatus.objects.select_related('hospital', 'bed').all()
    paginator = Paginator(bed_statuses, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "bed_statuses": page_obj,
    }
    return render(request, 'admin/hospital/bed_status_list.html', context)

@login_required
def bed_status_create(request):
    if request.method == "POST":
        hospital_id = request.POST.get('hospital_id')
        bed_id = request.POST.get('bed_id')
        status = request.POST.get('status')
        hospital = adminModel.Hospital.objects.get(id=hospital_id)
        bed = adminModel.Bed.objects.get(id=bed_id)
        # Creating a new Bed object
        bed_status = adminModel.BedStatus(hospital=hospital,bed=bed,status=status)
        bed_status.save()
        messages.success(request, 'Bed Status Added Successfully!')
        return redirect('bed_status_list')
    if request.method == "GET":
        hospitals = adminModel.Hospital.objects.all()
        beds = adminModel.Bed.objects.all()
        context = {
            "hospitals": hospitals,
            "beds": beds,
        }
        return render(request, 'admin/hospital/create_bed_status.html', context)

@login_required
def bed_status_edit(request, id):
    bed_status = get_object_or_404(adminModel.BedStatus, id=id)

    if request.method == "POST":
        # Get form data
        hospital_id = request.POST.get('hospital_id')
        bed_id = request.POST.get('bed_id')
        status = request.POST.get('status')
        hospital = adminModel.Hospital.objects.get(id=hospital_id)
        bed = adminModel.Bed.objects.get(id=bed_id)
        bed_status.hospital = hospital
        bed_status.bed = bed
        bed_status.status = status
        bed_status.save()
        messages.success(request, 'Bed Status Updated Successfully!')
        return redirect('bed_status_list')

    else:
        hospitals = adminModel.Hospital.objects.all()
        beds = adminModel.Bed.objects.all()
        context = {"hospitals": hospitals,"beds": beds,"bed_status": bed_status}
        return render(request, 'admin/hospital/bed_status_update.html', context)

@login_required
def bed_status_delete(request, id):
    if request.method == 'POST':
        try:
            bed_status = get_object_or_404(adminModel.BedStatus, id=id)
            bed_status.delete()
            messages.success(request, 'Bed Status Deleted Successfully!')
            return JsonResponse({'success': True, 'message': 'Bed Status deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


# Hospital services
@login_required
def hospital_service_list(request):
    hospital_service = adminModel.HospitalService.objects.all()
    paginator = Paginator(hospital_service, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'hospital_service': page_obj,
    }
    return render(request, 'admin/hospital/hospital_services_list.html', context)

@login_required
def hospital_service_create(request):
    if request.method == "GET":
        hospitals = adminModel.Hospital.objects.all()
        context ={"hospitals":hospitals,}
        return render(request,"admin/hospital/hospital_services_create.html",context)

    if request.method == 'POST':
        hospital_id = request.POST.get('hospital')
        service_name = request.POST.get('service_name')
        starting_from = request.POST.get('starting_from')
        service_icon = request.FILES.get('service_icon')
        if not service_icon:
            default_image_path = os.path.join(settings.STATIC_ROOT, 'images', 'default_image.png')
            with open(default_image_path, 'rb') as f:
                service_icon = default_storage.save('service_icons/default_image.png', f)

        hospital = adminModel.Hospital.objects.get(id=hospital_id)          
        hospital_service = adminModel.HospitalService(
            hospital=hospital,
            service_name=service_name,
            starting_from=starting_from,
            service_icon=service_icon,
        )
        hospital_service.save()
        messages.success(request, 'Service Added Successfully!')
        return redirect('hospital_service_list')

@login_required
def hospital_service_edit(request, id):
    service = get_object_or_404(adminModel.HospitalService, id=id)

    if request.method == 'GET':
        hospitals = adminModel.Hospital.objects.all()
        context = {
            'service': service,
            'hospitals': hospitals,
        }
        return render(request, "admin/hospital/hospital_service_edit.html", context)

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

        hospital = adminModel.Hospital.objects.get(id=hospital_id)
        service.hospital = hospital
        service.service_name = service_name
        service.starting_from = starting_from
        service.service_icon = service_icon
        service.save()
        messages.success(request, 'Service Updated Successfully!')
        return redirect('hospital_service_list')

@login_required
def hospital_service_delete(request, id):
    if request.method == 'POST':
        try:
            service = get_object_or_404(adminModel.HospitalService, id=id)
            service.delete()
            messages.success(request, 'Hospital Service Deleted Successfully!')
            return JsonResponse({'success': True, 'message': 'Service Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


# Hospital Department
@login_required
def hospital_department_list(request):
    hospital_department = adminModel.HospitalDepartment.objects.all()
    paginator = Paginator(hospital_department, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'hospital_departments': page_obj,
    }
    return render(request, 'admin/hospital/hospital_departments_list.html',context)

@login_required
def hospital_department_create(request):
    if request.method == "GET":
        hospitals = adminModel.Hospital.objects.all()
        context = {
            "hospitals": hospitals,
        }
        return render(request, "admin/hospital/hospital_department_create.html", context)

    if request.method == 'POST':
        hospital_id = request.POST.get('hospital')
        department_name = request.POST.get('department_name')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        if not image:
            default_image_path = os.path.join(settings.STATIC_ROOT, 'images', 'default_image.png')
            with open(default_image_path, 'rb') as f:
                image = default_storage.save('department_images/default_image.png', f)

        hospital_department = adminModel.HospitalDepartment(
            hospital_id=hospital_id,
            department_name=department_name,
            description=description,
            image=image,
        )
        hospital_department.save()
        messages.success(request, 'Department Added Successfully!')
        return redirect('hospital_department_list')

@login_required
def hospital_department_edit(request, id):
    department = get_object_or_404(adminModel.HospitalDepartment, id=id)
    hospitals = adminModel.Hospital.objects.all()
    if request.method == "GET":
        context = {
            "hospitals": hospitals,
            "department": department,
        }
        return render(request, "admin/hospital/hospital_department_edit.html", context)

    if request.method == 'POST':
        hospital_id = request.POST.get('hospital')
        department_name = request.POST.get('department_name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        if not image:
            image = department.image
        hospital = adminModel.Hospital.objects.get(id=hospital_id)
        department.hospital=hospital
        department.department_name = department_name
        department.description = description
        department.image = image
        department.save()
        messages.success(request, 'Updated Successfully!')
        return redirect('hospital_department_list')

@login_required
def hospital_department_delete(request, id):
    if request.method == 'POST':
        try:
            department = get_object_or_404(adminModel.HospitalDepartment, id=id)
            department.delete()
            messages.success(request, 'Department Deleted Successfully!')
            return JsonResponse({'success': True, 'message': 'Department Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


# Hospital Facilities
@login_required
def hospital_facilities_list(request):
    hospital_facilities = adminModel.HospitalFacility.objects.all()
    paginator = Paginator(hospital_facilities, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'hospital_facilities': page_obj,
    }
    return render(request, 'admin/hospital/hospital_facilities_list.html', context)

@login_required
def hospital_facility_create(request):
    if request.method == "GET":
        hospitals = adminModel.Hospital.objects.all()
        context = {
            "hospitals": hospitals,
        }
        return render(request, "admin/hospital/hospital_facility_create.html", context)

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
        hospital = adminModel.Hospital.objects.get(id=hospital_id)
        hospital_facility = adminModel.HospitalFacility(hospital=hospital,facility=facility_name,icon=facility_icon,)
        hospital_facility.save()
        messages.success(request, 'Added Successfully!')
        return redirect('hospital_facilities_list')

@login_required
def hospital_facility_edit(request, id):
    facility = get_object_or_404(adminModel.HospitalFacility, id=id)
    hospitals = adminModel.Hospital.objects.all()
    if request.method == "GET":
        context = {
            "hospitals": hospitals,
            "facility": facility,
        }
        return render(request, "admin/hospital/hospital_facility_edit.html", context)

    if request.method == 'POST':
        hospital_id = request.POST.get('hospital')
        facility_name = request.POST.get('facility_name')
        icon = request.FILES.get('facility_icon')
        if not icon:
            icon = facility.icon
        hospital = adminModel.Hospital.objects.get(id=hospital_id)
        facility.hospital = hospital
        facility.facility = facility_name
        facility.icon = icon
        facility.save()
        messages.success(request, 'Updated Successfully!')
        return redirect('hospital_facilities_list')   

@login_required
def hospital_facility_delete(request, id):
    if request.method == 'POST':
        try:
            facility = get_object_or_404(adminModel.HospitalFacility, id=id)
            facility.delete()
            messages.success(request, 'Hospital Facility Deleted Successfully!')
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


# Hospital Doctors
@login_required
def hospital_doctors_list(request):
    hospital_doctors = adminModel.HospitalDoctors.objects.all()
    paginator = Paginator(hospital_doctors, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "hospital_doctors":page_obj,
    }
    return render(request,"admin/hospital/hospital_doctors_list.html",context)

@login_required
def hospital_doctor_create(request):
    if request.method == "GET":
        hospitals = adminModel.Hospital.objects.all()
        doctors = adminModel.DoctorDetails.objects.all()
        context = {
            "hospitals": hospitals,
            "doctors": doctors,
        }
        return render(request, "admin/hospital/hospital_doctor_create.html", context) 
    
    if request.method == "POST":
        hospital_id = request.POST.get('hospital')
        doctor_id = request.POST.get('doctor')
        join_date = request.POST.get('join_date')
        status = request.POST.get('status')

        hospital = adminModel.Hospital.objects.get(id=hospital_id)
        doctor = adminModel.DoctorDetails.objects.get(id=doctor_id)
        adminModel.HospitalDoctors.objects.create(hospital=hospital,doctor=doctor,unique_code=doctor.dr_unique_code,join_date=join_date,status=status,)
        messages.success(request, 'Added Successfully!')
        return redirect('hospital_doctors_list')

@login_required
def hospital_doctor_edit(request, id):
    doctor_assignment = get_object_or_404(adminModel.HospitalDoctors, id=id)

    if request.method == 'GET':
        hospitals = adminModel.Hospital.objects.all()
        doctors = adminModel.DoctorDetails.objects.all()
        context = {
            'doctor_assignment': doctor_assignment,
            'hospitals': hospitals,
            'doctors': doctors,
        }
        return render(request, "admin/hospital/hospital_doctor_edit.html", context)

    if request.method == 'POST':
        hospital_id = request.POST.get('hospital')
        doctor_id = request.POST.get('doctor')
        join_date = request.POST.get('join_date')
        status = request.POST.get('status')

        doctor = adminModel.DoctorDetails.objects.get(id=doctor_id)
        hospital = adminModel.Hospital.objects.get(id=hospital_id)
        # Updating the HospitalDoctors object
        doctor_assignment.hospital = hospital
        doctor_assignment.doctor = doctor
        doctor_assignment.unique_code = doctor.dr_unique_code
        doctor_assignment.join_date = join_date
        doctor_assignment.status = status
        doctor_assignment.save()
        
        messages.success(request, 'Updated Successfully!')
        return redirect('hospital_doctors_list')

@login_required
def hospital_doctor_delete(request, id):
    if request.method == 'POST':
        try:
            hospital_doctor = get_object_or_404(adminModel.HospitalDoctors, id=id)
            hospital_doctor.delete()
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


# Symptoms
@login_required
def symptoms_list(request):
    symptoms = adminModel.Symptom.objects.all()
    paginator = Paginator(symptoms, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "admin/symptom_list.html", {'symptoms': page_obj})

@login_required
def symptom_create(request):
    if request.method == "GET":
        specialists = adminModel.SpecialistCategory.objects.all()
        return render(request, "admin/symptom_create.html", {'specialists': specialists})

    if request.method == 'POST':
        specialist_id = request.POST.get('specialist')
        symptom_name = request.POST.get('symptom_name')
        symptom_image = request.FILES.get('symptom_image')
        status = request.POST.get('status')

        if not symptom_image:
            default_image_path = os.path.join(settings.STATIC_ROOT, 'images', 'default_image.png')
            with open(default_image_path, 'rb') as f:
                symptom_image = default_storage.save('symptom_images/default_image.png', f)

        symptom = adminModel.Symptom(
            specialist_id=specialist_id,
            symptom_name=symptom_name,
            symptom_image=symptom_image,
            status=status,
        )
        symptom.save()
        messages.success(request, 'Created successfully!')
        return redirect('symptoms_list')

@login_required
def symptom_edit(request, id):
    symptom = get_object_or_404(adminModel.Symptom, id=id)
    specialists = adminModel.SpecialistCategory.objects.all()

    if request.method == 'GET':
        context = {
            'symptom': symptom,
            'specialists': specialists,
        }
        return render(request, "admin/symptom_edit.html", context)

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
        specialist = adminModel.SpecialistCategory.objects.get(id=specialist_id)
        symptom.specialist = specialist
        symptom.symptom_name = symptom_name
        symptom.symptom_image = symptom_image
        symptom.status = status
        symptom.save()
        messages.success(request, 'Updated Successfully!')
        return redirect('symptoms_list')
    
@login_required
def symptom_delete(request, id):
    if request.method == 'POST':
        try:
            symptom = get_object_or_404(adminModel.Symptom, id=id)
            symptom.delete()
            messages.success(request, 'Deleted Successfully!')
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

# Specialist
@login_required
def specialist_list(request):
    specialist_categories = adminModel.SpecialistCategory.objects.all()
    paginator = Paginator(specialist_categories, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "admin/specialist_list.html", {'specialist_categories': page_obj})

@login_required
def specialist_create(request):
    if request.method == "GET":
        return render(request, "admin/specialist_create.html")

    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        category_image = request.FILES.get('category_image')
        status = request.POST.get('status')
        if not category_image:
            default_image_path = os.path.join(settings.STATIC_ROOT, 'images', 'default_image.png')
            with open(default_image_path, 'rb') as f:
                category_image = default_storage.save('category_images/default_image.png', f)

        specialist_category = adminModel.SpecialistCategory(
            category_name=category_name,
            category_image=category_image,
            status=status,
        )
        specialist_category.save()
        messages.success(request, 'Created Successfully!')
        return redirect('specialist_list')

@login_required
def specialist_edit(request, id):
    specialist_category = get_object_or_404(adminModel.SpecialistCategory, id=id)

    if request.method == 'GET':
        context = {
            'specialist_category': specialist_category,
        }
        return render(request, "admin/specialist_edit.html", context)

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
        specialist_category.save()
        messages.success(request, 'Updated Successfully!')
        return redirect('specialist_list')

@login_required
def specialist_delete(request, id):
    if request.method == 'POST':
        try:
            specialist_category = get_object_or_404(adminModel.SpecialistCategory, id=id)
            specialist_category.delete()
            messages.success(request, 'Deleted Successfully!')
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


# bed booking 
def bed_requests(request):
    bed_list = adminModel.BedBooking.objects.all()
    paginator = Paginator(bed_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "bed_list": page_obj,
    }
    return render(request, 'admin/hospital/bed_booking_requests_list.html', context)

@require_POST
def update_booking_status(request):
    data = json.loads(request.body)
    booking_id = data.get('booking_id')
    new_status = data.get('status')
    try:
        booking = adminModel.BedBooking.objects.get(id=booking_id)
        booking.status = new_status
        booking.save()
        return JsonResponse({'success': True, 'message': 'Status updated successfully.'})
    except adminModel.BedBooking.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Booking not found.'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})