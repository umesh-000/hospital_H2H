# Generated by Django 4.2.16 on 2024-11-23 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_doctordetails_join_date'),
        ('H2H_admin', '0013_doctorclinics'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True, max_length=255, null=True)),
                ('banner', models.ImageField(upload_to='doctors/banners/')),
                ('position', models.CharField(choices=[('T', 'Top'), ('B', 'Bottom')], default='B', max_length=50)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banners', to='accounts.doctordetails')),
            ],
            options={
                'db_table': 'dr_banners',
            },
        ),
    ]