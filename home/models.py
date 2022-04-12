from telnetlib import STATUS
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm, TextInput, Textarea
from django.utils.safestring import mark_safe


# Create your models here.

class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(blank=True, max_length=150)
    keywords = models.CharField(blank=True, max_length=150)
    description = models.CharField(blank=True, max_length=150)
    company = models.CharField(blank=True, max_length=150)
    address = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    smptpServer = models.CharField(blank=True, max_length=50)
    smtpEmail = models.CharField(blank=True, max_length=50)
    smtpPassword = models.CharField(blank=True, max_length=50)
    smtpPort = models.CharField(blank=True, max_length=50)
    icon = models.ImageField(blank=True, upload_to='images/')
    instagram = models.CharField(blank=True,max_length=150)
    twitter = models.CharField(blank=True,max_length=150)
    youtube = models.CharField(blank=True,max_length=150)
    aboutUs = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status = models.CharField(blank=True,max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ContactFormMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(blank=True, max_length=50)
    email = models.CharField(blank=True, max_length=50)
    subject = models.CharField(blank=True, max_length=50)
    message = models.CharField(blank=True, max_length=50)
    ip = models.CharField(blank=True, max_length=50)
    note = models.CharField(blank=True, max_length=50)
    name = models.CharField(blank=True, max_length=50)
    status = models.CharField(blank=True,max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name' : TextInput(attrs={'class': 'input', 'placeholder': 'Name & Surname'}),
            'subject' : TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'email' : TextInput(attrs={'class': 'input', 'placeholder': 'Email Address'}),
            'message' : TextInput(attrs={'class': 'input', 'placeholder': 'Your Message', 'rows' : '5'}),
        }
