# Generated by Django 3.2 on 2023-05-13 22:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0003_auto_20230411_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('condition', models.PositiveSmallIntegerField(choices=[(1, 'new'), (2, 'seen_only'), (3, 'answered')], default=1)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('response', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='patientmessage',
            name='patient',
        ),
        migrations.DeleteModel(
            name='DoctorMessage',
        ),
        migrations.DeleteModel(
            name='PatientMessage',
        ),
    ]
