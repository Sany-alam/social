from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Follow(models.Model):
    following = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='following')
    follower = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='follower')
    status = models.BooleanField(default=False)
    types = models.CharField(max_length=50,choices=[('see_first','See first'),('follow','Follow'),('unfollow','Unfollow'),('reequest','request')],default='follow')
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True)
    def __str__(self):
        return self.follower.username+" following to "+self.following.username