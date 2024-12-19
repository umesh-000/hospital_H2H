# Generated by Django 4.2.16 on 2024-12-11 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_customer_created_at_and_more'),
        ('H2H_admin', '0033_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerWalletHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_type', models.CharField(choices=[('wallet recharge', 'Wallet Recharge'), ('purchase', 'Purchase'), ('refund', 'Refund'), ('others', 'Others')], max_length=20)),
                ('message', models.TextField()),
                ('transaction_type', models.CharField(choices=[('credit', 'Credit'), ('debit', 'Debit')], max_length=20)),
                ('amount', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallet_histories', to='accounts.customer')),
            ],
            options={
                'db_table': 'customer_wallet_histories',
            },
        ),
    ]