# Generated by Django 2.1.7 on 2019-04-05 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('second_name', models.CharField(max_length=200)),
                ('gender', models.BooleanField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CourierToOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_pickpup', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('second_name', models.CharField(max_length=200)),
                ('gender', models.BooleanField()),
                ('email', models.EmailField(max_length=254)),
                ('position', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('prive', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemToOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prive', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Laundry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateField()),
                ('time_pickup', models.TimeField()),
                ('is_selfpickup', models.BooleanField()),
                ('status', models.CharField(max_length=200)),
                ('is_paid', models.BooleanField()),
                ('date_payment', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Client')),
                ('laundry', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orders.Laundry')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='itemtoorder',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.User'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.User'),
        ),
        migrations.AddField(
            model_name='couriertoorder',
            name='courier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Employee'),
        ),
        migrations.AddField(
            model_name='couriertoorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order'),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.User'),
        ),
    ]
