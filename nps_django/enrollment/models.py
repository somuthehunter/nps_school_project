from django.db import models

# Create your models here.


class Enrollment(models.Model):
    CLASS_CHOICES = [
        ('Pre-Nursery', ''),
        ('2', 'Nursery'),
        ('3', 'LKG'),
        ('4', 'UKG'),
        ('5', 'I'),
        ('6', 'II'),
        ('7', 'III'),
        ('8', 'IV'),
        ('9', 'V'),
        ('10', 'VI'),
        ('11', 'VII'),
        ('12', 'VIII'),
        # Add more classes as necessary
    ]

    student_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=2, choices=CLASS_CHOICES)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    question = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - {self.email}"