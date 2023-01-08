from django.contrib import admin
from .models import department,course, units

class departmentAdmin(admin.ModelAdmin):
    list_display = ['department_code', 'department_name']
    search_fields = ['department_code', 'department_name']
    list_filter = ['department_code', 'department_name']

class courseAdmin(admin.ModelAdmin):
    list_display = ['department', 'course_name', 'course_code', 'module']
    search_filter = ['department__department_code', 'course_name', 'course_code', 'module']
    list_filter = ['department__department_code', 'course_name', 'course_code', 'module']

class unitsAdmin(admin.ModelAdmin):
    list_display = ['course', 'unit_code', 'unit']

admin.site.register(department, departmentAdmin)
admin.site.register(course, courseAdmin)
admin.site.register(units, unitsAdmin)
