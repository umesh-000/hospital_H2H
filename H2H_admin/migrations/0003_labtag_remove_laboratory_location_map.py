# Generated by Django 4.2.16 on 2024-09-24 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('H2H_admin', '0002_rename_is_recommended_laboratory_emergency_services_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=150)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Lab Tag',
                'verbose_name_plural': 'Lab Tags',
                'db_table': 'lab_tags',
            },
        ),
        migrations.RemoveField(
            model_name='laboratory',
            name='location_map',
        ),
    ]