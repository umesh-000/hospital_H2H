# Generated by Django 4.2.16 on 2024-09-23 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor', '0002_doctorbanner'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_number', models.CharField(blank=True, max_length=50, null=True)),
                ('booking_for', models.CharField(blank=True, max_length=10, null=True)),
                ('patient_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=255, null=True)),
                ('emergency_contact', models.CharField(blank=True, max_length=255, null=True)),
                ('blood_group', models.CharField(max_length=255)),
                ('medical_history', models.TextField(blank=True, null=True)),
                ('current_symptoms', models.CharField(blank=True, max_length=255, null=True)),
                ('booking_date', models.DateField(blank=True, null=True)),
                ('time_slot', models.TimeField(blank=True, null=True)),
                ('consultation_charge', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('base_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('tax', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('additional_charges', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('final_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('payment_mode', models.CharField(blank=True, max_length=50, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('status', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('clinic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctor.doctorclinics')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctor.doctordetails')),
            ],
        ),
    ]