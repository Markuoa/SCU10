import datetime
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class UserInfo(models.Model):
    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    Email = models.EmailField(max_length=30)
    Img = models.CharField(max_length=40, null=True, blank=True)


class Goods(models.Model):
    Commodity_ID = models.AutoField(primary_key=True)
    Commodity_Name = models.CharField(max_length=120, null=True, blank=True)
    Price = models.IntegerField()
    Contact_QQ = models.DecimalField(max_digits=11, decimal_places=0)
    Note = models.CharField(max_length=120)
    Date = models.DateTimeField(auto_now=False, auto_now_add=True)
    UserID = models.ForeignKey('UserInfo', related_name='UserID_Goods', on_delete=models.CASCADE)
    Img = models.CharField(max_length=40, null=True, blank=True)









