from django.db import models
from django.urls import reverse

class Category(models.Model):
    category_name   =  models.CharField(max_length=50, unique=True)
    slug            =  models.SlugField(max_length=50, unique=True)
    description     =  models.CharField(max_length=250, blank=True)
    cat_image       =  models.ImageField(upload_to='photos/categories', blank=True, null=True)


    #Django make the models name plural in django administration. so to prevent that
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'

    '''
        reverse is to provide the URL path by using the name of the view defined in urls.py,
        instead of hardcoding the URL string manually.
        This ensures flexibility and avoids errors if URLs change later.   
    '''
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    '''
        __str__ is for : whenever you print the object or see it in Django Admin or Django Shell, it will display the 
        value of self.category_name.Shows category_name instead of Category object (1). When you represent an object of
        this class as a string (e.g., in the admin panel, templates, or print statements), use its category_name field.
    '''
    def __str__(self):
        return self.category_name

