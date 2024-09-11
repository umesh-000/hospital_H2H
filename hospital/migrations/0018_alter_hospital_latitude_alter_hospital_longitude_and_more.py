# Generated by Django 4.2.14 on 2024-09-11 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0017_alter_customer_email_alter_customer_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='latitude',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='longitude',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='HospitalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='hospital/hospital_images/')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='hospital.hospital')),
            ],
        ),
    ]