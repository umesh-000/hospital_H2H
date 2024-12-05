from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
import accounts.models as accountModels
import H2H_admin.models as admin_models
from django.contrib import messages
from django.http import JsonResponse
import datetime
import json


@login_required
def admin_dashboard(request):
    doctors_count = accountModels.DoctorDetails.objects.count()
    context = {
        "doctors_count":doctors_count,
    }
    return render(request, "admin/deshboard.html",context)


@login_required
def banners_list(request):
    if request.method == "GET":
        banners = admin_models.Banner.objects.all()
        context = {"banners": banners,}
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
        context = {"blogs": blogs_list,}
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
        context = {"banners": banners}
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


# List all expert talks
@login_required
def expert_talks_list(request):
    if request.method == "GET":
        expert_talks = admin_models.ExpertTalk.objects.select_related('doctor').all()
        context = {"expert_talks": expert_talks}
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
    context = {
        "all_users": all_users,
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