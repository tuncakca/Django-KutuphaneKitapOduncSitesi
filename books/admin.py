from django.contrib import admin

from books.models import Book, Category, Images

# Register your models here.

class BookImageInline(admin.TabularInline):
    model = Images
    extra = 5

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image_tag',   'status']
    list_filter = ['status', 'category']
    readonly_fields = ('image_tag',)
    inlines = [BookImageInline]
    

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'book', 'image']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Images, ImagesAdmin)

