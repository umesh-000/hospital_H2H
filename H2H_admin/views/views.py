from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
# from .. import models
import doctor.models as doctor_module
import hospital.models as hospital_module
import datetime

def home(request):
    return redirect('admin_login')

def index(request):
    doctors_count = doctor_module.DoctorDetails.objects.count()
    context = {
        "doctors_count":doctors_count,
    }
    return render(request, "admin/deshboard.html",context)

def users(request):
    users = hospital_module.Admin.objects.all()
    
    context = {
        "users":users,
    }
    return render(request,"admin/users.html",context)

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        hashed_password = make_password(password)
        try:
            admin = hospital_module.Admin.objects.get(email=email)
        except hospital_module.Admin.DoesNotExist:
            admin = None
        if admin and check_password(password, admin.password):
            messages.success(request, 'Login Successfully!')
            return redirect('/admin/')
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, "admin_login.html")
    return render(request, "admin/admin_login.html")

def register(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        hashed_password = make_password(password)
        create_at = datetime.datetime.now()
        modified_at = datetime.datetime.now()
        admin = hospital_module.Admin(username=username, password=hashed_password, email=email, created_at=create_at, modified_at=modified_at)
        admin.save()
        return redirect('/admin/login/')
    return render(request, "admin/admin_register.html")

def show_user(request, id):
    user = get_object_or_404(hospital_module.Admin, id=id)
    return render(request, 'admin/show_user.html', {'user': user})

def edit_user(request, id):
    user = get_object_or_404(hospital_module.Admin, id=id)
    if request.method=="GET":
        return render(request, 'admin/edit_user.html', {'user': user})
    if request.method=="POST":
        username = request.POST.get('username')
        modified_at = datetime.datetime.now()
        user.username = username
        user.modified_at = modified_at
        user.save()
        return redirect('/admin/users/')

def delete_user(request, id):
    user = get_object_or_404(hospital_module.Admin, id=id)
    user.delete()
    return redirect('/admin/users/')