from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
import hospital.models as hospital_module
import datetime




# Create your views here.
def lab_dashboard(request):
    return render(request, "lab_dashboard.html")


