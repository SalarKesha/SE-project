# Generated by Django 3.2 on 2023-05-26 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0004_alter_transaction_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='doctor',
        ),
    ]