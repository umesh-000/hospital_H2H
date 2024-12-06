from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.core.files.storage import default_storage
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.core.files.base import ContentFile
from accounts import models as account_module
from H2H_admin import models as adminModel
from django.contrib import messages
from django.db import transaction
from django.conf import settings
from H2H_admin import utils
import traceback
import logging
import json
import os


logger = logging.getLogger(__name__)

# Hospital
@login_required
def customers_list(request):
    customers = account_module.Customer.objects.select_related('user').all()
    return render(request,"admin/customers/customers_list.html",{"customers_list":customers})

@login_required
def customers_edit(request, id):
    customer = get_object_or_404(account_module.Customer, id=id)
    if request.method == 'POST':
        try:
            customer_name = request.POST.get('name')
            email = request.POST.get('email')
            contact_number = request.POST.get('contact_number')
            status = request.POST.get('status')


            customer.customer_name = customer_name
            customer.user.email = email
            customer.phone_number = contact_number
            if request.FILES.get('profile_picture'):
                customer.profile_picture = request.FILES['profile_picture']
            customer.status = int(status)
            customer.save()
            customer.user.save()
            messages.success(request, 'Customer updated successfully!')
            return redirect('customers_list') 
        except Exception as e:
            messages.error(request, f"Error updating customer: {str(e)}")
            return redirect('customers_edit', id=id) 
    return render(request, 'admin/customers/customer_edit.html', {'customer': customer})


@login_required
def customers_show(request, id):
    customer = get_object_or_404(account_module.Customer, id=id)
    return render(request, 'admin/customers/customer_show.html', {'customer': customer})

@login_required
def customers_delete(request, id):
    if request.method == 'POST':
        try:
            customer = get_object_or_404(account_module.Customer, id=id)
            user = customer.user
            user.delete() 
            customer.delete()
            messages.success(request, 'Customer deleted successfully!')
            return JsonResponse({'success': True, 'message': 'Customer and associated user deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f"Error: {str(e)}"})
    return JsonResponse({'success': False, 'message': 'Invalid request method. Use POST.'})

@login_required
def help_desk_query(request):
    queries = adminModel.HelpDeskQuery.objects.all()
    return render(request, "admin/customers/help_desk_query_list.html", {"queries": queries})


@login_required
def help_desk_query_edit(request, id):
    query = get_object_or_404(adminModel.HelpDeskQuery, id=id)
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            query.name = name
            query.email = email
            query.message = message
            query.save()

            messages.success(request, 'Query updated successfully!')
            return redirect('help_desk_query_list')
        except Exception as e:
            messages.error(request, f"Error updating query: {str(e)}")
            return redirect('help_desk_query_edit', id=id)

    return render(request, 'admin/customers/help_desk_query_edit.html', {'query': query})


@login_required
def help_desk_query_show(request, id):
    query = get_object_or_404(adminModel.HelpDeskQuery, id=id)
    return render(request, 'admin/customers/help_desk_query_show.html', {'query': query})


@login_required
def help_desk_query_delete(request, id):
    if request.method == 'POST':
        try:
            query = get_object_or_404(adminModel.HelpDeskQuery, id=id)
            query.delete()
            messages.success(request, 'Query deleted successfully!')
            return JsonResponse({'success': True, 'message': 'Query deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f"Error: {str(e)}"})
    return JsonResponse({'success': False, 'message': 'Invalid request method. Use POST.'})

@login_required
def feedbacks(request):
    feedbacks = adminModel.Feedback.objects.all()
    return render(request, "admin/customers/feedbacks_list.html", {"feedbacks": feedbacks})

@login_required
def feedbacks_edit(request,id):
    feedback = get_object_or_404(adminModel.Feedback, id=id)
    customers = account_module.Customer.objects.all()
    labs = account_module.Laboratory.objects.all()
    doctors = account_module.DoctorDetails.objects.all()
    hospitals = account_module.Hospital.objects.all()
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            feedback.name = name
            feedback.email = email
            feedback.message = message
            feedback.save()

            messages.success(request, 'Feedback updated successfully!')
            return redirect('help_desk_query_list')
        except Exception as e:
            messages.error(request, f"Error updating query: {str(e)}")
            return redirect('help_desk_query_edit', id=id)
    context = {
        'labs': labs,
        'doctors': doctors,
        'feedback': feedback,
        'hospitals': hospitals,
        'customers': customers,
        }
        
    return render(request, 'admin/customers/feedback_edit.html',context)

@login_required
def feedbacks_show(request,id):
    feedback = get_object_or_404(adminModel.Feedback, id=id)
    return render(request, 'admin/customers/feedbacks_show.html', {'feedback': feedback})

@login_required
def feedbacks_delete(request,id):
    if request.method == 'POST':
        try:
            query = get_object_or_404(adminModel.Feedback, id=id)
            query.delete()
            messages.success(request, 'Feedback deleted successfully!')
            return JsonResponse({'success': True, 'message': 'Feedback deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f"Error: {str(e)}"})
    return JsonResponse({'success': False, 'message': 'Invalid request method. Use POST.'})
