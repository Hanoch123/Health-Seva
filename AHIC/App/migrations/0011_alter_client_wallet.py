# Generated by Django 4.1.5 on 2023-04-02 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_client_wallet_delete_walletmon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='wallet',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
