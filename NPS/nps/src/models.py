from django.db import models

# Create your models here.

class StudentsPayment(models.Model):
    name = models.CharField(max_length = 50)
    # student_class = models.CharField(max_length = 10)
    # parent_name = models.CharField(max_length = 50)
    amount = models.CharField(max_length = 100)
    razorpay_payment_id = models.CharField(max_length = 100 , blank = True)
    paid = models.BooleanField(default = False)
