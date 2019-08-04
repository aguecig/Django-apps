from django.db import models

# custom imports for user account creation
from django.contrib.auth.models import User

# image scaling imports
from PIL import Image

class Profile(models.Model):
    # one profile per user
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'
         # run migrations for effects to take place
         # make sure to register in admin file of app
         
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # resize image for user profile
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)