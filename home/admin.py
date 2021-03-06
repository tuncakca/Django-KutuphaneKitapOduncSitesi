from django.contrib import admin

from home.models import ContactFormMessage, Setting

# Register your models here.

class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'note', 'status']
    list_filter = ['status']


admin.site.register(ContactFormMessage, ContactFormMessageAdmin)
admin.site.register(Setting)
