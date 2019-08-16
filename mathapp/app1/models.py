from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    
     # make sure to run migrations
     
    def __str__(self):
        return self.title
    
    # return to the forum after making new post
    
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})
    

class Function(models.Model):
    function = models.CharField(max_length=100)
        
# return to the calculus tool after making new function
    
    def get_absolute_url(self):
        return reverse('calculus_tool')