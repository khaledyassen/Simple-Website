from django.shortcuts import redirect, render
from .forms import BuyingProducts_forms
from .models import BuyingProducts
from django.contrib.auth.decorators import login_required
from Home.decorate import customer_only
# Create your views here.

# The Products of app

# Display the Products

@login_required(login_url='LOGINPAGE')
@customer_only
def Products(request):
  context={}
  return render(request,'Products/Products.html',context)

# Buying the products

@login_required(login_url='LOGINPAGE')
@customer_only
def Buying(request):
  bPForms=BuyingProducts_forms()
  if request.method=='POST':
    bPForms=BuyingProducts_forms(request.POST, request.FILES)
    if bPForms.is_valid():
      bPForms.save()
      return redirect('PRODUCTS')
  context={'bPForms':bPForms}
  return render(request,'Products/buying.html',context)

# Show Products

@login_required(login_url='LOGINPAGE')
def ShowProducts(request):
  bpforms=BuyingProducts.objects.all()
  context={'bpforms':bpforms}
  return render(request,'Products/showProducts.html',context)

# Update Product

@login_required(login_url='LOGINPAGE')
def UpdateProducts(request,pk):
  prdct=BuyingProducts.objects.get(id=pk)
  upprdct=BuyingProducts_forms(instance=prdct)
  if request.method=='POST':
    upprdct=BuyingProducts_forms(request.POST,instance=prdct)
    if upprdct.is_valid():
      upprdct.save()
      return redirect('SHOWPRODUCTS')
  context={'upprdct':upprdct}
  return render(request,'Products/update.html',context)

# Delete the product

@login_required(login_url='LOGINPAGE')
def DeleteProducts(request,pk):
  prdct=BuyingProducts.objects.get(id=pk)
  if request.method=='POST':
    prdct.delete()
    return redirect('SHOWPRODUCTS')
  context={'prdct':prdct}
  return render(request,'Products/delete.html',context)