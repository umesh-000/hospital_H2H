from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin_register/', views.admin_register, name='admin_register'),
    path('hospital_register/', views.hospital_register, name='hospital_register'),
    path('doctor_register/', views.doctor_register, name='doctor_register'),
    path('lab_register/', views.lab_register, name='lab_register'),
    path('login/', views.admin_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]