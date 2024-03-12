from django.db import models
from django.views.generic import View



# Create your models here.
class user(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    uname = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    mailid = models.EmailField(max_length=40)
    phone = models.CharField(max_length=10)
    def __str__(self):
        return '%S,%S,%S,%S,%S,%S'%(self.fname,self.lname,self.uname,self.password,self.mailid,self.phone)