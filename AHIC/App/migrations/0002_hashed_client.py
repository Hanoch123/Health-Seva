# Generated by Django 4.1.5 on 2023-03-24 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashed_Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashed_details', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
