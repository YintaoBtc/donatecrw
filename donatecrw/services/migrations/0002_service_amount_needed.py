# Generated by Django 2.0.2 on 2018-08-23 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='amount_needed',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Crowns necesarios'),
        ),
    ]
