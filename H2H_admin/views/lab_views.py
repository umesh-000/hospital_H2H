from django.contrib.auth.hashers import make_password,check_password
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from django.core.files.base import ContentFile
from accounts import models as account_module
from django.core.paginator import Paginator
from H2H_admin import models as adminModel
import doctor.models as doctor_module
from django.contrib import messages
from django.db import transaction
from django.utils import timezone
from django.conf import settings
from hospital import models
import traceback
import datetime
import logging
import json
import os
from H2H_admin import utils

logger = logging.getLogger(__name__)


# Lab 
@login_required
def laboratories(request):
    laboratories = account_module.Laboratory.objects.all()
    paginator = Paginator(laboratories, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "laboratories": page_obj,
    }
    return render(request, "admin/lab/laboratories_list.html", context)

@login_required
def laboratories_create(request):
    if request.method == "GET":
        print("GET")
        return render(request, "admin/lab/laboratories_create.html")

    if request.method == "POST":
        try:
            print("POST")
            with transaction.atomic():
                user = account_module.User.objects.create( username=request.POST.get('username'), email=request.POST.get('email'), user_type='lab', password=make_password(request.POST.get('password')))
                print("LABuser")
                lab_image = request.FILES.get('lab_image')
                lab_image_url = None
                if lab_image:
                    fs = FileSystemStorage()
                    lab_image_url = fs.save(lab_image.name, lab_image)

                # Create the lab profile
                print("LAB")
                account_module.Laboratory.objects.create(
                    user=user,
                    lab_name=request.POST.get('lab_name'), address=request.POST.get('address'), city=request.POST.get('city'),
                    state_province=request.POST.get('state_province'), postal_code=request.POST.get('postal_code'),
                    contact_number=request.POST.get('contact_number'), alternate_number=request.POST.get('alternate_number'),
                    website=request.POST.get('website'), operating_hours=request.POST.get('operating_hours'),
                    specializations=request.POST.get('specializations'), lab_commission=request.POST.get('lab_commission'),
                    description=request.POST.get('description'), insurance_accepted=request.POST.get('insurance_accepted'),
                    payment_methods=request.POST.get('payment_methods'), emergency_services=request.POST.get('emergency_services'),
                    home_sample_collection=request.POST.get('home_sample_collection'), report_delivery_options=request.POST.get('report_delivery_options'),
                    promote=request.POST.get('promote'), status=request.POST.get('status'),
                    latitude=request.POST.get('latitude'), longitude=request.POST.get('longitude'), lab_image=lab_image_url,
                )

                messages.success(request, 'Laboratory created successfully!')
                return redirect('laboratories_list')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('laboratories_create')

@login_required
def laboratories_edit(request, id):
    lab = get_object_or_404(account_module.Laboratory, id=id)

    if request.method == "GET":
        return render(request, "admin/lab/laboratories_edit.html", {'lab': lab})

    if request.method == "POST":
        try:
            with transaction.atomic():
                lab.lab_name = request.POST.get('lab_name')
                lab.user.username = request.POST.get('username')
                lab.user.email = request.POST.get('email')
                lab.address = request.POST.get('address')
                lab.city = request.POST.get('city')
                lab.state_province = request.POST.get('state_province')
                lab.postal_code = request.POST.get('postal_code')
                lab.contact_number = request.POST.get('contact_number')
                lab.alternate_number = request.POST.get('alternate_number')
                lab.website = request.POST.get('website')
                lab.operating_hours = request.POST.get('operating_hours')
                lab.specializations = request.POST.get('specializations')
                lab.lab_commission = request.POST.get('lab_commission')
                lab.description = request.POST.get('description')
                lab.insurance_accepted = request.POST.get('insurance_accepted')
                lab.payment_methods = request.POST.get('payment_methods')
                lab.emergency_services = request.POST.get('emergency_services')
                lab.home_sample_collection = request.POST.get('home_sample_collection')
                lab.report_delivery_options = request.POST.get('report_delivery_options')
                lab.promote = request.POST.get('promote')
                lab.status = request.POST.get('status')
                lab.latitude = request.POST.get('latitude')
                lab.longitude = request.POST.get('longitude')

                # Handle file upload
                if 'lab_image' in request.FILES:
                    fs = FileSystemStorage()
                    lab.lab_image = fs.save(request.FILES['lab_image'].name, request.FILES['lab_image'])

                lab.save()
                lab.user.save()
                messages.success(request, 'Laboratory updated successfully!')
                return redirect('laboratories_list')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('laboratories_edit', id=id)

