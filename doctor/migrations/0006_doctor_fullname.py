# Generated by Django 3.2 on 2023-04-27 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_alter_request_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='fullname',
            field=models.CharField(default='<django.db.models.fields.CharField> <django.db.models.fields.CharField>', max_length=80),
        ),
    ]