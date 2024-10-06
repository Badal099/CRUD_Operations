from django.db import models

# Create your models here.
class Employee(models.Model):
    empid = models.CharField(max_length=10)
    empname = models.CharField(max_length=40)
    empdesignation = models.CharField(max_length=50)
    empcontact = models.IntegerField()

    def __str__(self):
        return self.empname