from django.db import models
import datetime as dt
# Create your models here.

class Editor(models.Model):
    username = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 30)
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username

class Location(models.Model):
    loc_name = models.CharField(max_length = 10)
    def __str__(self):
        return self.loc_name

class Category(models.Model):
    cat_name = models.CharField(max_length = 40)
    def __str__(self):
        return self.cat_name
    
    

class Image(models.Model):
    image_name = models.CharField(max_length = 40)
    image_description = models.CharField(max_length = 100)
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)
    image = models.ImageField(upload_to = 'images/')
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.image_name


    @classmethod
    def todays_photos(cls):
            today = dt.date.today()
            photos = cls.objects.filter(pub_date__date = today)
            return photos

