# Generated by Django 4.1.5 on 2023-03-27 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_alter_hashed_client_cli_user'),
        ('Insurance', '0013_userdetails_inc_proof_userdetails_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='cli',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.client'),
        ),
    ]