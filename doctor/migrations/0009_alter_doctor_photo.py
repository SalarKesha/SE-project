# Generated by Django 3.2 on 2023-05-30 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0008_auto_20230509_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='photo',
            field=models.ImageField(blank=True, default='C:\\Users\\SALAR\\Desktop\\project\\mysite\\media/icons/defdoc.png', null=True, upload_to='doctors/'),
        ),
    ]
