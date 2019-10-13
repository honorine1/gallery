from django.db import models
import datetime as dt
# Create your models here.

class Editor(models.Model):
    username = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 30)
    pub_date = models.DateTimeField(auto_now_add=True)


    def save_editor(self):
        self.save()
    def __str__(self):
        return self.username


class Location(models.Model):
    location_name = models.CharField(max_length = 10)


    def save_location(self):
        self.save()
    def __str__(self):
        return self.location_name

class Category(models.Model):
    category_name = models.CharField(max_length = 40)

    def save_category(self):
        self.save()
    def __str__(self):
        return self.category_name

    
    
    

class Image(models.Model):
    # editor_name = models.CharField(max_length = 40)
    image_name = models.CharField(max_length = 40)
    image_description = models.CharField(max_length = 100)
    image_location = models.ForeignKey(Location,db_column='location_name')
    image_category = models.ForeignKey(Category,db_column='category_name')
    image = models.ImageField(upload_to = 'images/')
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.image_name

    
    def save_image(self):
        self.save()
    @classmethod
    def todays_photos(cls):
            today = dt.date.today()
            photos = cls.objects.filter(pub_date__date = today)
            return photos

    @classmethod
    def search_by_category_name(cls,search_term):
        photos =cls.objects.filter(image_category__category_name__contains=search_term)
        return photos


  
