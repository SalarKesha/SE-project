# Generated by Django 3.2 on 2023-04-09 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0001_initial'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.BigIntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='patient.patient')),
                ('visit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='doctor.visit')),
            ],
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('amount', models.BigIntegerField()),
                ('patient_visit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='refunds', to='patient.patientvisit')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.BigIntegerField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='balances', to='doctor.doctor')),
            ],
        ),
    ]
