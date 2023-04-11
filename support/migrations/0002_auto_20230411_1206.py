# Generated by Django 3.2 on 2023-04-11 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('condition', models.PositiveSmallIntegerField(choices=[(1, 'new'), (2, 'read')], default=1)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('response', models.TextField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='doctor.doctor')),
            ],
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]