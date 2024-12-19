# Generated by Django 4.2.17 on 2024-12-13 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_customer_created_at_and_more'),
        ('H2H_admin', '0038_alter_doctorbooking_clinic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='notifications_images/')),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'Active'), (1, 'Inactive')], default=0)),
                ('meta', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('app_module', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='H2H_admin.appmodule')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notifications', to='accounts.customer')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
                'db_table': 'notifications',
            },
        ),
    ]
