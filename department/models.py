from django.db import models

class department(models.Model):
    department_name = models.CharField(max_length=150)
    department_code = models.CharField(max_length=150)

    def __str__(self):
        return self.department_name

class course(models.Model):
    exam_bodies_choices = [
        ('KNEC', 'KNEC'),
        ('NITA', 'NITA'),
        ('KASNEB', 'KASNEB'),
    ]
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=150)
    course_name = models.CharField(max_length=150)
    module = models.CharField(max_length=50)
    exam_body = models.CharField(max_length=50, choices = exam_bodies_choices)
    min_qualification = models.CharField(max_length=150)
    duration = models.CharField(max_length=50)
    intake = models.CharField(max_length=50)

    def __str__(self):
        return self.course_code
class units(models.Model):
    course = models.ForeignKey(course, on_delete=models.CASCADE)
    unit_code = models.CharField(max_length=150)
    unit = models.CharField(max_length=150)

    def __str__(self):
        return self.unit_code

    class Meta:
        verbose_name_plural = 'Units'