from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Post
from .models import Comment
from follow.models import Follow
from django.utils.text import Truncator
import json
from django.db.models import Q

# Create your views here.
def single_post(request,post_id):
    p = Post.objects.get(id=post_id)
    return render(request,'home/post.html',{'post':p})


def post(request):
    ofst = request.POST['offset']
    lmt = request.POST['limit']
    posts = Post.objects.filter(Q(owner=request.user.id)|Q(owner__in=Follow.objects.filter(follower=request.user.id).values('following'))).order_by('-id')[int(ofst):int(ofst)+int(lmt)]
    p = ""
    for post in posts:
        updatetime = post.updated_at
        ptime = updatetime.strftime("%d-%h-%Y %I:%M:%p")
        p += """
        <div class="card">
            <div class="card-body">
                <div class="row">
                    <div class="col-md-4">
                        <img class="img-fluid" src="{% static '/images/others/img-2.jpg' %}" alt="">
                    </div>
                    <div class="col-md-8">
                        <h4 class="m-b-10">"""+post.title +"""</h4>
                        <div class="d-flex align-items-center m-t-5 m-b-15">
                            <div class="avatar avatar-image avatar-sm">
                                <img src="{% static '/images/avatars/thumb-8.jpg' %}" alt="">
                            </div>
                            <div class="m-l-10">
                                <span class="text-gray font-weight-semibold">"""+ post.owner.first_name +""" """+post.owner.last_name +"""</span>
                                <span class="m-h-5 text-gray">|</span>
                                <span class="text-gray">"""+ ptime +"""</span>
                            </div>
                        </div>
                        <p class="m-b-20">"""+ Truncator(post.post).words(50) +"""</p>
                        <div class="text-right">
                            <a class="btn btn-hover font-weight-semibold" href="/posts/"""+str(post.id)+"""">
                                <span>Read More</span>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """
    return HttpResponse(p)

def cpost(request):
    title = request.POST['title']
    reference = request.POST['reference']
    post = request.POST['content']
    i = Post(owner_id=request.user.id,title=title,post=post,reference=reference)
    i.save()
    return HttpResponse("done")

def addcomment(request):
    hidden_post_id = request.POST['hidden_post_id']
    comment = request.POST['comment']
    i = Comment(owner_id=request.user.id,post_id=hidden_post_id,comment=comment)
    i.save()
    return HttpResponse("done")

def comments(request,id):
    i = Comment.objects.filter(post_id=id).order_by("-id")
    j = ""
    for k in i:
        if request.user.username == k.owner.username:
            owner = "Me"
        else:
            owner = k.owner.first_name+" "+k.owner.last_name
        j += """
        <li class="list-group-item p-h-0">
            <div class="media m-b-15">
                <div class="avatar avatar-image">
                    <img src="assets/images/avatars/thumb-8.jpg" alt="">
                </div>
                <div class="media-body m-l-20">
                    <h6 class="m-b-0">
                        <a href="#" class="text-dark">"""+owner+"""</a>
                    </h6>
                    <span class="font-size-13 text-gray">28th Jul 2018</span>
                </div>
            </div>
            <span>"""+ k.comment +"""</span>
            <div class="m-t-15">
                <ul class="list-inline text-right">
                    <li class="d-inline-block m-r-20">
                        <a class="text-dark" href="javascript:void(0)">
                            <i class="anticon m-r-5 anticon-like"></i>
                            <span>43</span>
                        </a>
                    </li>
                    <li class="d-inline-block m-r-30">
                        <a class="text-dark" href="javascript:void(0)">
                            <i class="anticon m-r-5 anticon-message"></i>
                            <span>Reply</span>
                        </a>
                    </li>
                </ul>
            </div>
        </li>
        """
    data = {'loop':j,'total':i.count()}
    return HttpResponse(json.dumps(data))