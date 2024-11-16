# Generated by Django 4.2.16 on 2024-10-07 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('H2H_admin', '0003_labtag_remove_laboratory_location_map'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=150)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'services',
            },
        ),
    ]
