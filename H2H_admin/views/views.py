from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
import accounts.models as accountModels
import H2H_admin.models as admin_models
from django.contrib import messages
from django.http import JsonResponse
import datetime
import json


@login_required
def admin_dashboard(request):
    doctors_count = accountModels.DoctorDetails.objects.count()
    customers_count = accountModels.Customer.objects.count()
    labs_count = accountModels.Laboratory.objects.count()
    hospitals_count = accountModels.Hospital.objects.count()
    total_users = accountModels.User.objects.exclude(user_type='admin').count()
    lab_orders = admin_models.LabOrders.objects.select_related('customer', 'lab').prefetch_related('lab_order_items').all()
    lab_orders_count = lab_orders.count()
    context = {
        "doctors_count":doctors_count,
        "customers_count":customers_count,
        "hospitals_count":hospitals_count,
        "labs_count":labs_count,
        'lab_orders_count':lab_orders_count,
        "total_users":total_users,
    }
    return render(request, "admin/deshboard.html",context)


@login_required
def banners_list(request):
    if request.method == "GET":
        banners = admin_models.Banner.objects.all()
        paginator = Paginator(banners, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {"banners": page_obj,}
        return render(request, "admin/banners/banners_list.html", context)

@login_required
def banner_create(request):
    if request.method == "GET":
        app_modules = admin_models.AppModule.objects.all()
        context = {
            "app_modules": app_modules,
            'POSITION_CHOICES': admin_models.Banner.POSITION_CHOICES,
            "status_choices": admin_models.STATUS_CHOICES,
            }
        return render(request, "admin/banners/banner_create.html", context)

    if request.method == "POST":
        app_module_id = request.POST.get('app_module')
        banner_image = request.FILES.get('banner') 
        link = request.POST.get('link')
        position = request.POST.get('position')
        status = request.POST.get('status')

        try:
            app_module = get_object_or_404(admin_models.AppModule, id=app_module_id)
            banner = admin_models.Banner(app_module=app_module,banner=banner_image,link=link,position=position,status=status)
            messages.success(request, 'Banner created successfully!')
            banner.save()
            return redirect('banners_list')  # Redirect to banners list after successful creation

        except admin_models.AppModule.DoesNotExist:
            messages.error(request, f'App Module not found')

@login_required
def banner_edit(request, id):
    banner = get_object_or_404(admin_models.Banner, id=id)
    app_modules = admin_models.AppModule.objects.all()

    if request.method == "GET":
        context = {
            "banner": banner,
            "app_modules": app_modules,
            'POSITION_CHOICES': admin_models.Banner.POSITION_CHOICES,
            "status_choices": admin_models.STATUS_CHOICES,
            }
        return render(request, "admin/banners/banner_edit.html", context)

    if request.method == "POST":
        app_module_id = request.POST.get('app_module')
        banner_image = request.FILES.get('banner') 
        link = request.POST.get('link')
        position = request.POST.get('position')
        status = request.POST.get('status')

        app_module = get_object_or_404(admin_models.AppModule, id=app_module_id)

        if banner_image:
            banner.banner = banner_image


        banner.app_module = app_module
        banner.link = link
        banner.position = position
        banner.status = int(status)
        banner.save()
        messages.success(request, 'Banner updated successfully!')
        return redirect('banners_list')

@login_required
def banner_delete(request, id):
    if request.method == 'POST':
        try:
            banner = get_object_or_404(admin_models.Banner, id=id)
            banner.delete()
            messages.success(request, 'Banner deleted successfully!')
            return JsonResponse({'success': True, 'message': 'Banner deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


@login_required
def blogs_list(request):
    if request.method == "GET":
        blogs_list = admin_models.Blog.objects.all()
        paginator = Paginator(blogs_list, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {"blogs": page_obj,}
        return render(request, "admin/blogs_list.html", context)

@login_required
def blogs_create(request):

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        video = request.POST.get("video")
        status = request.POST.get("status")


        # Create a new Blog object and save it
        blog = admin_models.Blog(
            title=title,
            description=description,
            image=image,
            video=video,
            status=status,
        )
        blog.save()

        messages.success(request, "Blog created successfully!")
        return redirect("blogs_list")
    return render(request, "admin/blog_create.html")


@login_required
def blogs_edit(request, id):
    blog = get_object_or_404(admin_models.Blog, id=id)
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        video = request.POST.get("video")
        status = request.POST.get("status")
        blog.title = title
        blog.description = description
        if image:
            blog.image = image
        blog.video = video
        blog.status = status
        blog.save()
        messages.success(request, "Blog updated successfully!")
        return redirect("blogs_list")
    return render(request, "admin/blog_edit.html", {"blog": blog})


@login_required
def blogs_delete(request, id):
    if request.method == 'POST':
        try:
            blog = get_object_or_404(admin_models.Blog, id=id)
            blog.delete()
            messages.success(request, 'Blog deleted successfully!')
            return JsonResponse({'success': True, 'message': 'Blog deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

@login_required
def module_offer_banners(request):
    if request.method == "GET":
        banners = admin_models.ModuleOfferBanner.objects.all()
        paginator = Paginator(banners, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {"banners": page_obj}
        return render(request, "admin/banners/module_offer_banners_list.html", context)

@login_required
def module_offer_banners_create(request):
    if request.method == "GET":
        app_modules = admin_models.AppModule.objects.all()
        context = {
            "app_modules": app_modules,
            "status_choices": admin_models.STATUS_CHOICES,
        }
        return render(request, "admin/banners/module_offer_banner_create.html", context)

    if request.method == "POST":
        app_module_id = request.POST.get('app_module')
        banner_image = request.FILES.get('banner')
        link = request.POST.get('link')
        status = request.POST.get('status')

        try:
            app_module = get_object_or_404(admin_models.AppModule, id=app_module_id)
            banner = admin_models.ModuleOfferBanner(app_module=app_module,banner=banner_image,link=link,status=status,)
            banner.save()
            messages.success(request, 'Offer Banner created successfully!')
            return redirect('module_offer_banners_list')
        except admin_models.AppModule.DoesNotExist:
            messages.error(request, 'App Module not found')
            return redirect('module_offer_banner_create')

@login_required
def module_offer_banners_edit(request, id):
    banner = get_object_or_404(admin_models.ModuleOfferBanner, id=id)
    app_modules = admin_models.AppModule.objects.all()

    if request.method == "GET":
        context = {
            "banner": banner,
            "app_modules": app_modules,
            "status_choices": admin_models.STATUS_CHOICES,
        }
        return render(request, "admin/banners/module_offer_banner_edit.html", context)

    if request.method == "POST":
        app_module_id = request.POST.get('app_module')
        banner_image = request.FILES.get('banner')
        link = request.POST.get('link')
        status = request.POST.get('status')

        app_module = get_object_or_404(admin_models.AppModule, id=app_module_id)

        if banner_image:
            banner.banner = banner_image

        banner.app_module = app_module
        banner.link = link
        banner.status = int(status)
        banner.save()
        messages.success(request, 'Offer Banner updated successfully!')
        return redirect('module_offer_banners_list')

@login_required
def module_offer_banners_delete(request, id):
    if request.method == 'POST':
        try:
            banner = get_object_or_404(admin_models.ModuleOfferBanner, id=id)
            banner.delete()
            messages.success(request, 'Offer Banner deleted successfully!')
            return JsonResponse({'success': True, 'message': 'Offer Banner deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

@login_required
def fcm_notifications(request):
    if request.method == "GET":
        fcm_notifications = admin_models.FcmNotification.objects.all()
        paginator = Paginator(fcm_notifications, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {"fcm_notifications": page_obj}
        return render(request, "admin/fcm_notifications_list.html", context)
    
@login_required
def fcm_notifications_create(request):
    if request.method == "POST":
        slug = request.POST.get('slug')
        customer_title = request.POST.get('customer_title')
        customer_description = request.POST.get('customer_description')
        try:
            if admin_models.FcmNotification.objects.filter(slug=slug).exists():
                messages.error(request, 'A notification with this slug already exists.')
                return redirect('fcm_notifications_create')
            notification = admin_models.FcmNotification(slug=slug,customer_title=customer_title,customer_description=customer_description)
            notification.save()
            messages.success(request, 'FCM created successfully!')
            return redirect('fcm_notifications_list')
        except Exception as e:
            messages.error(request, f'Error occurred: {str(e)}')
            return redirect('fcm_notifications_create')
    return render(request, "admin/fcm_notification_create.html")

@login_required
def fcm_notifications_edit(request, id):
    fcm_notification = get_object_or_404(admin_models.FcmNotification, id=id)
    if request.method == "POST":
        slug = request.POST.get('slug')
        customer_title = request.POST.get('customer_title')
        customer_description = request.POST.get('customer_description')
        if admin_models.FcmNotification.objects.filter(slug=slug).exclude(id=id).exists():
            messages.error(request, 'A notification with this slug already exists.')
            return redirect('fcm_notifications_edit', id=id)
        try:
            fcm_notification.slug = slug
            fcm_notification.customer_title = customer_title
            fcm_notification.customer_description = customer_description
            fcm_notification.save()
            messages.success(request, 'FCM Notification updated successfully!')
            return redirect('fcm_notifications_list')
        except Exception as e:
            messages.error(request, f'Error occurred: {str(e)}')
            return redirect('fcm_notifications_edit', id=id)
    context = {'fcm_notification': fcm_notification,}
    return render(request, "admin/fcm_notification_edit.html", context)


# List all expert talks
@login_required
def expert_talks_list(request):
    if request.method == "GET":
        expert_talks = admin_models.ExpertTalk.objects.select_related('doctor').all()
        paginator = Paginator(expert_talks, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {"expert_talks": page_obj}
        return render(request, "admin/expert_talks_list.html", context)

# Create a new expert talk
@login_required
def expert_talks_create(request):
    if request.method == "GET":
        doctors = accountModels.DoctorDetails.objects.all()

    if request.method == "POST":
        doctor_id = request.POST.get('doctor')
        comment = request.POST.get('comment')

        try:
            doctor = get_object_or_404(accountModels.DoctorDetails, id=doctor_id)
            expert_talk = admin_models.ExpertTalk(doctor=doctor, comment=comment)
            expert_talk.save()
            messages.success(request, 'Expert Talk created successfully!')
            return redirect('expert_talks_list')
        except accountModels.DoctorDetails.DoesNotExist:
            messages.error(request, 'Doctor not found')
            return redirect('expert_talks_create')
    
    context = {"doctors": doctors}
    return render(request, "admin/expert_talks_create.html", context)

# Edit an existing expert talk
@login_required
def expert_talks_edit(request, id):
    expert_talk = get_object_or_404(admin_models.ExpertTalk, id=id)
    doctors = accountModels.DoctorDetails.objects.all()


    if request.method == "POST":
        doctor_id = request.POST.get('doctor')
        comment = request.POST.get('comment')

        try:
            doctor = get_object_or_404(accountModels.DoctorDetails, id=doctor_id)
            expert_talk.doctor = doctor
            expert_talk.comment = comment
            expert_talk.save()
            messages.success(request, 'Expert Talk updated successfully!')
            return redirect('expert_talks_list')
        except accountModels.DoctorDetails.DoesNotExist:
            messages.error(request, 'Doctor not found')
            return redirect('expert_talks_edit', id=id)

    context = {
        "expert_talk": expert_talk,
        "doctors": doctors,
    }
    return render(request, "admin/expert_talks_edit.html", context)
# Delete an expert talk
@login_required
def expert_talks_delete(request, id):
    if request.method == 'POST':
        try:
            expert_talk = get_object_or_404(admin_models.ExpertTalk, id=id)
            expert_talk.delete()
            messages.success(request, 'Expert Talk deleted successfully!')
            return JsonResponse({'success': True, 'message': 'Expert Talk deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


@login_required
def users(request):
    # Retrieve and annotate users with their types
    all_users = []

    # Add Admin users
    admins = accountModels.Admin.objects.select_related('user').all()
    for admin in admins:
        all_users.append({
            "user_id": admin.user.id,
            "username": admin.user.username,
            "created_at": admin.user.created_at,
            "updated_at": admin.user.updated_at,
            "type": admin.user.user_type
        })

    # Add Customer users
    customers = accountModels.Customer.objects.select_related('user').all()
    for customer in customers:
        all_users.append({
            "user_id": customer.user.id,
            "username": customer.user.username,
            "created_at": customer.user.created_at,
            "updated_at": customer.user.updated_at,
            "type": customer.user.user_type
        })

    # Add Hospital users
    hospitals = accountModels.Hospital.objects.select_related('user').all()
    for hospital in hospitals:
        all_users.append({
            "user_id": hospital.user.id,
            "username": hospital.user.username,
            "created_at": hospital.user.created_at,
            "updated_at": hospital.user.updated_at,
            "type": hospital.user.user_type
        })

    # Add Laboratory users
    labs = accountModels.Laboratory.objects.select_related('user').all()
    for lab in labs:
        all_users.append({
            "user_id": lab.user.id,
            "username": lab.user.username,
            "created_at": lab.user.created_at,
            "updated_at": lab.user.updated_at,            
            "type": "Lab"
        })

    # Add Doctor users
    doctors = accountModels.DoctorDetails.objects.select_related('user').all()
    for doctor in doctors:
        all_users.append({
            "user_id": doctor.user.id,
            "username": doctor.user.username,
            "created_at": doctor.user.created_at,
            "updated_at": doctor.user.updated_at,
            "type": doctor.user.user_type
        })
    # print(json.dumps(list(all_users), indent=4))
    all_users = sorted(all_users, key=lambda x: x['user_id'])
    paginator = Paginator(all_users, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "all_users": page_obj,
    }
    return render(request, "admin/users.html", context)

@login_required
def show_user(request, id):
    user = get_object_or_404(accountModels.User, id=id)
    return render(request, 'admin/user_show.html', {'user': user})

@login_required
def edit_user(request, id):
    user = get_object_or_404(accountModels.User, id=id)
    if request.method=="GET":
        return render(request, 'admin/user_edit.html', {'user': user})
    if request.method=="POST":
        username = request.POST.get('username')
        modified_at = datetime.datetime.now()
        user.username = username
        user.modified_at = modified_at
        user.save()
        return redirect('/admin/users/')

@login_required
def delete_user(request, id):
    if request.method == 'POST':
        try:
            user = get_object_or_404(accountModels.User, id=id)
            user.delete()
            messages.success(request, 'Expert Talk deleted successfully!')
            return JsonResponse({'success': True, 'message': 'Expert Talk deleted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


@login_required
def admin_profile(request, id):
    admin_instance = get_object_or_404(accountModels.Admin, user_id=id)

    if request.method=="POST":
        pass


    context = {
        "profile" : admin_instance
    }
    return render(request, "admin/admin_profile.html", context)

@login_required
def admin_profile(request, id):
    admin_instance = get_object_or_404(accountModels.Admin, user_id=id)
    if request.method == "POST":
        profile_image = request.FILES.get('profile_image')
        if profile_image:
            admin_instance.profile_image = profile_image
            admin_instance.save()
            messages.success(request, "Profile image updated successfully!")
        else:
            messages.error(request, "Please select a valid image.")

    context = {
        "profile": admin_instance,
    }
    return render(request, "admin/admin_profile.html", context)

@login_required
def admin_change_password(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    admin_profile = get_object_or_404(accountModels.Admin, id=id)
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        user = admin_profile.user
        if not check_password(current_password, user.password):
            messages.error(request, 'Current password is incorrect.')
            return redirect('admin_profile', id=id)
        if new_password != confirm_password:
            messages.error(request, 'New password and confirmation do not match.')
            return redirect('admin_profile', id=id)
        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)
        messages.success(request, 'Password updated successfully.')
        return redirect('admin_profile', id=id)
    context = {
        "profile": admin_profile,
    }
    return render(request, 'admin/admin_profile.html', context)

@login_required
def hospital_profile(request, id):
    admin_instance = get_object_or_404(accountModels.Hospital, user_id=id)
    if request.method == "POST":
        profile_image = request.FILES.get('profile_image')
        if profile_image:
            admin_instance.hospital_logo = profile_image
            admin_instance.save()
            messages.success(request, "Profile image updated successfully!")
        else:
            messages.error(request, "Please select a valid image.")

    context = {
        "profile": admin_instance,
    }
    return render(request, 'hospital/hospital_profile.html', context)


@login_required
def hospital_change_password(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    admin_profile = get_object_or_404(accountModels.Hospital, user_id=id)
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        user = admin_profile.user
        if not check_password(current_password, user.password):
            messages.error(request, 'Current password is incorrect.')
            return redirect('hospital_profile', id=id)
        if new_password != confirm_password:
            messages.error(request, 'New password and confirmation do not match.')
            return redirect('hospital_profile', id=id)
        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)
        messages.success(request, 'Password updated successfully.')
        return redirect('hospital_profile', id=id)
    context = {
        "profile": admin_profile,
    }
    return render(request, 'hospital/hospital_profile.html', context)

@login_required
def doctor_profile(request, id):
    admin_instance = get_object_or_404(accountModels.DoctorDetails, user_id=id)
    if request.method == "POST":
        profile_image = request.FILES.get('profile_image')
        if profile_image:
            admin_instance.profile_img = profile_image
            admin_instance.save()
            messages.success(request, "Profile image updated successfully!")
        else:
            messages.error(request, "Please select a valid image.")

    context = {
        "profile": admin_instance,
    }
    return render(request, 'doctor/doctor_profile.html', context)


@login_required
def doctor_change_password(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    admin_profile = get_object_or_404(accountModels.DoctorDetails, user_id=id)
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        user = admin_profile.user
        if not check_password(current_password, user.password):
            messages.error(request, 'Current password is incorrect.')
            return redirect('doctor_profile', id=id)
        if new_password != confirm_password:
            messages.error(request, 'New password and confirmation do not match.')
            return redirect('doctor_profile', id=id)
        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)
        messages.success(request, 'Password updated successfully.')
        return redirect('doctor_profile', id=id)
    context = {
        "profile": admin_profile,
    }
    return render(request, 'doctor/doctor_profile.html', context)


@login_required
def lab_profile(request, id):
    admin_instance = get_object_or_404(accountModels.Laboratory, user_id=id)
    if request.method == "POST":
        profile_image = request.FILES.get('profile_image')
        if profile_image:
            admin_instance.lab_image = profile_image
            admin_instance.save()
            messages.success(request, "Profile image updated successfully!")
        else:
            messages.error(request, "Please select a valid image.")

    context = {
        "profile": admin_instance,
    }
    return render(request, 'lab/lab_profile.html',context)


@login_required
def lab_change_password(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    admin_profile = get_object_or_404(accountModels.Laboratory, user_id=id)
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        user = admin_profile.user
        if not check_password(current_password, user.password):
            messages.error(request, 'Current password is incorrect.')
            return redirect('lab_profile', id=id)
        if new_password != confirm_password:
            messages.error(request, 'New password and confirmation do not match.')
            return redirect('lab_profile', id=id)
        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)
        messages.success(request, 'Password updated successfully.')
        return redirect('lab_profile', id=id)
    context = {
        "profile": admin_profile,
    }
    return render(request, 'lab/lab_profile.html', context)