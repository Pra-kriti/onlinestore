# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 11:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0003_auto_20171118_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=20)),
                ('orderDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.IntegerField(choices=[(1, 'Submitted'), (2, 'Processed'), (3, 'Shipped'), (4, 'Cancelled')], default=1)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('email', models.EmailField(max_length=50)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
                ('shipping_name', models.CharField(max_length=50)),
                ('shipping_address_1', models.CharField(max_length=50)),
                ('shipping_address_2', models.CharField(blank=True, max_length=50)),
                ('shipping_city', models.CharField(max_length=50)),
                ('shipping_zip', models.CharField(max_length=10)),
                ('billing_name', models.CharField(max_length=50)),
                ('billing_address', models.CharField(max_length=50)),
                ('billing_zip', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Product')),
            ],
        ),
    ]
