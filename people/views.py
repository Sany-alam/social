from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from follow.models import Follow
from django.db.models import Q

# Create your views here.
def peoples(request):
    return render(request,'home/people.html')

def showpeoples(request):
    ofst = request.POST['offset']
    lmt = request.POST['limit']
    data = User.objects.order_by('-id')[int(ofst):int(ofst)+int(lmt)]
    all = ""
    for p in data:
        # if Follow.objects.filter(follwer=request.user.id).filter(follwing=p.id).exists():
        #     icon = """<a onclick="follow("""+str(p.id)+""")" href="#" style="padding: .35rem 0.4rem;" class="mx-md-2 btn btn-info btn-tone">
        #             <i class="fas fa-user-plus"></i>
        #         </a>"""
        # elif Follow.objects.filter(follwing=request.user.id).filter(follwer=p.id).exists():
        #     icon = """<a onclick="follow("""+str(p.id)+""")" href="#" style="padding: .35rem 0.4rem;" class="mx-md-2 btn btn-info btn-tone">
        #             <i class="fas fa-user-plus"></i>
        #         </a>"""
        # else:
        #     icon = """<a onclick="follow("""+str(p.id)+""")" href="#" style="padding: .35rem 0.4rem;" class="mx-md-2 btn btn-info btn-tone">
        #             <i class="fas fa-user-plus"></i>
        #         </a>"""
        all += """
        <div class="d-flex justify-content-between align-items-center m-b-30 ">
            <div class="d-flex">
                <div class="avatar avatar-image">
                    <img src="/static/images/avatars/thumb-1.jpg" alt="">
                </div>
                <div class="m-l-15">
                    <a href="/profile/"""+p.username+"""" class="text-dark m-b-0 font-weight-semibold">"""+p.first_name+""" """+p.last_name+"""</a>
                    <p class="m-b-0 text-muted font-size-13">Joined at """+str(p.profile.created_at.strftime("%d-%h-%Y"))+"""</p>
                </div>
            </div>
            <div class="d-flext justify-content-between align-items-center">
                <a href="#" style="padding: .35rem 0.4rem;" class="mx-md-2 btn btn-info btn-tone">
                    <i class="fab fa-rocketchat"></i>
                </a>
                <a onclick="follow("""+str(p.id)+""")" href="#" style="padding: .35rem 0.4rem;" class="mx-md-2 btn btn-info btn-tone">
                    <i class="fas fa-user-plus"></i>
                </a>
            </div>
        </div>
        """
    return HttpResponse(all)