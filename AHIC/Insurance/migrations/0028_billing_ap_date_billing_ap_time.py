# Generated by Django 4.1.5 on 2023-04-02 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insurance', '0027_billing_rel_fund_billing_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='ap_date',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='billing',
            name='ap_time',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
