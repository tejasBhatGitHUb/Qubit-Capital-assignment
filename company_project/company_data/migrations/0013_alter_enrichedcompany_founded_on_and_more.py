# Generated by Django 5.1 on 2024-08-15 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_data', '0012_rename_company_id_enrichedcompany_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrichedcompany',
            name='founded_on',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='enrichedcompany',
            name='specialities',
            field=models.TextField(blank=True, null=True),
        ),
    ]
