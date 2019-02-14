# Generated by Django 2.0.2 on 2018-08-24 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_service_amount_needed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='amount_donate',
            field=models.CharField(blank=True, max_length=18, null=True, verbose_name='Saldo donado'),
        ),
        migrations.AlterField(
            model_name='service',
            name='amount_needed',
            field=models.CharField(blank=True, max_length=18, null=True, verbose_name='Crowns necesarios'),
        ),
    ]
