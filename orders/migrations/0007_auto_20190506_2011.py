# Generated by Django 2.1.7 on 2019-05-06 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20190506_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='hola@barcelona.es', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.CharField(default=894313124, max_length=50),
            preserve_default=False,
        ),
    ]
