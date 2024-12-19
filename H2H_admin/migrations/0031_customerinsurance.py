# Generated by Django 4.2.16 on 2024-12-05 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_customer_created_at_and_more'),
        ('H2H_admin', '0030_alter_reminder_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerInsurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_company_id', models.IntegerField(blank=True, null=True)),
                ('insurance_company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('insurance_type', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insurances', to='accounts.customer')),
            ],
            options={
                'db_table': 'customer_insurances',
            },
        ),
    ]