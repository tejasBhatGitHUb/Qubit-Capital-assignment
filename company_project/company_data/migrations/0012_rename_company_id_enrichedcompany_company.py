# Generated by Django 5.1 on 2024-08-15 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_data', '0011_rename_company_enrichedcompany_company_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrichedcompany',
            old_name='company_id',
            new_name='company',
        ),
    ]
