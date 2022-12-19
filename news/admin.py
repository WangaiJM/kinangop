from django.contrib import admin
from .models import Upcoming, Latest

class latestAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    list_display = ['title', 'author', 'created_at']
    search_fields = ['title', 'created_at', 'author__username']
    list_filter = ['created_at']

class UpcomingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    list_display = ['title', 'author', 'created_at']
    search_fields = ['title', 'created_at', 'author__username']
    list_filter = ['created_at']

admin.site.register(Latest, latestAdmin)
admin.site.register(Upcoming, UpcomingAdmin)