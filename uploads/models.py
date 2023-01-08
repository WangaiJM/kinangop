from django.db import models
from ckeditor.fields import RichTextField

class note(models.Model):
    unit = models.ForeignKey('department.units', on_delete=models.CASCADE)
    subject = models.CharField(max_length=150)
    description = RichTextField(blank=True, null=True)
    file = models.FileField(upload_to='Notes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.subject

class assignment(models.Model):
    unit = models.ForeignKey('department.units', on_delete=models.CASCADE)
    subject = models.CharField(max_length=150)
    description = RichTextField(blank=True, null=True)
    file = models.FileField(upload_to='Notes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.subject