# Generated by Django 3.2 on 2023-05-26 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0008_auto_20230509_0235'),
        ('transaction', '0003_transaction_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='doctor.doctor'),
        ),
    ]
