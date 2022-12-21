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
