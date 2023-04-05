# Generated by Django 4.1.5 on 2023-03-29 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_alter_hashed_client_cli_user'),
        ('Insurance', '0017_alter_billing_bill'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='cli',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.client'),
        ),
    ]