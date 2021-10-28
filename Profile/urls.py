from django.urls import path
from . import views
urlpatterns=[
  path('profile/',views.settingsPage,name='USERPROFILE'),
  path('contactus/',views.contactUSPage,name='CONTACTUS'),
]