@login_required
def laboratories_delete(request, id):
    if request.method == 'POST':
        try:
            laboratory = get_object_or_404(account_module.Laboratory, id=id)
            laboratory.delete()
            laboratory.user.delete()
            messages.success(request, 'Deleted Successfully!')
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


# Laboratory Tags
@login_required
def lab_tags(request):
    lab_tags = adminModel.LabTag.objects.all()
    paginator = Paginator(lab_tags, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "lab_tags": page_obj,
    }
    return render(request, "admin/lab/lab_tags_list.html", context)

@login_required
def lab_tags_create(request):
    if request.method == 'POST':
        tag_name = request.POST.get('tag_name')
        status = request.POST.get('status')
        adminModel.LabTag.objects.create(tag_name=tag_name, status=status)
        messages.success(request, 'Lab Tag created successfully!')
        return redirect('lab_tags_list')
    return render(request, 'admin/lab/lab_tags_create.html')
        
@login_required
def lab_tags_edit(request, id):
    lab_tag = get_object_or_404(adminModel.LabTag, id=id)
    if request.method == 'POST':
        tag_name = request.POST.get('tag_name')
        status = request.POST.get('status')
        lab_tag.tag_name = tag_name
        lab_tag.status = status
        lab_tag.save()
        messages.success(request, 'Lab Tag updated successfully!')
        return redirect('lab_tags_list')
    return render(request, 'admin/lab/lab_tags_edit.html', {'lab_tag': lab_tag})

@login_required
def lab_tags_delete(request, id):
    if request.method == 'POST':
        try:
            LabTag = get_object_or_404(adminModel.LabTag, id=id)
            LabTag.delete()
            messages.success(request, 'Deleted Successfully!')
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})


# Laboratory Service
@login_required
def services_list(request):
    services = adminModel.Service.objects.all()
    paginator = Paginator(services, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'services':page_obj,
    }
    return render(request, "admin/lab/services_list.html", context)

@login_required
def services_create(request):
    if request.method == 'POST':
        service_name = request.POST.get('service_name')
        status = request.POST.get('status')
        adminModel.Service.objects.create(service_name=service_name, status=status)
        messages.success(request, 'Service created successfully!')
        return redirect('services_list')

    return render(request, 'admin/lab/services_create.html')

@login_required
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
    return render(request, 'admin/lab/services_edit.html', {'service': service})

@login_required
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
@login_required
def lab_services_list(request):
    lab_services = adminModel.LabService.objects.all()
    paginator = Paginator(lab_services, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'lab_services': page_obj,
    }
    return render(request, "admin/lab/lab_services_list.html", context)

@login_required
def lab_services_create(request):
    if request.method == 'POST':
        lab_id = request.POST.get('lab_id')
        service_id = request.POST.get('service_id')
        status = request.POST.get('status')
        lab = get_object_or_404(account_module.Laboratory, id=lab_id)
        service = get_object_or_404(adminModel.Service, id=service_id)
        adminModel.LabService.objects.create(laboratory=lab,service=service,status=status)
        messages.success(request, 'Lab service created successfully!')
        return redirect('lab_services_list')

    labs = account_module.Laboratory.objects.all()
    services = adminModel.Service.objects.all()
    context = {
        'labs': labs,
        'services': services,
    }
    return render(request, 'admin/lab/lab_services_create.html', context)

