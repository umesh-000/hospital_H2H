from django.urls import path
from lab import views


urlpatterns = [
    # Lab Panel
    path('', views.lab_dashboard, name='lab_dashboard'),
]