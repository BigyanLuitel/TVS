from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore

# Create your models here.
class Student(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    student_name=models.CharField(max_length=100)
    student_class=models.CharField(max_length=20)
    student_image=models.ImageField(upload_to='media/')
