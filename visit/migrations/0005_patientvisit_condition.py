# Generated by Django 3.2 on 2023-04-30 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0004_remove_patientvisit_is_visited'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientvisit',
            name='condition',
            field=models.SmallIntegerField(choices=[(1, 'not_visited'), (2, 'visited'), (3, 'refunded')], default=1),
        ),
    ]
