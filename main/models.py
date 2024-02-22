from django.db import models
from datetime import datetime

class Staff(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.f_name

class Attendance(models.Model):
    stuff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    came = models.BooleanField(default=False)
    came_time = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.stuff.name