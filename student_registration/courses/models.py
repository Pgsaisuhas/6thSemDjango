from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Student(models.Model):
    name = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course, related_name="students")


    def __str__(self):
        return f"{', '.join(course.name for course in self.courses.all())} - {self.name}"