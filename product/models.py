from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm
from django.urls import reverse
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    STATUS = (
        ('TRUE', 'EVET'),
        ('FALSE', 'HAYIR'),
    )
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='images/category/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])

    def get_absolute_url(self):
        return reverse('category_title', kwargs={'slug': self.slug})




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
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='images/products/')
    price = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=True, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_title', kwargs={'slug': self.slug})

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'




class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=80, blank=True)
    image = models.ImageField(blank=True, upload_to='images/products/')
    def __str__(self):
        return self.title



class Office(models.Model):
    STATUS = (
        ('TRUE', 'EVET'),
        ('FALSE', 'HAYIR'),
    )
    title = models.CharField(max_length=80)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    status = models.CharField(max_length=10, choices=STATUS)
    def __str__(self):
        return self.title



class Comment(models.Model):
    STATUS = (
        ('TRUE', 'EVET'),
        ('FALSE', 'HAYIR'),
        ('NEW', 'YENI'),
    )
    name = models.CharField(max_length=80)
    surname = models.CharField(max_length=80)
    email = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS)
    def __str__(self):
        return self.name


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'surname', 'email', 'comment']




class Order(models.Model):
    STATUS = (
        ('TRUE', 'ONLİNE ODEME'),
        ('FALSE', 'OFİSTE ÖDEME'),
    )
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    starthour = models.CharField(max_length=50)
    endhour = models.CharField(max_length=50)
    office = models.CharField(max_length=50)
    price = models.IntegerField()
    days = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product.title















