from django.db import models
from datetime import datetime
# Create your models here.

class BuyingProducts(models.Model):
  Email=models.CharField(null=True,blank=True,max_length=50)
  Password=models.CharField(null=True,blank=True,max_length=50)
  phoneNumber=models.CharField(null=True,blank=True,max_length=50)
  Address=models.CharField(null=True,blank=True,max_length=50)
  city=models.CharField(null=True,blank=True,max_length=50)
  state=models.CharField(null=True,blank=True,max_length=50)
  Code=models.CharField(null=True,blank=True,max_length=50)
  Img=models.ImageField(upload_to='aniamls/',default='aniamls 10/animal7.jpg')
  dateTime=models.DateTimeField(default=datetime.now)

  def __str__(self):
    return self.Email
  
  class Meta:
    verbose_name='BuyingProduct'
    ordering=['dateTime']