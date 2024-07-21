from django.db import models

class Project(models.Model):
    TOPIC_CHOICES = [
        ('Web Development', 'Web Development'),
        ('Data Science', 'Data Science'),
        ('Machine Learning', 'Machine Learning'),
        ('Mobile App Development', 'Mobile App Development'),
        # Add more topics as needed
    ]
    
    LANGUAGES_CHOICES = [
        ('Python', 'Python'),
        ('JavaScript', 'JavaScript'),
        ('Java', 'Java'),
        ('C++', 'C++'),
        # Add more languages as needed
    ]
    
    topic = models.CharField(max_length=50, choices=TOPIC_CHOICES)
    languages_used = models.CharField(max_length=50, choices=LANGUAGES_CHOICES)
    duration = models.IntegerField(help_text="Duration in days")

    def __str__(self):
        return f'{self.topic} - {self.languages_used} ({self.duration} days)'
