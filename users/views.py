from django.shortcuts import render , redirect

from django.contrib.auth.models import User,auth
from django.contrib import messages
from images.views import Display_Images
# Create your views here.

def register(request):
    
    if request.method=="POST":
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect("register")

            elif User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect("register")

            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Password Not matched")
            return render(request,'users/register_form.html',)
            
    else:
        return render(request,'users/register_form.html',)

    

def login(request):
    if request.method=="POST":
        username=request.POST['login_username']
        email=request.POST['login_email']
        password=request.POST['login_password']

        user=auth.authenticate(username=username,email=email,password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"Credentials Invalid")
            return redirect("login")
    else:
        return render(request,'users/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

