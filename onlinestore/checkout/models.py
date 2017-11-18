# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.timezone import now

class Order(models.Model):
    #each individual status
    SUBMITTED = 1
    PROCESSED = 2
    SHIPPED = 3
    CANCELLED = 4

    #set of possible order statuses
    ORDER_STATUS = ((SUBMITTED,'Submitted'),
                    (PROCESSED, 'Processed'),
                    (SHIPPED, 'Shipped'),
                    (CANCELLED, 'Cancelled'))

    #order_info
    order_id = models.CharField(max_length=20)
    orderDate = models.DateTimeField(default=now)
    status = models.IntegerField(choices=ORDER_STATUS, default=SUBMITTED)
    # ip_address = models.IPAddressField()
    last_updated = models.DateTimeField(default=now)
    #user = models.ForeignKey(User, null=True)

    #contact info
    email = models.EmailField(max_length=50)
    phone = PhoneNumberField(blank=True)

    #shipping_information
    shipping_name = models.CharField(max_length=50)
    shipping_address_1 = models.CharField(max_length=50)
    shipping_address_2 = models.CharField(max_length=50,blank=True)
    shipping_city = models.CharField(max_length=50)
    shipping_zip = models.CharField(max_length=10)

    #billing information
    billing_name = models.CharField(max_length=50)
    billing_address = models.CharField(max_length=50)
    billing_zip = models.CharField(max_length=10)

    def __unicode__(self):
        return 'Order# ' + str(self.order_id)

    @property
    def total(self):
        total = decimal.Decimal('0.00')
        order_items = OrderItem.objects.filter(order=self)
        for item in order_items:
            total+=item.total
        return total

class OrderItem(models.Model):
    product = models.ForeignKey('catalog.Product')
    quantity = models.IntegerField(default = 1)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    order = models.ForeignKey(Order)

    @property
    def total(self):
        return self.quantity * self.price

    @property
    def name(self):
        return self.product.name

    @property
    def sku(self):
        return self.product.sku

    def __unicode__(self):
        return self.product.name + ' (' +self.product.sku+')'

    def get_absolute_url(self):
        return self.product.get_absolute_url()
