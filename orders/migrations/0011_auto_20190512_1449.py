# Generated by Django 2.1.7 on 2019-05-12 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20190512_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(default='2019-04-11', null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_time',
            field=models.TimeField(null=True),
        ),
    ]