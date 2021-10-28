from django.shortcuts import redirect

def unauthincated(val):
  def wrapperfunction(request,*args,**kwargs):
    if request.user.is_authenticated:
      return redirect('PRODUCTS')
    else:
      return val(request,*args,**kwargs)
  return wrapperfunction

# customer only

def customer_only(val):
  def wrapperfunction(request,*args,**kwargs):
    group=None
    if request.user.groups.exists():
      group=request.user.groups.all()[0].name
    if group=='customer':
      return val(request,*args,**kwargs)
    if group=='admin':
      return redirect('SHOWPRODUCTS')
  return wrapperfunction

