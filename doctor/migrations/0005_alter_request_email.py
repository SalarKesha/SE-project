# Generated by Django 3.2 on 2023-04-12 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_alter_request_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
