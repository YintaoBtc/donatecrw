# Generated by Django 2.0.2 on 2018-08-30 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_service_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='finish',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Date Finish'),
        ),
    ]
