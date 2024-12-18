# Generated by Django 4.2.16 on 2024-11-23 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_doctordetails_join_date'),
        ('H2H_admin', '0012_alter_cliniccategory_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorClinics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinic_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('consultation_minutes', models.CharField(default='0', max_length=10)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=0)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('clinic_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='H2H_admin.cliniccategory')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clinics', to='accounts.doctordetails')),
            ],
            options={
                'db_table': 'doctor_clinics',
            },
        ),
    ]
