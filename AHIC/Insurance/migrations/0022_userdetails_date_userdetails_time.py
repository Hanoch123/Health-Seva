# Generated by Django 4.1.5 on 2023-03-30 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insurance', '0021_userdetails_bank_ins'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='date',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='time',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]