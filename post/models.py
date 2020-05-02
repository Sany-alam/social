from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='author')
    title = models.CharField(max_length=50)
    post = models.TextField()
    reference = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return "Posted By "+self.owner.username

class Comment(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True)