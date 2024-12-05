# Generated by Django 4.2.16 on 2024-12-04 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_customer_created_at_and_more'),
        ('H2H_admin', '0024_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpDeskQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='queries', to='accounts.customer')),
            ],
            options={
                'verbose_name': 'Help Desk Query',
                'verbose_name_plural': 'Help Desk Queries',
                'db_table': 'help_desk_queries',
            },
        ),
    ]
