from django.shortcuts import render

# Create your views here.
def hospital_dashboard(request):
    # return render(request,'hospital_master.html')
    return render(request,'dashboard.html')