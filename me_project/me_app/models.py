from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE


class Idea(models.Model):
    title = models.CharField(max_length=150)
    writer = models.CharField(max_length=100)
    body = models.TextField(null=True, default='')
    pud_date = models.DateTimeField()

class Comment(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)