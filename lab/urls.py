from django.urls import path
from lab import views


urlpatterns = [
    # Lab Panel
    path('', views.lab_dashboard, name='lab_dashboard'),

    path('login/', views.lab_login, name='lab_login'),
    path('register/', views.lab_register, name='lab_login'),
]