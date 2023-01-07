from django.contrib import admin
from .models import online_registration

class registerAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'surname', 'email', 'course', 'registered_at']
    search_fields = ['surname', 'firstname', 'email', 'course__course_name', 'registered_at']
    list_filter = ['surname', 'firstname', 'email','course__course_name',  'registered_at']

admin.site.register(online_registration, registerAdmin)
