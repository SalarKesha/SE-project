# Generated by Django 3.2 on 2023-04-30 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_delete_patientvisit'),
        ('visit', '0002_auto_20230501_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientvisit',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='patient_visits', to='patient.patient'),
        ),
    ]
