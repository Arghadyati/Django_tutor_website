from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
from home.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
# Create your views here.

def home(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,subject=subject,message=message,date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent")
    return render(request,'contact.html')
def services(request):
    return render(request,'services.html')

def loginUser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            
            return redirect("/")
        else:
            
            return render(request,'login.html')
    # A backend authenticated the credentials
    
    
    # No backend authenticated the credentials
   
    return render(request,'login.html')

def logoutuser(request):

    logout(request)
    
    return redirect("/login")

