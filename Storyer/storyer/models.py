from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    

    def __str__(self):
        return self.name
class Assignment(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    students = models.ManyToManyField('Student')
    def __str__(self):
        return self.title