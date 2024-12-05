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

# def doctor_documents(request):
#     doctor_doc_list = models.DoctorDetails.objects.all()
#     context = {
#         'doctor_doc_list': doctor_doc_list,
#     }
#     return render(request, "doctor/doctor_doc_list.html", context)

# def change_doc_status(request):
#     if request.method == 'POST':
#         doctor_id = request.POST.get('doctor_id')
#         status = request.POST.get('status')

#         try:
#             doctor = models.DoctorDetails.objects.get(id=doctor_id)
#             doctor.document_approve_status = status
#             doctor.save()
#             return JsonResponse({'success': True})
#         except models.DoctorDetails.DoesNotExist:
#             return JsonResponse({'success': False, 'error': 'Doctor not found'})
    
#     return JsonResponse({'success': False, 'error': 'Invalid request'})


# # Doctor booking list view
# def doctor_booking_requests(request):
#     doctor_booking_list = models.DoctorBooking.objects.all()
#     context = {
#         "doctor_booking_list": doctor_booking_list,
#     }
#     return render(request, 'doctor/doctor_booking_requests_list.html', context)


# @require_POST
# def update_doctor_booking_status(request):
#     data = json.loads(request.body)
#     booking_id = data.get('booking_id')
#     new_status = data.get('status')
#     try:
#         booking = models.DoctorBooking.objects.get(id=booking_id)
#         booking.status = new_status
#         booking.save()
#         return JsonResponse({'success': True, 'message': 'Status updated successfully.'})
#     except models.DoctorBooking.DoesNotExist:
#         return JsonResponse({'success': False, 'message': 'Booking not found.'})
#     except Exception as e:
#         return JsonResponse({'success': False, 'message': str(e)})