from django.shortcuts import render

# Create your views here.
def hospital_dashboard(request):
    return render(request,'dashboard.html')