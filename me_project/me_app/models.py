from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models import Count
from django.db.models.fields import NullBooleanField
from django.forms.fields import ImageField

class Idea(models.Model):
    title = models.CharField(max_length=150)
    writer = models.CharField(max_length=100)
    body = models.TextField(null=True, default='')
    pud_date = models.DateTimeField()
    image = models.ImageField(upload_to='idea/', blank=True, null=True)
    def summary(self):
        return self.body[:30]

    def count(self):
        counts = Comment.objects.filter(idea=self.pk)
        n=counts.count()
        return n

class Comment(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
