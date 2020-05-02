from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name="profile")
    phone = models.IntegerField()
    bio = models.TextField()
    birthdate = models.DateField()
    gender = models.CharField(max_length=50,choices=(('male','Male'),('female','Female'),('others','others')),default="male")
    address = models.CharField(max_length=50)
    status = models.CharField(max_length=250,choices=[('single','Single'),('mingle','in a relationship'),('dual','Married'),('commited','commited')])
    created_at = models.DateTimeField(auto_now_add=True,auto_now=False,blank=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True)
    def __str__(self):
        return self.user.username