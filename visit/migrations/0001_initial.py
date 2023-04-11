# Generated by Django 3.2 on 2023-04-11 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0002_alter_request_condition'),
        ('patient', '0003_auto_20230412_0213'),
        ('transaction', '0002_delete_refund'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_visited', models.BooleanField(default=False)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='PatientVisits', to='patient.patient')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='patient_visit', to='transaction.transaction')),
                ('visit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='PatientVisit', to='doctor.visit')),
            ],
        ),
    ]