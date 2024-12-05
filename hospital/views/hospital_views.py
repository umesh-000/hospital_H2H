from django.contrib.auth.hashers import make_password,check_password
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.conf import settings


# Create your views here.
def hospital_dashboard(request):
    return render(request,'hospital/hospital_deshboard.html')


# # bed booking 
# def bed_requests(request):
#     bed_list = models.BedBooking.objects.all()
#     context = {
#         "bed_list": bed_list,
#     }
#     return render(request, 'hospital/bed_booking_requests_list.html', context)

# @require_POST
# def update_booking_status(request):
#     data = json.loads(request.body)
#     booking_id = data.get('booking_id')
#     new_status = data.get('status')
#     try:
#         booking = models.BedBooking.objects.get(id=booking_id)
#         booking.status = new_status
#         booking.save()
#         return JsonResponse({'success': True, 'message': 'Status updated successfully.'})
#     except models.BedBooking.DoesNotExist:
#         return JsonResponse({'success': False, 'message': 'Booking not found.'})
#     except Exception as e:
#         return JsonResponse({'success': False, 'message': str(e)})


# # # Fee Setting
# # def hospital_fee_setting_list(request):
# #     fee_settings = models.HospitalFeeSettings.objects.all()
# #     context = {
# #         'fee_settings': fee_settings,
# #     }
# #     return render(request, 'hospital/hospital_fee_setting_list.html', context)

# # def hospital_fee_setting_list_create(request):
# #     if request.method == "GET":
# #         hospitals = models.Hospital.objects.all()
# #         fee_settings = models.HospitalFeeSettings.objects.all()
# #         context = {
# #             "hospitals": hospitals,
# #             "fee_settings": fee_settings,
# #         }
# #         return render(request, "hospital/hospital_fee_setting_create.html", context)
    
# #     if request.method == "POST":
# #         hospital_id = request.POST.get('hospital_id')
# #         appointment_fee = request.POST.get('appointment_fee')
# #         consultation_fee = request.POST.get('consultation_fee')
# #         waiting_time = request.POST.get('waiting_time')
# #         # Fetch the hospital object
# #         hospital = models.Hospital.objects.get(id=hospital_id)
# #         print(hospital_id)

# #         # Create a new HospitalFeeSetting object
# #         fee_setting = models.HospitalFeeSettings(
# #             hospital=hospital,
# #             appointment_fee=appointment_fee,
# #             consultation_fee=consultation_fee,
# #             waiting_time=waiting_time,
# #             created_at= datetime.datetime.now(),
# #             updated_at = datetime.datetime.now(),
# #         )
# #         print(fee_setting)
# #         fee_setting.save()
# #         messages.success(request, 'Hospital Fee Setting added successfully!')
# #         return redirect('/admin/hospital/fee_settings/')







# # Insurances
# def insurances_list(request):
#     insurances = models.Insurance.objects.all()
#     context = {
#         "insurances":insurances,
#     }
#     return render(request,"hospital/insurances_list.html",context)

# def insurance_create(request):
#     if request.method == "GET":
#         return render(request, "hospital/insurance_create.html")
    
#     if request.method == "POST":
#         # Insurance details
#         insurance_name = request.POST.get('insurance_name')
#         insurance_link = request.POST.get('insurance_link')
#         status = request.POST.get('status')

#         # File handling
#         insurance_logo = request.FILES.get('insurance_logo')
#         if not insurance_logo:
#             default_image_path = os.path.join(settings.STATIC_ROOT, 'images', 'default_image.png')
#             with open(default_image_path, 'rb') as f:
#                 insurance_logo = default_storage.save('insurance_logos/default_image.png', ContentFile(f.read()))
        
        
        
#         # Create Insurance instance
#         insurance = models.Insurance(
#             insurance_name=insurance_name,
#             insurance_logo=insurance_logo,
#             insurance_link=insurance_link,
#             status=status,
#             created_at=datetime.datetime.now(),
#             updated_at=datetime.datetime.now(),
#         )
#         insurance.save()
#         messages.success(request, 'Added Successfully!')
#         return redirect('insurances_list')

