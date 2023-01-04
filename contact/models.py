from django.db import models
from ckeditor.fields import RichTextField

class contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    body = RichTextField()
    queried_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email