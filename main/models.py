from django.db import models
from django.contrib.auth.models import User
# from django.dispatch import receiver
from cloudinary.models import CloudinaryField
# from django.db.models.signals import post_save
from authy.models import *
# Create your models here.


class NeighbourHood(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    image = CloudinaryField('image')
    description = models.TextField(null=True)

    class Meta:
        db_table = 'neighbourhoods'
        ordering = ['-name']

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def search_hood(cls, searchTerm):
        hoods = cls.objects.filter(name__icontains=searchTerm)
        return hoods

    @classmethod
    def search_by_title(cls, search_term):
        hoods = cls.objects.filter(name__icontains=search_term)
        return hoods

class Business(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    location = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'businesses'
        ordering = ['-name']

    def __repr__(self):
        return f'{self.name}'

    @classmethod
    def search_biz(cls, searchTerm):
        biz = cls.objects.filter(name__icontains=searchTerm)
        return biz  
    def __str__(self):
        return f'{self.name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls, business_id):
        return cls.objects.filter(id=business_id)
      

class EmergencyContact(models.Model):
    name = models.CharField(max_length=250)
    contact = models.CharField(max_length=250)
    description = models.TextField()

    class Meta:
        db_table = 'e_contacts'
        ordering = ['-name']

    def __repr__(self):
        return f'{self.name}'

    @classmethod
    def search_emergencies(cls, searchTerm):
        emergencies = cls.objects.filter(name__icontains=searchTerm)
        return emergencies
