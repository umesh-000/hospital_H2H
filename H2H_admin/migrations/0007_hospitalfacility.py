# Generated by Django 4.2.16 on 2024-11-19 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_hospitalimage_table'),
        ('H2H_admin', '0006_hospitaldepartment'),
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalFacility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='hospital/facility_icons/')),
                ('facility', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='facilities', to='accounts.hospital')),
            ],
            options={
                'db_table': 'hospital_facility',
            },
        ),
    ]