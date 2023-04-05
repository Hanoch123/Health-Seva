# Generated by Django 4.1.5 on 2023-04-01 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Insurance', '0022_userdetails_date_userdetails_time'),
        ('App', '0007_notification_cli'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='bks',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Insurance.bank'),
        ),
    ]