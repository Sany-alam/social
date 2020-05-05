from django.shortcuts import render
from django.http import HttpResponse
from .models import Follow
from django.contrib.auth.models import User

# Create your views here.
def follow(request):
    return render(request,'home/follow.html')

def addfollowing(request):
    a = User.objects.get(id=int(request.POST['id']))
    if Follow.objects.filter(following=a,follower=request.user).exists():
        return HttpResponse("You are already following")
    else:
        follower = request.user
        following = a
        q = Follow(following=following,follower=follower)
        q.save()
        return HttpResponse("done")

def following(request):
    a = Follow.objects.filter(follower=request.user.id)
    b=""
    for following in a:
        b += """
        <div class="d-flex justify-content-between align-items-center m-b-30 ">
            <div class="d-flex">
                <div class="avatar avatar-image">
                    <img src="/static/images/avatars/thumb-1.jpg" alt="">
                </div>
                <div class="m-l-15">
                    <a href="/profile/"""+following.following.username+"""" class="text-dark m-b-0 font-weight-semibold">"""+following.following.first_name+""" """+following.following.last_name+"""</a>
                    <p class="m-b-0 text-muted font-size-13">Following from """+str(following.following.profile.created_at.strftime("%d-%h-%Y"))+"""</p>
                </div>
            </div>
            <div class="d-flext justify-content-between align-items-center">
                <a href="#" style="padding: .35rem 0.4rem;" class="mx-md-2 btn btn-info btn-tone">
                    <i class="fab fa-rocketchat"></i>
                </a>
                <a onclick="unfollow("""+str(following.following.id)+""")" href="#" style="padding: .35rem 0.4rem;" class="mx-md-2 btn btn-info btn-tone">
                    <i class="fas fa-user-minus"></i>
                </a>
            </div>
        </div>"""
    return HttpResponse(b)

def follower(request):
    a = Follow.objects.filter(following=request.user.id)
    b=""
    for follower in a:
        b += """
        <div class="d-flex justify-content-between align-items-center m-b-30 ">
            <div class="d-flex">
                <div class="avatar avatar-image">
                    <img src="/static/images/avatars/thumb-1.jpg" alt="">
                </div>
                <div class="m-l-15">
                    <a href="/profile/"""+follower.follower.username+"""" class="text-dark m-b-0 font-weight-semibold">"""+follower.follower.first_name+""" """+follower.follower.last_name+"""</a>
                    <p class="m-b-0 text-muted font-size-13">follower from """+str(follower.follower.profile.created_at.strftime("%d-%h-%Y"))+"""</p>
                </div>
            </div>
            <div class="d-flext justify-content-between align-items-center">
                <a href="#" style="padding: .35rem 0.4rem;" class="mx-md-2 btn btn-info btn-tone">
                    <i class="fab fa-rocketchat"></i>
                </a>
                <a onclick="unfollow("""+str(follower.follower.id)+""")" href="#" style="padding: .35rem 0.4rem;" class="mx-md-2 btn btn-info btn-tone">
                    <i class="fas fa-user-minus"></i>
                </a>
            </div>
        </div>"""
    return HttpResponse(b)