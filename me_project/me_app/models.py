from django.db import models

class Idea(models.Model):
    title = models.CharField(max_length=150)
    writer = models.CharField(max_length=100)
    body = models.TextField
    pub_date = models.DateTimeField
    

# Create your models here.
