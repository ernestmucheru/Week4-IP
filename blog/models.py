from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from authy.models import Profile
from main.models import NeighbourHood

# Create your models here.
class Post(models.Model):
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    hood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='hood_post')

    class Meta:
        db_table = 'posts'
        
    def __str__(self):
        return self.post

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk': self.pk})
    

    # def __repr__(self):
    #     return f'{self.title}'

    # @classmethod
    # def search_posts(cls, searchTerm):
    #     posts = cls.objects.filter(title__icontains=searchTerm)
    #     return posts
