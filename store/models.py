from django.db import models
from category.models import Category
from django.urls import reverse


class Product(models.Model):
    product_name    = models.CharField(max_length=50, unique=True)
    slug            = models.CharField(max_length=50, unique=True)
    description     = models.CharField(max_length=250, blank=True)
    price           = models.IntegerField()
    product_image   = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=False)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)


    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])


    def __str__(self):
        return self.product_name

