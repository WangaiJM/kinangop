from django.contrib import admin
from .models import department, course, units, department_message, department_images


class departmentAdmin(admin.ModelAdmin):
    list_display = ['department_code', 'department_name', 'is_academic']
    search_fields = ['department_code', 'department_name', 'is_academic']
    list_filter = ['department_code', 'department_name', 'is_academic']


class courseAdmin(admin.ModelAdmin):
    list_display = ['department', 'course_name', 'course_code', 'module']
    search_filter = ['department__department_code',
                     'course_name', 'course_code', 'module']
    list_filter = ['department__department_code',
                   'course_name', 'course_code', 'module']


class unitsAdmin(admin.ModelAdmin):
    list_display = ['course', 'unit_code', 'unit']


class depatrmentMessageAdmin(admin.ModelAdmin):
    list_display = ['department', 'title']


class departmentImageAdmin(admin.ModelAdmin):
    list_display = ['department', 'title']


admin.site.register(department, departmentAdmin)
admin.site.register(course, courseAdmin)
admin.site.register(units, unitsAdmin)
admin.site.register(department_message, depatrmentMessageAdmin)
admin.site.register(department_images, departmentImageAdmin)
