from django.shortcuts import render
from django.http import HttpResponse
from .models import Follow
from django.contrib.auth.models import User

# Create your views here.
def follow(request):
    return render(request,'home/follow.html')

def following(request):
    a = User.objects.get(id=int(request.POST['id']))
    # return HttpResponse(a)
    follower = request.user
    following = a
    q = Follow(following=following,follower=follower)
    q.save()
    return HttpResponse("done")