@login_required
def lab_services_edit(request, id):
    lab_service = get_object_or_404(adminModel.LabService, id=id)
    if request.method == 'POST':
        lab = get_object_or_404(account_module.Laboratory, id=request.POST.get('lab_id'))
        service = get_object_or_404(adminModel.Service, id=request.POST.get('service_id'))
        lab_service.laboratory = lab
        lab_service.service = service
        lab_service.is_emergency_service = request.POST.get('is_emergency_service') == 'on' 
        lab_service.status = request.POST.get('status')
        lab_service.save()
        messages.success(request, 'Lab service updated successfully!')
        return redirect('lab_services_list')

    # Get labs and services to display in the form
    labs = account_module.Laboratory.objects.all()
    services = adminModel.Service.objects.all()
    context = {
        'lab_service': lab_service,
        'labs': labs,
        'services': services,
    }
    return render(request, 'admin/lab/lab_services_edit.html', context)

@login_required
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
@login_required
def lab_banners_list(request):
    lab_banners = adminModel.LabBanner.objects.all()
    paginator = Paginator(lab_banners, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = { 'lab_banners': page_obj, }
    return render(request, 'admin/lab/lab_banners_list.html', context)

@login_required
def lab_banners_create(request):
    if request.method == 'POST':
        lab_id = request.POST.get('laboratory_id')
        link = request.POST.get('link')
        banner = request.FILES.get('banner')
        status = request.POST.get('status')
        lab = get_object_or_404(account_module.Laboratory, id=lab_id)
        lab_banner = adminModel.LabBanner( laboratory=lab, link=link, banner=banner, status=status, )
        lab_banner.save()
        messages.success(request, 'Lab banner created successfully!')
        return redirect('lab_banners_list')
    laboratories = account_module.Laboratory.objects.all()
    context = { 'laboratories': laboratories, }
    return render(request, 'admin/lab/lab_banners_create.html', context)

@login_required
def lab_banners_edit(request, id):
    lab_banner = get_object_or_404(adminModel.LabBanner, id=id)
    if request.method == 'POST':
        lab = get_object_or_404(account_module.Laboratory, id=request.POST.get('laboratory_id'))
        lab_banner.laboratory = lab
        lab_banner.link = request.POST.get('link')
        if request.FILES.get('banner'):
            lab_banner.banner = request.FILES['banner']
        lab_banner.status = request.POST.get('status')
        lab_banner.save()
        messages.success(request, 'Lab banner updated successfully!')
        return redirect('lab_banners_list')
    laboratories = account_module.Laboratory.objects.all()
    context = { 'lab_banner': lab_banner, 'laboratories': laboratories, }
    return render(request, 'admin/lab/lab_banners_edit.html', context)

@login_required
def lab_banners_delete(request, id):
    if request.method == 'POST':
        try:
            lab_banner = get_object_or_404(adminModel.LabBanner, id=id)
            lab_banner.delete()
            messages.success(request, 'Lab banner deleted successfully!')
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
        

# Lab Staff
@login_required
def lab_staff_list(request):
    lab_staff = adminModel.LabStaff.objects.all()
    paginator = Paginator(lab_staff, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'lab_staff': page_obj,
    }
    return render(request, 'admin/lab/lab_staff_list.html', context)

@login_required
def lab_staff_create(request):
    if request.method == 'POST':
        lab_id = request.POST.get('laboratory_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        qualification = request.POST.get('qualification')
        experience = request.POST.get('experience')
        staff_type = request.POST.get('staff_type')
        profile_picture = request.FILES.get('profile_picture')
        status = request.POST.get('status')
        lab = get_object_or_404(adminModel.Laboratory, id=lab_id)
        lab_staff = adminModel.LabStaff( laboratory=lab, name=name, email=email, phone=contact_number,profile_img=profile_picture,qualification=qualification,experience=experience,staff_type=staff_type,status=status,)
        lab_staff.save()
        messages.success(request, 'Member Created Successfully!')
        return redirect('lab_staff_list')
    laboratories = adminModel.Laboratory.objects.all()
    context = {'laboratories': laboratories,}
    return render(request, 'admin/lab/lab_staff_create.html', context)

@login_required
def lab_staff_edit(request, id):
    lab_staff = get_object_or_404(adminModel.LabStaff, id=id)
    if request.method == 'POST':
        laboratory_id = request.POST.get('laboratory_id')
        lab = get_object_or_404(adminModel.Laboratory, id=laboratory_id)
        lab_staff.laboratory = lab
        lab_staff.name = request.POST.get('name')
        lab_staff.email = request.POST.get('email')
        lab_staff.phone = request.POST.get('contact_number')
        lab_staff.qualification = request.POST.get('qualification')
        lab_staff.experience = request.POST.get('experience')
        lab_staff.staff_type = request.POST.get('staff_type')
        lab_staff.status = request.POST.get('status')
        if request.FILES.get('profile_picture'):
            lab_staff.profile_img = request.FILES['profile_picture']
        lab_staff.save()
        messages.success(request, 'Lab staff details updated successfully!')
        return redirect('lab_staff_list') 
    laboratories = adminModel.Laboratory.objects.all()
    context = {'lab_staff': lab_staff,'laboratories': laboratories,}
    return render(request, 'admin/lab/lab_staff_edit.html', context)

@login_required
def lab_staff_delete(request, id):
    if request.method == 'POST':
        try:
            lab_staff = get_object_or_404(adminModel.LabStaff, id=id)
            lab_staff.delete()
            messages.success(request, 'Lab Staff deleted successfully!')
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

#Lab Package
@login_required
def lab_package_list(request):
    lab_packages = adminModel.LabPackage.objects.all()
    paginator = Paginator(lab_packages, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'lab_packages': page_obj,
    }
    return render(request, 'admin/lab/lab_package_list.html', context)

@login_required
def lab_package_create(request):
    if request.method == 'POST':
        lab_id = request.POST.get('lab_id')
        lab_specialization = request.POST.get('lab_specialization')
        package_name = request.POST.get('package_name')
        lab_service = request.POST.get('lab_service')
        test_preparation = request.POST.get('test_preparation')
        package_img = request.FILES.get('package_img')
        expected_delivery = request.POST.get('expected_delivery')
        lab_tag = request.POST.get('lab_tag')
        lab_price = request.POST.get('lab_price')
        sale_price = request.POST.get('sale_price')
        promote = request.POST.get('promote')
        status = request.POST.get('status')

        lab = get_object_or_404(adminModel.Laboratory, id=lab_id)
        lab_service_obj = get_object_or_404(adminModel.LabService, id=lab_service)
        lab_tag_obj = get_object_or_404(adminModel.LabTag, id=lab_tag)

        lab_package = adminModel.LabPackage(
            lab=lab,lab_specialization=lab_specialization,package_name=package_name,
            lab_service=lab_service_obj,test_preparation=test_preparation,
            package_img=package_img,expected_delivery=expected_delivery,
            lab_tag=lab_tag_obj,lab_price=lab_price,sale_price=sale_price,
            promote=promote,status=status,
        )
        lab_package.save()
        messages.success(request, 'Lab Package Created Successfully!')
        return redirect('lab_package_list')
    laboratories = adminModel.Laboratory.objects.all()
    lab_services = adminModel.LabService.objects.all()
    lab_tags = adminModel.LabTag.objects.all()
    context = {'laboratories': laboratories,'lab_services': lab_services,'lab_tags': lab_tags,}
    return render(request, 'admin/lab/lab_package_create.html', context)

@login_required
def lab_package_edit(request, id):
    lab_package = get_object_or_404(adminModel.LabPackage, id=id)

    if request.method == 'POST':
        lab_id = request.POST.get('lab_id')
        lab_specialization = request.POST.get('lab_specialization')
        package_name = request.POST.get('package_name')
        lab_service = request.POST.get('lab_service')
        test_preparation = request.POST.get('test_preparation')
        package_img = request.FILES.get('package_img')
        expected_delivery = request.POST.get('expected_delivery')
        lab_tag = request.POST.get('lab_tag')
        lab_price = request.POST.get('lab_price')
        sale_price = request.POST.get('sale_price')
        promote = request.POST.get('promote')
        status = request.POST.get('status')

        lab = get_object_or_404(adminModel.Laboratory, id=lab_id)
        lab_service = get_object_or_404(adminModel.LabService, id=lab_service)
        lab_tag = get_object_or_404(adminModel.LabTag, id=lab_tag)
        lab_package.lab = lab
        lab_package.lab_specialization = lab_specialization
        lab_package.package_name = package_name
        lab_package.lab_service = lab_service
        lab_package.test_preparation = test_preparation
        lab_package.expected_delivery = expected_delivery
        lab_package.lab_tag = lab_tag
        lab_package.lab_price = lab_price
        lab_package.sale_price = sale_price
        lab_package.promote = promote
        lab_package.status = status

        # Handle package image upload
        if request.FILES.get('package_img'):
            lab_package.package_img = request.FILES['package_img']

        lab_package.save()

        messages.success(request, 'Lab Package details updated successfully!')
        return redirect('lab_package_list')

    laboratories = adminModel.Laboratory.objects.all()
    lab_services = adminModel.LabService.objects.all()
    lab_tags = adminModel.LabTag.objects.all()
    context = {
        'lab_package': lab_package,
        'laboratories': laboratories,
        'lab_services':lab_services,
        'lab_tags':lab_tags,
    }
    return render(request, 'admin/lab/lab_package_edit.html', context)

@login_required
def lab_package_delete(request, id):
    if request.method == 'POST':
        try:
            lab_package = get_object_or_404(adminModel.LabPackage, id=id)
            lab_package.delete()
            messages.success(request, 'Lab Package deleted successfully!')
            return JsonResponse({'success': True, 'message': 'Deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

@login_required
def lab_orders_list(request):
    lab_orders = adminModel.LabOrders.objects.select_related('customer', 'lab').prefetch_related('lab_order_items').all()
    paginator = Paginator(lab_orders, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admin/lab/lab_orders_list.html', {'lab_orders': page_obj})

@login_required
def lab_orders_show(request, id):
    lab_order = get_object_or_404(adminModel.LabOrders, id=id)
    lab_order_items = lab_order.lab_order_items.all()
    context = {
        'lab_order': lab_order,
        'lab_order_items': lab_order_items,
    }
    return render(request, "admin/lab/lab_orders_show.html", context)

@login_required
def lab_orders_edit(request, id):
    lab_order = get_object_or_404(adminModel.LabOrders, id=id)
    lab_staffs = adminModel.LabStaff.objects.all()
    if request.method == 'POST':
        lab_staff_id = request.POST.get('lab_staff_id')
        status = request.POST.get('status')
        report = request.FILES.get('report')
        print(lab_staff_id)
        lab_staff = get_object_or_404(adminModel.LabStaff, id=lab_staff_id)
        lab_order.lab_staff = lab_staff
        lab_order.status = status
        if report:
            lab_order.report = report
        lab_order.save()
        messages.success(request, 'Lab Order updated successfully!')
        return redirect('lab_orders_list')
    context = {
        'lab_staffs':lab_staffs,
        'lab_order': lab_order,
    }
    return render(request, 'admin/lab/lab_order_edit.html', context)

@login_required
def lab_orders_delete(request, id):
    if request.method == 'POST':
        try:
            lab_order = get_object_or_404(adminModel.LabOrders, id=id)
            lab_order.delete()
            messages.success(request, 'Lab Order deleted successfully!')
            return JsonResponse({'success': True, 'message': 'Lab order deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})