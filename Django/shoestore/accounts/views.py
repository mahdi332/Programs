from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect , HttpResponse
from django.shortcuts import render
from django.urls import reverse 
from .models import User
from History.models import history
# Create your views here.
def signin_section(request):
    return render(request, 'accounts/signin.html')

def signin_view(request):
    username=request.POST["username"]
    password=request.POST["password"]
    confirm_password=request.POST["confirm_password"]
    email=request.POST["email"]
    if password==confirm_password:
        u=User.objects.create_user(username=username,password=password,email=email)
        u.save()
        history.objects.create(user=u)
        return HttpResponseRedirect(reverse('accounts:login_section'))
    else:
        password_incorrect="Password doesn't match"
        return render(request,'accounts/signin.html',{"password_incorrect":password_incorrect})

def login_section(request):
    return render(request,'accounts/login.html')

def login_view(request):
    username=request.POST["username"]
    password=request.POST["password"]
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return HttpResponseRedirect(reverse('game:menu'))
    else:
        login_failed="Login failed, please try again"
        return render(request,"accounts/login.html",{"login_failed":login_failed})
    
def logout_view(request):
    logout(request)
    return HttpResponse("SUCCES")