# Generated by Django 4.1.5 on 2023-03-26 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_alter_hashed_client_cli_user'),
        ('Insurance', '0010_alter_bankinsurance_desc'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InsDocs',
            new_name='UserDetails',
        ),
    ]
