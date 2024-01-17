from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 100)
    role_number = models.IntegerField()
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
