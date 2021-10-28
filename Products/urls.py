from django.urls import path
from . import views

urlpatterns=[
  path('',views.Products,name='PRODUCTS'),
  path('buying/',views.Buying,name='BUYING'),
  path('products/',views.ShowProducts,name='SHOWPRODUCTS'),
  path('UpdateProducts/<str:pk>',views.UpdateProducts,name='UPDATERODUCTS'),
  path('DeleteProducts/<str:pk>',views.DeleteProducts,name='DELETEPRODUCTS'),
]