from django.db import models
from django.urls import reverse


class Function(models.Model):
    title = models.CharField(max_length=100)
    func = models.TextField()
    
        
    def __str__(self):
        return self.title
    
# be sure to makemigrations after creating the model
# and to migrate. This introduces the model and its 
# field attributes to the database.
        
# return to the database after making new function
    
    def get_absolute_url(self):
        return reverse('database')