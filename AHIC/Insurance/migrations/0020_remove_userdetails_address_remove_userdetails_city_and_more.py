# Generated by Django 4.1.5 on 2023-03-29 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Insurance', '0019_userdetails_banks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='City',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='NetWorth',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='Occupation',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='State',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='ph_num',
        ),
    ]