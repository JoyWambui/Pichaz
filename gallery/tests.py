from django.test import TestCase
from .models import Image, Location, Category

class ImageTestCase(TestCase):
    '''Test Class to test the Image Model and its methods'''
    
    def setUp(self):
        '''Defines new instances'''
        self.location = Location(location_name='nairobi')
        self.location.save()
        self.category = Category(category_name='food')
        self.category.save()
        self.image = Image(image_path='imagepath',image_name='spurs',description='a plate of ribs',location=self.location)
        self.image.save()
        self.image.categories.add(self.category)
        
    def tearDown(self):
        '''Clears the database after every test'''
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
        
    def test_save_image(self):
        '''Tests if an image is saved'''
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==1)
        
    def test_get_images(self):
        '''Tests that all images are returned'''
        self.image.save_image()
        self.location1 = Location(location_name='thika')
        self.location1.save()
        self.category1 = Category(category_name='travel')
        self.category1.save()
        self.image1 = Image(image_path='imagepath1',image_name='pineapple',description='a pinapple farm',location=self.location1)
        self.image1.save_image()
        self.image1.categories.add(self.category1)
        images = Image.get_images()
        self.assertTrue(len(images)==2)
        
    def test_get_single_image(self):
        '''Retrieves an image instance from the database by id'''
        self.image.save_image()
        print(self.image.pk)
        got_image= Image.get_single_image(4)
        self.assertEquals(self.image,got_image)

        
    # def test_update_image(self):
    #     '''Tests whether an image instance can be updated'''
    #     self.image.save_image()
    #     update = Image.update_image(5,image_name ='pineapples')
    #     print(self.image.image_name)
    #     #self.assertEquals(self.image.image_name,'pineapples')
    
    def test_delete_image(self):
        '''Tests whether an image instance is deleted'''
        self.image.save_image()
        Image.delete_image(1)
        images = Image.get_images()
        self.assertTrue(len(images)==0)
        
class LocationTestCase(TestCase):
    '''Tests the Location Model and its methods'''
    
    def setUp(self):
        '''Creates an instance of the Location Model'''
        self.location = Location(location_name='nairobi')
    
    def tearDown(self):   
        '''Clears the database after every test'''
        Location.objects.all().delete()
        
    def test_save_location(self):
        '''Tests if a location is saved'''
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)==1)

    def test_get_locations(self):
        '''Tests that all location instances are returned'''
        self.location.save_location()
        self.location1 = Location(location_name='thika')
        self.location1.save()
        locations = Location.get_locations()
        self.assertTrue(len(locations)==2)
        
    # def test_update_location(self):
    #     '''Tests that a location can be updated'''
    #     self.location.save_location()
    #     print('loc=',self.location.pk)
    #     Location.update_location(9,'thika')
    #     self.assertEquals(self.location.location_name,'thika')
    
    def test_delete_location(self):
        '''Tests that a location instance is deleted'''
        self.location.save_location()
        print('loc=',self.location.pk)
        Location.delete_location(6)
        locations = Location.get_locations()
        self.assertTrue(len(locations)==0)
        
class CategoryTestCase(TestCase):
    '''Tests the Category Model and its methods'''
    
    def setUp(self):
        '''Creates an instance of the Category Model'''
        self.category = Category(category_name='business')
    
    def tearDown(self):   
        '''Clears the database after every test'''
        Category.objects.all().delete()
        
    def test_save_category(self):
        '''Tests if a category is saved'''
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)==1)

    def test_get_categories(self):
        '''Tests that all category instances are returned'''
        self.category.save_category()
        self.category1 = Category(category_name='fitness')
        self.category1.save()
        categories = Category.get_categories()
        self.assertTrue(len(categories)==2)
        
    # def test_update_category(self):
    #     '''Tests that a category can be updated'''
    #     self.category.save_category()
    #     print('loc=',self.category.pk)
    #     Category.update_category(9,'thika')
    #     self.assertEquals(self.category.category_name,'thika')
    
    def test_delete_category(self):
        '''Tests that a category instance is deleted'''
        self.category.save_category()
        print('cat=',self.category.pk)
        Category.delete_category(1)
        categories = Category.get_categories()
        self.assertTrue(len(categories)==0)
