# Generated by Django 4.1.5 on 2023-04-02 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insurance', '0025_remove_billing_billing_date_billing_admit_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='policy_no',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
