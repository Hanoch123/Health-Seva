# Generated by Django 4.1.5 on 2023-03-24 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insurance', '0005_remove_bankinsurance_bank_name_bankinsurance_bk_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankinsurance',
            name='no_plans',
            field=models.CharField(max_length=50),
        ),
    ]
