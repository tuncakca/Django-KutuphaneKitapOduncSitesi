from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


from books.models import Book


# Create your models here.

class BorrowCart(models.Model):
    STATUS = (
    ('True', 'Evet'),
    ('False', 'Hayır'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    bookdate = models.CharField(max_length=100, blank=True)
    returndate = models.CharField(max_length=100, blank=True)
    days = models.IntegerField(blank=True)

    ip = models.CharField(max_length=30, blank=True)
    note = models.CharField(max_length=500, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.book.title


class BorrowCartForm(ModelForm):
    class Meta:
        model = BorrowCart
        fields = ['bookdate' ,'returndate']