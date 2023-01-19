from django.db import models
from ckeditor.fields import RichTextField

class about(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    

    def __str__(self):
        return self.title

class statement(models.Model):
    vision = RichTextField()
    mission = RichTextField()
    core_values = RichTextField()
    quality_policy_statement = RichTextField()
    motto = RichTextField()

    def __str__(self):
        return self.motto

class principal(models.Model):
    title = models.CharField(max_length=100)
    message = RichTextField()
    image = models.ImageField(upload_to='images/principal')

    def __str__(self):
        return self.title

class board_of_governor(models.Model):
    title = models.CharField(max_length=100)
    message = RichTextField()
    image = models.ImageField(upload_to='images/bog')

    class Meta:
        verbose_name_plural = 'Board of Governors'
        
    def __str__(self):
        return self.title

class dean(models.Model):
    title = models.CharField(max_length=100)
    message = RichTextField()
    image = models.ImageField(upload_to='images/dean')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Dean of Students'

class service_charter(models.Model):
    title = models.CharField(max_length=150)
    charter = models.FileField(upload_to='charter/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Service Charter'

class gallery(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='gallery/')
    description = RichTextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Galleries'

class carousel(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='carousel/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title