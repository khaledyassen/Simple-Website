
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import *
from Home.decorate import customer_only
# Create your views here.

@login_required(login_url='LOGINPAGE')
@customer_only
def settingsPage(request):
  customer=request.user.customer
  form=customerForm(instance=customer)
  if request.method=='POST':
    form=customerForm(request.POST,request.FILES,instance=customer)
    if form.is_valid:
      form.save()
  context={'form':form}
  return render(request,'Profile/showuser_profile.html',context)

@login_required(login_url='LOGINPAGE')
@customer_only
def contactUSPage(request):
  cUP=contactUSForm()
  if request.method=='POST':
    cUP=contactUSForm(request.POST)
    if cUP.is_valid():
      cUP.save()
      return redirect('PRODUCTS')
  context={'form':cUP}
  return render(request,'Profile/contactUS.html',context)