from django.contrib import admin
from .models import contact

class contactAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'subject', 'email', 'queried_at']
    search_fields= ['firstname', 'lastname', 'subject', 'email', 'queried_at']
    list_filter = ['email', 'queried_at', 'subject']


admin.site.register(contact, contactAdmin)