# def insurance_edit(request, id):
#     insurance = get_object_or_404(models.Insurance, id=id)
#     if request.method == 'GET':
#         context = {
#             'insurance': insurance,
#         }
#         return render(request, "hospital/insurance_edit.html", context)
    
#     if request.method == 'POST':
#         insurance_name = request.POST.get('insurance_name')
#         insurance_link = request.POST.get('insurance_link')
#         status = request.POST.get('status')
#         insurance_logo = request.FILES.get('insurance_logo')

#         # Handling the default image fallback
#         if not insurance_logo:
#             if insurance.insurance_logo:
#                 insurance_logo = insurance.insurance_logo
#             else:
#                 default_image_path = os.path.join(settings.STATIC_ROOT, 'images', 'default_image.png')
#                 with open(default_image_path, 'rb') as f:
#                     insurance_logo = default_storage.save('insurance_logos/default_image.png', f)

#         # Update the fields
#         insurance.insurance_name = insurance_name
#         insurance.insurance_link = insurance_link
#         insurance.status = status
#         insurance.insurance_logo = insurance_logo

#         # Save the updated insurance
#         insurance.save()

#         # Success message
#         messages.success(request, 'Details Dpdated successfully!')

#         return redirect('insurances_list')

# def insurance_delete(request, id):
#     insurance = get_object_or_404(models.Insurance, id=id)
#     insurance.delete()
#     messages.success(request, 'Deleted successfully!')
#     return redirect('insurances_list')


# # Hospital Insurances
# def hospital_insurance_list(request):
#     hospital_insurances = models.HospitalInsurance.objects.all()
#     context = {
#         "hospital_insurances": hospital_insurances,
#     }
#     return render(request, "hospital/hospital_insurance_list.html", context)

# def hospital_insurance_create(request):
#     if request.method == "GET":
#         hospitals = models.Hospital.objects.all()
#         insurances = models.Insurance.objects.all()
#         context = {
#             "hospitals":hospitals,
#             "insurances":insurances,
#         }
#         return render(request, "hospital/hospital_insurance_create.html",context)
#     if request.method == "POST":
#         hospital_id = request.POST.get('hospital')
#         insurance_id = request.POST.get('insurance')
#         status = request.POST.get('status')
        
#         if hospital_id and insurance_id:
#             try:
#                 hospital = models.Hospital.objects.get(id=hospital_id)
#                 insurance = models.Insurance.objects.get(id=insurance_id)
#                 models.HospitalInsurance.objects.create(
#                     hospital=hospital,
#                     insurance=insurance,
#                     status=status
#                 )
#                 messages.success(request, 'Added Successfully!')
#                 return redirect('hospital_insurance_list')  # Redirect to the list page or another view
#             except models.Hospital.DoesNotExist:
#                 return HttpResponse("Hospital not found.", status=404)
#             except models.Insurance.DoesNotExist:
#                 return HttpResponse("Insurance not found.", status=404)
        
#         return HttpResponse("Invalid data submitted.", status=400)

# def hospital_insurance_edit(request, id):
#     hospital_insurance = get_object_or_404(models.HospitalInsurance, id=id)
#     hospitals = models.Hospital.objects.all()
#     insurances = models.Insurance.objects.all()
#     if request.method == 'GET':
#         context = {
#             'hospital_insurance': hospital_insurance,
#             "hospitals":hospitals,
#             "insurances":insurances,
#         }
#         return render(request, "hospital/hospital_insurance_edit.html", context)
    
#     if request.method == "POST":
#         hospital_id = request.POST.get("hospital")
#         insurance_id = request.POST.get("insurance")
#         status = request.POST.get("status")

#         # Updating the hospital insurance record
#         hospital_insurance.hospital_id = hospital_id
#         hospital_insurance.insurance_id = insurance_id
#         hospital_insurance.status = status
#         hospital_insurance.save()
#         messages.success(request, 'Updated successfully!')
#         return redirect("hospital_insurance_list")


# def hospital_insurance_delete(request, id):
#     hospital_insurance = get_object_or_404(models.HospitalInsurance, id=id)
#     hospital_insurance.delete()
#     messages.success(request, 'Deleted successfully!')
#     return redirect('hospital_insurance_list')