# Generated by Django 3.2 on 2023-04-27 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_doctor_fullname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='fullname',
        ),
    ]