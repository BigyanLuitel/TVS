from django.db import models # type: ignore

# Create your models here.
class Student(models.Model):
    student_name=models.CharField(max_length=100)
    student_class=models.CharField(max_length=20)
    student_image=models.ImageField()
