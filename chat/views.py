from django.shortcuts import render
from django.http import HttpResponse
from .models import Inbox
from django.db.models import Q

# Create your views here.
def chat(request):
    return render(request,'home/chat.html')

def chatlist(request):
    a = Inbox.objects.filter(Q(owner2=request.user)|Q(owner1=request.user))
    b = ""
    for c in a:
        if c.owner1==request.user:
            user = c.owner2.username
            if c.owner2.is_active:
                active = "<small>Active</small>"
        elif c.owner2==request.user:
            user = c.owner1.username
            if c.owner1.is_active:
                active = "<small>(Active)</small>"
        b += """
        <a class="chat-list-item p-h-25" href="javascript:void(0);" onclick="chat("""+str(c.id)+""")">
            <div class="media align-items-center">
                <div class="avatar avatar-image">
                    <img src="assets/images/avatars/thumb-1.jpg" alt="">
                </div>
                <div class="p-l-15">
                    <h5 class="m-b-0">"""+user+""" """+active+"""</h5>
                    <p class="msg-overflow m-b-0 text-muted font-size-13">
                        Wow, that was cool!
                    </p>
                </div>
            </div>
        </a>
        """
    return HttpResponse(b)