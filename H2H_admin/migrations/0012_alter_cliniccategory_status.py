# Generated by Django 4.2.16 on 2024-11-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('H2H_admin', '0011_cliniccategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliniccategory',
            name='status',
            field=models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=1),
        ),
    ]
