from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Setting(models.Model):
    STATUS = (
        ('TRUE', 'EVET'),
        ('FALSE', 'HAYIR'),
    )
    title = models.CharField(max_length=80)
    keywords = models.CharField(max_length=100)
    description = RichTextUploadingField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    smtpserver = models.CharField(max_length=30)
    smtpemail = models.CharField(max_length=30)
    smtppassword = models.CharField(max_length=30)
    smtpport = models.CharField(max_length=10)
    logo = models.ImageField(upload_to='images/products/')
    icon = models.ImageField(upload_to='images/products/')
    instagram = models.CharField(max_length=30)
    facebook = models.CharField(max_length=30)
    aboutus = RichTextUploadingField()
    contact = RichTextUploadingField()
    references = RichTextUploadingField
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title