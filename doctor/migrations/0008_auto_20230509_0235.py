# Generated by Django 3.2 on 2023-05-08 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0007_remove_doctor_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='phone_number',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='request',
            name='medical_code',
            field=models.CharField(max_length=5),
        ),
    ]