from django.contrib import admin
from .models import Comment, Idea

admin.site.register(Idea)
admin.site.register(Comment)
