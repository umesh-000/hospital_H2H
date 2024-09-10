from django.urls import path
from . import views

urlpatterns = [

    # Hospital Panel
    path('', views.hospital_dashboard, name='hospital_dashboard'),
]