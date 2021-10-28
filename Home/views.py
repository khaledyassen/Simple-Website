from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import register_page
from django.contrib.auth import authenticate,login,logout
from .decorate import unauthincated

# Create your views here.

# LoginPage

@unauthincated
def LoginPage(request):
  if request.method=='POST':
    user_name=request.POST.get('UserName')
    passrd=request.POST.get('Password')
    user_login=authenticate(request,username=user_name,password=passrd)
    if user_login is not None:
      login(request,user_login)
      return redirect('PRODUCTS')
    else:
      return render(request,'Home/error.html')
  context={}
  return render(request,'Home/Login.html',context)

# Logout

@unauthincated
def LogOut(request):
  logout(request)
  return redirect('LOGINPAGE')

# RegisterPage

@unauthincated
def RegisterPage(request):
  user_register=register_page()
  if request.method=='POST':
    user_register=register_page(request.POST)
    if user_register.is_valid():
      user_group_register=user_register.save()
      group=Group.objects.get(name='customer')
      user_group_register.groups.add(group)
      return redirect('LOGINPAGE') 
  context={'user_register':user_register}
  return render(request,'Home/Register.html',context)
