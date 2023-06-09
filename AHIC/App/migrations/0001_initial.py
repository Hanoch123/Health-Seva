# Generated by Django 4.1.5 on 2023-03-07 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('ph_num', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('Address', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('Occupation', models.CharField(max_length=50)),
                ('NetWorth', models.CharField(max_length=50)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
