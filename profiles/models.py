from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL


class student_profile(models.Model):
    student_id = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=150)
    middlename = models.CharField(max_length=150, blank=True, null=True)
    lastname = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    contact = models.CharField(max_length=150)
    gender = models.CharField(max_length=150, choices=[
                              ('Male', 'Male'), ('Female', 'Female')])
    box_number = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=150)
    town = models.CharField(max_length=150)
    course = models.OneToOneField(
        'department.course', on_delete=models.CASCADE)
    passport = models.ImageField(
        upload_to='students/passport/', blank=True, null=True)
    kcse_cert = models.FileField(upload_to='students/kcse/')
    updated_at = models.DateTimeField(auto_now_add=True)
    is_student = models.BooleanField(default=True, editable=False)

    def __str__(self):
        return self.lastname

    class Meta:
        verbose_name = 'Student Profile'
        verbose_name_plural = 'Student Profiles'


class trainer_profile(models.Model):
    trainer_id = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=150)
    middlename = models.CharField(max_length=150, null=True, blank=True)
    lastname = models.CharField(max_length=150)
    id_number = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    contact = models.CharField(max_length=150)
    gender = models.CharField(max_length=150, choices=[
                              ('Male', 'Male'), ('Female', 'Female')])
    box_number = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=150)
    town = models.CharField(max_length=150)
    department = models.OneToOneField(
        'department.department', on_delete=models.CASCADE)
    passport = models.ImageField(
        upload_to='teacher/passport/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_trainer = models.BooleanField(default=True, editable=False)

    def __str__(self):
        return self.id_number

    class Meta:
        verbose_name = 'Trainer Profile'
        verbose_name_plural = 'Trainer Profiles'


class guardianInfo(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=150)
    middlename = models.CharField(max_length=150, null=True, blank=True)
    lastname = models.CharField(max_length=150)
    id_number = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, blank=True, null=True)
    contact = models.CharField(max_length=150)
    gender = models.CharField(max_length=150, choices=[
                              ('Male', 'Male'), ('Female', 'Female')])
    box_number = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=150)
    town = models.CharField(max_length=150)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lastname

    class Meta:
        verbose_name = 'Guardian'
        verbose_name_plural = 'Guardians'
