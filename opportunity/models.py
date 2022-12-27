from django.db import models

class tender(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/tenders/')
    active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class career(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/careers/')
    active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class internship(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/internship/')
    active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title