from distutils.command.upload import upload
from django.db import models

class Image(models.Model):
    image_path = models.ImageField(upload_to = 'pictures/')
    image_name = models.CharField(max_length=100)
    description = models.TextField()
    # location =
    # category =
    
    def __str__(self):
        return self.image_name
    
