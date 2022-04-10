from django.db import models

class Employee(models.Model):
    ename = models.CharField(max_length=50)
    eaddr = models.CharField(max_length=50)
    esal = models.FloatField()

