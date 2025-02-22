from django.db import models

# Create your models here.
class Course(models.Model):
    course_code = models.CharField(max_length=40)
    course_name = models.CharField(max_length=100)
    course_credits = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.course_code}-{self.course_name}-{self.course_credits}"
    
