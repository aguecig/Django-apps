from django.db import models
#from django.utils import timezone
#from django.contrib.auth.models import User
from django.urls import reverse


class Function(models.Model):
    equation = models.CharField(max_length=100)
        
# return to the calculus tool after making new function
    
    def get_absolute_url(self):
        return reverse('calculus_tool')