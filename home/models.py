from telnetlib import STATUS
from django.db import models

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
    aboutUs = models.TextField(blank=True)
    contact = models.TextField(blank=True)
    references = models.TextField(blank=True)
    status = models.CharField(blank=True,max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

