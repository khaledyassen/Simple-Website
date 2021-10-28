from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
  path('register/',views.RegisterPage,name='REGISTERPAGE'),
  path('',views.LoginPage,name='LOGINPAGE'),
  path('logout/',views.logout,name='LOGOUT'),


  path('reset_password/',
  auth_views.PasswordResetView.as_view(),
  name="RESET_PASSWORD"),
  path('reset_password_sent/',
  auth_views.PasswordResetDoneView.as_view(),
  name="password_reset_done"),
  path('reset/<uidb64>/<token>',
  auth_views.PasswordResetConfirmView.as_view(),
  name="password_reset_confirm"),
  path('reset_password_complete/',
  auth_views.PasswordResetCompleteView.as_view(template_name='Home/password_reset_done.html'),
  name="password_reset_complete")
]