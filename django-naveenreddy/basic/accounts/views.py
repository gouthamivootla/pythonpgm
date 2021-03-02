from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info('credential are wrong')
            return redirect('login')
    else:
        return render(request,'login.html')
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['passsword2']
        if(password1==password2):
            if(User.objects.filter(username=username).exists()):
                messages.info(request,"user name alreadytoken")
                return redirect('register')
            elif(User.objects.filter(email=email).exists()):
                messages.info(request,"email already taken")
                return redirect('register')
            else:    
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
               
                return redirect('login')
            
        else:
            messages.info(request,"passwords are not matched")
            return redirect('/')
    else:
        return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')