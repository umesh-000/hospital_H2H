# Generated by Django 4.2.16 on 2024-11-30 11:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_customer_created_at_and_more'),
        ('H2H_admin', '0020_experttalk'),
    ]

    operations = [
        migrations.CreateModel(
            name='BedBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward_type', models.CharField(max_length=255)),
                ('bed_type', models.CharField(max_length=255)),
                ('booking_type', models.CharField(max_length=255)),
                ('patient_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('contact_number', models.CharField(max_length=20)),
                ('emergency_contact', models.CharField(blank=True, max_length=20, null=True)),
                ('blood_group', models.CharField(max_length=10)),
                ('medical_history', models.TextField(blank=True, null=True)),
                ('booking_reason', models.CharField(max_length=255)),
                ('insurance_info', models.TextField(blank=True, null=True)),
                ('admission_date', models.DateField()),
                ('discharge_date', models.DateField(blank=True, null=True)),
                ('booking_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('time_slot', models.TimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('rejected', 'Rejected'), ('accepted', 'Accepted')], default='pending', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bed_bookings', to='accounts.customer')),
                ('doctor_assigned', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bed_bookings', to='accounts.doctordetails')),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bed_bookings', to='accounts.hospital')),
            ],
            options={
                'db_table': 'bed_bookings',
            },
        ),
    ]
