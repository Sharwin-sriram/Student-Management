from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *

# Create your views here.

def login_page(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not User.objects.filter(username = username).exists():
      messages.error(request,'Invalid Username')
      return redirect('/login/')
    
    user = authenticate(username=username,password=password)
    
    
    if user is None:
      messages.error(request,'Invalid Password')
      return redirect('/login/')
    else:
      login(request,user)
      return redirect('/home/')
    
  return render(request,"index.html")
  
  

def register(request):
  return render(request,'index.html')

def reset_password(request):
  return render(request,'index.html')

