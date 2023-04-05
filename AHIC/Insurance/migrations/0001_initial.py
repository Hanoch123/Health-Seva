# Generated by Django 4.1.5 on 2023-02-24 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankInsurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=30)),
                ('features', models.CharField(max_length=500)),
                ('exclusions', models.CharField(max_length=500)),
                ('coverage', models.CharField(choices=[('1', '₹3 Lac'), ('2', '₹5 Lac'), ('3', '₹10 Lac')], default=1, max_length=30)),
                ('plan_type', models.CharField(choices=[('1', 'Base'), ('2', '1 Cr Cover')], default=1, max_length=30)),
                ('insurance_for', models.CharField(choices=[('1', 'Family'), ('2', 'Senior Citizen'), ('3', 'Individual'), ('4', 'Personal Accident'), ('5', 'Parent'), ('6', 'Maternity'), ('7', 'Child Health'), ('8', 'Newborn Baby'), ('9', 'Self-Employed'), ('10', 'Woman Healthcare'), ('11', 'Group')], default=1, max_length=30)),
                ('tenure', models.CharField(choices=[('1', '1 Year'), ('2', '2 Years'), ('3', '3 Years')], default=1, max_length=30)),
                ('hospitals', models.CharField(max_length=500)),
                ('premium', models.IntegerField()),
                ('Brochure', models.FileField(default=None, max_length=250, null=True, upload_to='brochure/')),
            ],
        ),
    ]