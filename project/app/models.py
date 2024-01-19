from django.db import models

# Create your models here.
class Student1Model(models.Model):
    stu1_name = models.CharField(max_length=100)
    stu1_email = models.EmailField()
    stu1_mobile = models.IntegerField()
    stu1_city = models.CharField(max_length=100)
    # students = models.Manager() # Rename model Manager from objects to students
    def __str__(self):
        return self.stu1_name