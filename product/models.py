from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Category(models.Model):
    STATUS = (
        ('TRUE', 'EVET'),
        ('FALSE', 'HAYIR'),
    )
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='images/category/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Product(models.Model):
    STATUS = (
        ('TRUE', 'EVET'),
        ('FALSE', 'HAYIR'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    model = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    fuel = models.CharField(max_length=30)
    gear = models.CharField(max_length=30)
    km = models.CharField(max_length=30)
    engine = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    keywords = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/products/')
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=80, blank=True)
    image = models.ImageField(blank=True, upload_to='images/products/')
    def __str__(self):
        return self.title
















