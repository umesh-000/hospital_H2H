from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password,check_password
from hospital import models
import datetime

def hospital_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        hashed_password = make_password(password)
        try:
            hospital = models.Hospital.objects.get(email=email)
        except models.Hospital.DoesNotExist:
            hospital = None
        if hospital and check_password(password, hospital.password):
            print("Login successful")
            return redirect('hospital_dashboard')
        else:
            print("Invalid email or password")
            return render(request, "login.html")
    return render(request, "hospital_login.html")

def hospital_register(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        hashed_password = make_password(password)
        create_at = datetime.datetime.now()
        modified_at = datetime.datetime.now()
        admin = models.Admin(username=username, password=hashed_password, email=email, create_at=create_at, modified_at=modified_at)
        admin.save()
        return redirect('/admin/login/')
    return render(request, "hospital_register.html")