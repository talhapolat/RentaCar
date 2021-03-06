from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
from django.forms import ModelForm, TextInput, Textarea
from django.utils.safestring import mark_safe


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


class Contact(models.Model):
    STATUS = (
        ('NEW', 'YENİ'),
        ('READ', 'OKUNDU'),
    )
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS, default='NEW')
    message = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'İsim'}),
            'email': TextInput(attrs={'class': 'input', 'placeholder': 'Email Adresi'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Konu'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'Mesajınız'}),
        }

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    image = models.ImageField(blank=True, upload_to='images/users/')
    def __str__(self):
        return self.user.username
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'address', 'city', 'image']
