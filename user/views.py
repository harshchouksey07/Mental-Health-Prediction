from django.shortcuts import redirect, render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import usertab

# Create your views here.
def login_user(request):
    if request.method=="POST":
        username=request.POST.get("username")
        passw=request.POST.get("pass")
        user=authenticate(username=username,password=passw)
        if user is not None:
            login(request,user)
            return render(request,'form.html')
        else:
            return HttpResponse("worng Password")
    return render(request,'loginf.html')
def logout_user(request):
    logout(request)
    return redirect("/")

def register_user(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        username=request.POST.get('Username')
        email=request.POST.get("email")
        passw=request.POST.get('pass')
        passwc=request.POST.get('password_confirmation')

        if passw==passwc:
            myuser=usertab.objects.create(fname,lname,email,username,passw)
            myuser.set_password(passw)
            myuser.save()
            return redirect("/login/")
        else:
            return HttpResponse("invalid password")
    return render(request,'register.html')
