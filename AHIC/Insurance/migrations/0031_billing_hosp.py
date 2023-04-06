# Generated by Django 4.1.5 on 2023-04-02 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_alter_hospital_age_alter_hospital_category_name_and_more'),
        ('Insurance', '0030_alter_billing_rel_fund'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='hosp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.hosp_details'),
        ),
    ]
