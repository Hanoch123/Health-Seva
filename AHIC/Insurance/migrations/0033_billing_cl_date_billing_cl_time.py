# Generated by Django 4.1.5 on 2023-04-03 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insurance', '0032_billing_hosp_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='cl_date',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='billing',
            name='cl_time',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]