# Generated by Django 4.1.5 on 2023-03-24 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_hashed_client_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hashed_client',
            old_name='user',
            new_name='cli_user',
        ),
    ]
