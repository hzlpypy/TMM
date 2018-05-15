# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

import datetime

from decimal import Decimal
from django.db import models
from django.db.models import QuerySet


class Change(models.Model):
    class Meta:
        abstract = True

    def to_dict(self):
        dic = {}
        for key in vars(self).keys():
            if '_' not in key:
                var = getattr(self, key)
                if isinstance(var, datetime.date):
                    dic[key] = datetime.date.strftime(var, '%Y%m%d')
                elif isinstance(var, datetime.datetime):
                    dic[key] = datetime.datetime.strftime(var, '%Y%m%d %H%M%S')
                elif isinstance(var, Decimal):
                    dic[key] = float(var)
                else:
                    dic[key] = var
        return dic

    @staticmethod
    def qs_to_dict(key):
        #转化列表嵌套字典的形式
        li = []
        if isinstance(key,QuerySet):
            li = [models.to_dict() for models in key]
        return li


class Category(Change):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:

        db_table = 'category'


class CategorySub1(Change):
    name = models.CharField(max_length=255, blank=True, null=True)
    cid = models.ForeignKey(Category, models.DO_NOTHING, db_column='cid', blank=True, null=True)

    class Meta:

        db_table = 'category_sub1'


class CategorySub2(Change):
    name = models.CharField(max_length=255, blank=True, null=True)
    cs1id = models.ForeignKey(CategorySub1, models.DO_NOTHING, db_column='cs1id', blank=True, null=True)

    class Meta:

        db_table = 'category_sub2'


class Categorysub(Change):
    name = models.CharField(max_length=255, blank=True, null=True)
    cid = models.ForeignKey(Category, models.DO_NOTHING, db_column='cid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorysub'


class DjangoMigrations(Change):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Jj(Change):
    jjj = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jj'


class Order(Change):
    ordercode = models.CharField(db_column='orderCode', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.
    address = models.CharField(max_length=255, blank=True, null=True)
    post = models.CharField(max_length=255, blank=True, null=True)
    receiver = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    usermessage = models.CharField(db_column='userMessage', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    paydate = models.DateTimeField(db_column='payDate', blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='deliveryDate', blank=True, null=True)  # Field name made lowercase.
    confirmdate = models.DateTimeField(db_column='confirmDate', blank=True, null=True)  # Field name made lowercase.
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order'


class Orderitem(Change):
    pid = models.ForeignKey('Product', models.DO_NOTHING, db_column='pid', blank=True, null=True)
    oid = models.IntegerField(blank=True, null=True)
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orderitem'


class Product(Change):
    name = models.CharField(max_length=255, blank=True, null=True)
    subtitle = models.CharField(db_column='subTitle', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    orignalprice = models.FloatField(db_column='orignalPrice', blank=True, null=True)  # Field name made lowercase.
    promoteprice = models.FloatField(db_column='promotePrice', blank=True, null=True)  # Field name made lowercase.
    stock = models.IntegerField(blank=True, null=True)
    cid = models.ForeignKey(Category, models.DO_NOTHING, db_column='cid', blank=True, null=True)
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    img_list = {}
    class Meta:
        managed = False
        db_table = 'product'


class Productimage(Change):
    pid = models.ForeignKey(Product, models.DO_NOTHING, db_column='pid',related_name='product_image', blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'productimage'


class Property(Change):
    cid = models.ForeignKey(Category, models.DO_NOTHING, db_column='cid', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'property'


class Propertyvalue(Change):
    pid = models.IntegerField(blank=True, null=True)
    ptid = models.ForeignKey(Property, models.DO_NOTHING, db_column='ptid', blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'propertyvalue'


class Review(Change):
    content = models.CharField(max_length=4000, blank=True, null=True)
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    pid = models.ForeignKey(Product, models.DO_NOTHING, db_column='pid', blank=True, null=True)
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'review'


class TBanner(Change):
    bid = models.AutoField(primary_key=True)
    path = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 't_banner'


class TShopCar(Change):
    shop_car_id = models.AutoField(primary_key=True)
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    pid = models.ForeignKey(Product, models.DO_NOTHING, db_column='pid', blank=True, null=True)
    num = models.IntegerField(db_column='NUM', blank=True, null=True)  # Field name made lowercase.
    create_data = models.DateTimeField(blank=True, null=True)
    update_data = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_shop_car'


class User(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
