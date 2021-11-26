from django.db import models

class Location(models.Model):
    location_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.location_name
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category_name

class Image(models.Model):
    image_path = models.ImageField(upload_to = 'pictures/')
    image_name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.image_name
    
