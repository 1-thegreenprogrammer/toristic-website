from ast import Mod
from distutils.command.upload import upload
from email.mime import image
from tkinter import Image
from xml.etree.ElementTree import XML
from django.db import models

class Hotel(models.Model):
    name=models.CharField(max_length=150)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    dec=models.CharField(max_length=150)
    image=models.ImageField(upload_to='pictures/%y/%m/%d')
    active=models.BooleanField(default=True)
    phone=models.CharField(max_length=10,blank=True,null=True)
    def __str__(self):
        return self.name
class HotelView(models.Model):
    Image=models.ImageField('hotels') 
    Hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    des=models.TextField(max_length=500) 
    def __str__(self):
        return self.Hotel.name 
    
class Resto(models.Model):
    name=models.CharField(max_length=150)
    dec=models.TextField(max_length=150)
    image=models.ImageField(upload_to='pictures/%y/%m/%d')
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name   
class Agenda(models.Model):
    name=models.CharField(max_length=150)
    dec=models.TextField(max_length=150)
    date=models.DateTimeField()
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.name            