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
    health_tell = models.IntegerField(null=True, blank=True)
    police_number = models.IntegerField(null=True, blank=True)

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
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='business')
    location = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    


    def __str__(self):
        return f'{self.name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()
      

