# Generated by Django 2.1.7 on 2019-04-07 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AlterField(
            model_name='client',
            name='gender',
            field=models.BooleanField(default=False),
        ),
    ]
