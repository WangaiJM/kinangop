from django.contrib import admin
from .models import student_profile, trainer_profile, guardianInfo


@admin.register(student_profile)
class studentProfileAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'full_name', 'email', 'course', 'contact']
    search_fields = ['student_id__username', 'firstname',
                     'lastname', 'course__course_name']
    list_filter = ['course__course_name', 'gender']

    def full_name(self, obj):
        return '{} {} {}'.format(obj.firstname, obj.middlename, obj.lastname)


@admin.register(trainer_profile)
class studentProfileAdmin(admin.ModelAdmin):
    list_display = ['trainer_id', 'full_name', 'email', 'id_number', 'contact']
    search_fields = ['trainer_id__username', 'firstname',
                     'lastname', 'department__department_name']
    list_filter = ['department__department_name', 'gender']

    def full_name(self, obj):
        return '{} {} {}'.format(obj.firstname, obj.middlename, obj.lastname)


@admin.register(guardianInfo)
class studentProfileAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'full_name', 'email', 'id_number', 'contact']
    search_fields = ['firstname', 'lastname', 'contact']
    list_filter = ['gender']

    def full_name(self, obj):
        return '{} {} {}'.format(obj.firstname, obj.middlename, obj.lastname)
