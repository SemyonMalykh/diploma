# Generated by Django 2.1.7 on 2019-04-11 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20190411_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(default='2019-04-11'),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_time',
            field=models.TimeField(default='19:00'),
            preserve_default=False,
        ),
    ]
