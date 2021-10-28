
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from datetime import datetime
# Create your models here.


class Customer(models.Model):
  user=models.OneToOneField(User,null=True,blank=True,on_delete=CASCADE)
  name=models.CharField(max_length=200,default='Name')
  phone=models.CharField(max_length=200,default='phone')
  email=models.CharField(max_length=200,default='email')
  profile_pic=models.ImageField(null=True,blank=True,default='images/user.png')
  date_created=models.DateField(datetime.now(),null=True)

  def __str__(self):
    return self.name


class contactUS(models.Model):
  YourName=models.CharField(max_length=50,null=True,blank=True)
  YourEmail=models.EmailField(max_length=70,null=True,blank=True)
  YourPhone=models.CharField(max_length=30,null=True,blank=True)
  YourMessages=models.TextField(max_length=500,null=True,blank=True)

  class Meta:
    verbose_name='Problem'
    ordering=['YourName']

  def __str__(self):
      return self.YourName