from django.db import models

# Create your models here.
class TaskBoard(models.Model):
    task = models.CharField(max_length=200)
    startDate = models.DateField(auto_now_add=True)
    endDate = models.DateField()
    status = models.CharField(max_length=100)
    priority = models.CharField(max_length=10)
    progress = models.IntegerField()

    def __str__(self):
        return self.task
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=10000)
