from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
import hospital.models as hospital_module
import datetime




# Create your views here.
def lab_dashboard(request):
    return render(request, "lab_dashboard.html")


def lab_login(request):
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
        
    if request.method == "GET":
        return render(request, 'lab/labLogin.html')

def lab_register(request):
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
    return render(request, "lab/lab_register.html")