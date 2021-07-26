from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    image = models.ImageField(upload_to='hood_images/', blank=True)

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
        