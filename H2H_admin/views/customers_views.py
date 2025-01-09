from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from H2H_admin import models as adminModel
from django.http import JsonResponse
from django.contrib import messages
import logging
import json


logger = logging.getLogger(__name__)

# Hospital
@login_required
def customers_list(request):
    customers = adminModel.Customer.objects.select_related('user').all()
    paginator = Paginator(customers, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"admin/customers/customers_list.html",{"customers_list":page_obj})

@login_required
def customers_edit(request, id):
    customer = get_object_or_404(adminModel.Customer, id=id)
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
    customer = get_object_or_404(adminModel.Customer, id=id)
    return render(request, 'admin/customers/customer_show.html', {'customer': customer})

@login_required
def customers_delete(request, id):
    if request.method == 'POST':
        try:
            customer = get_object_or_404(adminModel.Customer, id=id)
            user = customer.user
            user.delete() 
            customer.delete()
            messages.success(request, 'Customer deleted successfully!')
            return JsonResponse({'success': True, 'message': 'Customer and associated user deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f"Error: {str(e)}"})
    return JsonResponse({'success': False, 'message': 'Invalid request method. Use POST.'})


@login_required
def customer_wallet_histories_list(request):
    customer_wallet_histories = adminModel.CustomerWalletHistory.objects.all().order_by('-id')
    paginator = Paginator(customer_wallet_histories, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "admin/customers/customer_wallet_histories.html", {"customer_wallet_histories": page_obj})

@login_required
def customer_wallet_histories_create(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer')
        message = request.POST.get('message')
        transaction_type = request.POST.get('transaction_type')
        transaction_type_choices = request.POST.get('transaction_type_choices')
        amount = request.POST.get('amount')

        customer = get_object_or_404(adminModel.Customer, id=customer_id)
        adminModel.CustomerWalletHistory.objects.create(customer=customer,message=message,transaction_type=transaction_type,transaction_type_choices=transaction_type_choices,amount=amount,)
        messages.success(request, 'Wallet History created successfully!')
        return redirect('customer_wallet_histories_list')

    # On GET request, render the form
    customers = adminModel.Customer.objects.all()
    context = {
        'customers': customers,
        'type_choices': adminModel.CustomerWalletHistory._meta.get_field('transaction_type').choices,
        'transaction_type_choices': adminModel.CustomerWalletHistory._meta.get_field('transaction_type_choices').choices,
    }
    return render(request, 'admin/customers/customer_wallet_histories_create.html', context)

@login_required
def help_desk_query(request):
    queries = adminModel.HelpDeskQuery.objects.all()
    paginator = Paginator(queries, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "admin/customers/help_desk_query_list.html", {"queries": page_obj})


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
    paginator = Paginator(feedbacks, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "admin/customers/feedbacks_list.html", {"feedbacks": page_obj})

@login_required
def feedbacks_edit(request, id):
    feedback = get_object_or_404(adminModel.Feedback, id=id)
    customers = adminModel.Customer.objects.all()
    labs = adminModel.Laboratory.objects.all()
    doctors = adminModel.DoctorDetails.objects.all()
    hospitals = adminModel.Hospital.objects.all()
    if request.method == 'POST':
        try:
            customer_id = request.POST.get('customer_id')
            doctor_id = request.POST.get('doctor_id')
            hospital_id = request.POST.get('hospital_id')
            lab_id = request.POST.get('lab_id')
            feedback_text = request.POST.get('feedback')
            rating = request.POST.get('rating')
            if not customer_id:
                messages.error(request, "Customer must be selected.")
                return redirect('feedbacks_edit', id=id)
            customer = get_object_or_404(adminModel.Customer, id=customer_id)
            entities = [doctor_id, hospital_id, lab_id]
            selected_entities = [entity for entity in entities if entity]
            if len(selected_entities) > 1:
                messages.error(request,"Only one of Doctor, Hospital, or Lab can be selected at a time.")
                return redirect('feedbacks_edit', id=id)
            elif len(selected_entities) == 0:
                messages.error(request,"Please select either a Doctor, Hospital, or Lab.")
                return redirect('feedbacks_edit', id=id)
            if not rating:
                messages.error(request, "Rating is required.")
                return redirect('feedbacks_edit', id=id)
            try:
                rating_value = float(rating)
                if rating_value < 1 or rating_value > 5:
                    messages.error(request,"Rating must be a value between 1 and 5.")
                    return redirect('feedbacks_edit', id=id)
            except ValueError:
                messages.error(request, "Rating must be a number.")
                return redirect('feedbacks_edit', id=id)

            feedback.customer = customer
            feedback.doctor = adminModel.DoctorDetails.objects.filter(id=doctor_id).first() if doctor_id else None
            feedback.hospital = adminModel.Hospital.objects.filter(id=hospital_id).first() if hospital_id else None
            feedback.lab = adminModel.Laboratory.objects.filter(id=lab_id).first() if lab_id else None
            feedback.feedback = feedback_text
            feedback.rating = rating_value
            feedback.save()
            messages.success(request, "Feedback updated successfully!")
            return redirect('feedbacks_edit', id=id)
        except Exception as e:
            messages.error(request, f"Error updating feedback: {str(e)}")
            return redirect('feedbacks_edit', id=id)
    context = {
        'labs': labs, 'doctors': doctors, 'feedback': feedback,
        'hospitals': hospitals, 'customers': customers,
    }
    return render(request, 'admin/customers/feedback_edit.html', context)


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


@csrf_exempt
def update_approval_status(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            feedback_id = data.get('feedbackId')
            is_approved = data.get('is_approved')
            if feedback_id is None or is_approved is None:
                return JsonResponse({'success': False, 'message': 'Invalid data provided.'}, status=400)
            feedback = adminModel.Feedback.objects.get(id=feedback_id)
            feedback.admin_approved = is_approved
            feedback.save()
            return JsonResponse({'success': True, 'message': 'Status updated successfully.'})
        except adminModel.Feedback.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Feedback not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=400)