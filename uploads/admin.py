from django.contrib import admin
from .models import assignment, note

class assignmentAdmin(admin.ModelAdmin):
    list_display = ['unit','subject', 'uploaded_at']
    search_fields = ['subject', 'uploaded_at']
    list_filter = ['uploaded_at']

class noteAdmin(admin.ModelAdmin):
    list_display = ['unit','subject', 'uploaded_at']
    search_fields = ['subject', 'uploaded_at']
    list_filter = ['uploaded_at']



admin.site.register(assignment, assignmentAdmin)
admin.site.register(note, noteAdmin)