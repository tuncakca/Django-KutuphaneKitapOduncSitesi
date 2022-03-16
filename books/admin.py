from django.contrib import admin

from books.models import Book, Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status']
    list_filter = ['status', 'category']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)

