from django.contrib import admin
from .models import Upcoming

class latestAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}

class UpcomingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}

# admin.site.register(Latest, latestAdmin)
admin.site.register(Upcoming, UpcomingAdmin)