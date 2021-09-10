from django.db import models
from django.conf import settings
from datetime import datetime

from django.db.models.fields.related import ManyToManyField
# Create your models here.



class Post(models.Model):

    author=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='posts',on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    likes=ManyToManyField(settings.AUTH_USER_MODEL,related_name='liked_posts')
    description=models.TextField(max_length=500)
    image=models.ImageField(null=True,blank=True)
    createdAt=models.DateTimeField(auto_now_add=True)
    isPublished=models.BooleanField(default=False)
