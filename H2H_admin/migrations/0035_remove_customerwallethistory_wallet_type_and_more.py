# Generated by Django 4.2.16 on 2024-12-11 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('H2H_admin', '0034_customerwallethistory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerwallethistory',
            name='wallet_type',
        ),
        migrations.AlterField(
            model_name='customerwallethistory',
            name='transaction_type',
            field=models.CharField(choices=[('customer added amount', 'Customer added amount'), ('refund amount', 'Refund amount'), ('deducted amount', 'Deducted amount')], max_length=30),
        ),
    ]
