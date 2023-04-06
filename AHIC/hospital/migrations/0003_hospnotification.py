# Generated by Django 4.1.5 on 2023-04-05 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Insurance', '0034_billing_medication_billing_treatment'),
        ('hospital', '0002_alter_hospital_age_alter_hospital_category_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HospNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notf', models.CharField(blank=True, max_length=100, null=True)),
                ('bks', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Insurance.bank')),
                ('hosp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.hosp_details')),
            ],
        ),
    ]