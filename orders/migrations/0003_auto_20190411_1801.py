# Generated by Django 2.1.7 on 2019-04-11 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190407_1050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='prive',
            new_name='price',
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
