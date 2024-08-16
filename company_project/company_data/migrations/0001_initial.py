# Generated by Django 5.1 on 2024-08-15 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_linkedin_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='EnrichedCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enriched_data', models.JSONField()),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='company_data.company')),
            ],
        ),
    ]
