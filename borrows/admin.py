from django.contrib import admin
from borrows.models import BorrowCart

# Register your models here.
class BorrowCartAdmin(admin.ModelAdmin):
    list_display = ['book','user']
    list_filter = ['user']

admin.site.register(BorrowCart, BorrowCartAdmin)
