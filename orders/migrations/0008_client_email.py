# Generated by Django 2.1.7 on 2019-05-07 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20190506_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(default='hola@barcelona.es', max_length=254),
            preserve_default=False,
        ),
    ]