from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Profile

def profile(request, username="default"):
    if username == "default":
        u = User.objects.get(profile__user=request.user.id)
        return render(request,'home/profile.html', {'profile':u})
    else:
        uid = User.objects.get(username=username)
        u = User.objects.filter(profile__user=uid.id).get()
        return render(request,'home/profile.html', {'profile':u})

# Create your views here.
def register(request):
    if request.user.is_anonymous:
        if request.method=='POST':
            if User.objects.filter(username=request.POST['username']).exists():
                messages.error(request,"Username has taken, username must be unique")
                return redirect('register')
            else:
                if User.objects.filter(email=request.POST['email']).exists():
                    messages.error(request,"Email has taken, Email must be unique")
                    return redirect('register')
                else:
                    if len(request.POST['password']) > 15 or len(request.POST['password']) < 6:
                        messages.error(request,"Password must be 6 to 15 charecters")
                        return redirect('register')
                    else:
                        if request.POST['password'] != request.POST['confirmPassword']:
                            messages.error(request,"Password not match")
                            return redirect('register')
                        else:
                            username = request.POST['username']
                            email = request.POST['email']
                            firstname = request.POST['firstname']
                            lastname = request.POST['lastname']
                            password = request.POST['password']
                            myuser = User.objects.create_user(username,email,password)
                            myuser.first_name = firstname
                            myuser.last_name = lastname
                            myuser.save()

                            phone = request.POST['phone']
                            bio = request.POST['bio']
                            birthdate = request.POST['birthdate']
                            gender = request.POST['gender']
                            address = request.POST['address']
                            status = request.POST['status']
                            myprofile = Profile(user=myuser, phone=phone, bio=bio, birthdate=birthdate, gender=gender, address=address, status=status)
                            myprofile.save()
                            messages.success(request,"Account has been successfully created, Login to start session!")
                            return redirect('home')
        else:
            return render(request,'auth/register.html')
    else:
        return redirect('home')


def userlogin(request):
    if request.user.is_anonymous:
        if request.method=='POST':
            uname = request.POST['username']
            pas = request.POST['password']
            user = authenticate(request,username=uname,password=pas)
            if user is not None:
                login(request,user)
                messages.success(request,'Succsfully loggedin!')
                if request.GET.get('next',None):
                    return redirect(request.GET['next'])
                return redirect('home')
            else:
                messages.error(request,'Credentials are wrong!')
                return redirect('login')
        else:
            return render(request,'auth/login.html')
    else:
        return redirect('home')

@login_required(login_url="/login")
def home(request):
    return render(request,'home/home.html')

@login_required(login_url="/login/")
def userlogout(request):
    if request.method=='POST':
        logout(request)
        messages.success(request,'Succsfully loggedout!')
        return redirect('login')
    else:
        return redirect('home')




def ValidUsername(request):
    uname = request.POST['uname']
    if User.objects.filter(username=uname).exists():
        return HttpResponse("positive")
    else:
        return HttpResponse("negative")

def Validemail(request):
    email = request.POST['email']
    if User.objects.filter(email=email).exists():
        return HttpResponse("positive")
    else:
        return HttpResponse("negative")
