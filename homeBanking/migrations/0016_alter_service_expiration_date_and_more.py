# Generated by Django 4.1 on 2023-09-09 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeBanking', '0015_alter_service_paid_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='expiration_date',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='service',
            name='paid_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
