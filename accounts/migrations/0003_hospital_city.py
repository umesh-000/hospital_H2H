# Generated by Django 4.2.16 on 2024-11-19 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_customer_email_remove_doctordetails_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
