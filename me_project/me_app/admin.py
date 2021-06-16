from django.contrib import admin
from .models import Comment, Idea

admin.site.register(Idea)
# Register your models here.

admin.site.register(Comment)
