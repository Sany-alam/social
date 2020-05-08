from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Inbox(models.Model):
    owner1 = models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner1',blank=True)
    owner2 = models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner2',blank=True)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True)
    # def __str__(self):
    #     return self.owner1.username+" with "+self.owner2.username

class Message(models.Model):
    inbox = models.ForeignKey(Inbox,on_delete=models.CASCADE,blank=True)
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name="sender",blank=True)
    reciever = models.ForeignKey(User,on_delete=models.CASCADE,related_name="reciever",blank=True)
    message = models.TextField(blank=True,null=True)
    files = models.FileField(upload_to="files",blank=True,null=True)
    images = models.ImageField(upload_to="images",blank=True,null=True)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True)
    def __str__(self):
        return self.sender.username+" messsages to "+self.reciever.username