# Generated by Django 2.1.4 on 2018-12-04 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_auto_20180908_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='categories',
            field=models.ManyToManyField(related_name='get_projects', to='services.Category', verbose_name='Categories'),
        ),
    ]
