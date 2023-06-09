# Generated by Django 4.1.5 on 2023-04-02 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_notification_bks'),
        ('Insurance', '0024_alter_userdetails_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billing',
            name='billing_date',
        ),
        migrations.AddField(
            model_name='billing',
            name='admit_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='billing',
            name='banks',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Insurance.bank'),
        ),
        migrations.AddField(
            model_name='billing',
            name='cli',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.client'),
        ),
        migrations.AddField(
            model_name='billing',
            name='disc_date',
            field=models.DateField(null=True),
        ),
    ]
