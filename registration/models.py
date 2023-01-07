from django.db import models

class online_registration(models.Model):
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    surname = models.CharField(max_length=150)
    firstname = models.CharField(max_length=150)
    middlename = models.CharField(max_length=150, blank=True, null=True)
    gender = models.CharField(max_length=150, choices=gender_choices)
    email = models.EmailField(max_length=150)
    contact = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=150)
    town = models.CharField(max_length=150)
    kcse_certificate = models.FileField(upload_to='documents/KCSE/')
    course = models.ForeignKey('department.course', on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.surname + ' ' + self.firstname

    class Meta:
        ordering = ('-registered_at',)
        verbose_name_plural = 'Registered Online'
