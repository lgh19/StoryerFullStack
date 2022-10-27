from django.db import models

# Create your models here.
# To update models:
# py manage.py makemigrations
# py manage.py migrate


class Student(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    group = models.ForeignKey("Group", on_delete = models.DO_NOTHING, null=True, related_name="assigned_group")
    preferences = models.ManyToManyField("Group", through="Preference", related_name="group_preferences")

    def __str__(self):
        return self.name

# through table for student preferences for a group
class Preference(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE, null=False)
    group_preference = models.ForeignKey("Group", on_delete=models.CASCADE, null=False)
    priority = models.IntegerField(blank=False, null=False)
    date_listed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.group_preference.name + ":" + str(self.priority)

class Group(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Assignment(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.title
