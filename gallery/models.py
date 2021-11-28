from django.db import models

class Location(models.Model):
    location_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.location_name
    
    def save_location(self):
        '''Saves a location instance to the database'''
        self.save()
        
    @classmethod
    def get_locations(cls):
        '''Retrieves all the location instances from the database'''
        return cls.objects.all()
    
    @classmethod
    def update_location(cls,loc_id, value):
        '''Updates a location instance '''
        updated= Location.objects.get(id=loc_id)
        updated.location_name=value
        return updated.save()
    
    @classmethod
    def delete_location(cls,loc_id):
        '''Retrieves an image instance from the database by id'''
        return cls.objects.filter(id=loc_id).delete()

    
    


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category_name

class Image(models.Model):
    image_path = models.ImageField(upload_to = 'pictures/')
    image_name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.ForeignKey(to=Location,on_delete=models.CASCADE, null=True)
    categories = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.image_name
    
    def save_image(self):
        '''Saves an image instance to the database'''
        self.save()
        
    @classmethod
    def get_images(cls):
        '''Retrieves all the image instances from the database'''
        return cls.objects.all()
    
    @classmethod
    def get_single_image(cls,image_id):
        '''Retrieves an image instance from the database by id'''
        return cls.objects.filter(pk=image_id).get()
        

    # @classmethod
    # def update_image(cls,image_id,*, kwargs):
    #     '''Updates an image instance's attribute values'''
    #     return cls.objects.filter(id=image_id).update()
    
    @classmethod
    def delete_image(cls,image_id):
        '''Retrieves an image instance from the database by id'''
        return cls.objects.filter(id=image_id).delete()
