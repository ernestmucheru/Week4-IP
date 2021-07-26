from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from main.models import Neighbourhood
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    age = models.IntegerField(null=True)
    contact = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='members', blank=True, null=True)
    bio = models.TextField(max_length=254, blank=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    @classmethod
    def search_profiles(cls, searchTerm):
        profiles = cls.objects.filter(name__icontains=searchTerm)
        return profiles

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
