from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.fields import related 
# Create your models here.

class Author(AbstractUser):
    profileImage = models.ImageField(null=True,blank=True)
    my_followers = models.ManyToManyField('self',through='AuthorFollowing',through_fields=('following_id','follower_id'))
    my_following = models.ManyToManyField('self',through='AuthorFollowing',through_fields=('follower_id','following_id'))





class AuthorFollowing(models.Model):
    following_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='followers')
    follower_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='following')
    createdAt = models.DateTimeField(settings.AUTH_USER_MODEL,auto_now=True)


