from django.db import models

# Create your models here.

class Idea(models.Model):
    title = models.CharField(max_length=150)
    writer = models.CharField(max_length=100)
    body = models.TextField()
    pud_date = models.DateTimeField()
    

